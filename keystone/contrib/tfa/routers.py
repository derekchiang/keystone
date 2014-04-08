# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystone.common import wsgi
from keystone.contrib.tfa import controllers


class TfaExtension(wsgi.ExtensionRouter):
    def add_routes(self, mapper):
        tfa_controller = controllers.TfaController()
        #hello world
        mapper.connect(
            '/tfa',
            controller=tfa_controller,
            action='hello',
            conditions=dict(method=['GET']))
'''
        # validation
        mapper.connect(
            '/tfatokens',
            controller=tfa_controller,
            action='authenticate',
            conditions=dict(method=['POST']))

        # crud
        mapper.connect(
            '/users/{user_id}/credentials/OS-TFA',
            controller=tfa_controller,
            action='create_credential',
            conditions=dict(method=['POST']))
        mapper.connect(
            '/users/{user_id}/credentials/OS-TFA',
            controller=tfa_controller,
            action='get_credentials',
            conditions=dict(method=['GET']))
        mapper.connect(
            '/users/{user_id}/credentials/OS-TFA/{credential_id}',
            controller=tfa_controller,
            action='get_credential',
            conditions=dict(method=['GET']))
        mapper.connect(
            '/users/{user_id}/credentials/OS-TFA/{credential_id}',
            controller=tfa_controller,
            action='delete_credential',
            conditions=dict(method=['DELETE']))
'''

