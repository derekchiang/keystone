# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil

from keystone.common import openssl
from keystone import exception
from keystone import tests
from keystone.tests import default_fixtures
from keystone import token


SSLDIR = tests.dirs.tests('ssl')
CONF = tests.CONF
DEFAULT_DOMAIN_ID = CONF.identity.default_domain_id


CERTDIR = os.path.join(SSLDIR, 'certs')
KEYDIR = os.path.join(SSLDIR, 'private')


class CertSetupTestCase(tests.TestCase):

    def setUp(self):
        super(CertSetupTestCase, self).setUp()
        ca_certs = os.path.join(CERTDIR, 'ca.pem')
        ca_key = os.path.join(CERTDIR, 'cakey.pem')

        self.opt_in_group(
            'signing',
            certfile=os.path.join(CERTDIR, 'signing_cert.pem'),
            ca_certs=ca_certs,
            ca_key=ca_key,
            keyfile=os.path.join(KEYDIR, 'signing_key.pem'))
        self.opt_in_group(
            'ssl',
            ca_certs=ca_certs,
            ca_key=ca_key,
            certfile=os.path.join(CERTDIR, 'keystone.pem'),
            keyfile=os.path.join(KEYDIR, 'keystonekey.pem'))

        self.load_backends()
        self.load_fixtures(default_fixtures)
        self.controller = token.controllers.Auth()

        def cleanup_ssldir():
            try:
                shutil.rmtree(SSLDIR)
            except OSError:
                pass

        self.addCleanup(cleanup_ssldir)

    def test_can_handle_missing_certs(self):
        self.opt_in_group('signing', certfile='invalid')
        user = {
            'id': 'fake1',
            'name': 'fake1',
            'password': 'fake1',
            'domain_id': DEFAULT_DOMAIN_ID
        }
        body_dict = {
            'passwordCredentials': {
                'userId': user['id'],
                'password': user['password'],
            },
        }
        self.identity_api.create_user(user['id'], user)
        self.assertRaises(exception.UnexpectedError,
                          self.controller.authenticate,
                          {}, body_dict)

    def test_create_pki_certs(self):
        pki = openssl.ConfigurePKI(None, None)
        pki.run()
        self.assertTrue(os.path.exists(CONF.signing.certfile))
        self.assertTrue(os.path.exists(CONF.signing.ca_certs))
        self.assertTrue(os.path.exists(CONF.signing.keyfile))

    def test_create_ssl_certs(self):
        ssl = openssl.ConfigureSSL(None, None)
        ssl.run()
        self.assertTrue(os.path.exists(CONF.ssl.ca_certs))
        self.assertTrue(os.path.exists(CONF.ssl.certfile))
        self.assertTrue(os.path.exists(CONF.ssl.keyfile))
