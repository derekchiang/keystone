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

"""Main entry point into the TFA Credentials service."""

#import uuid

#from keystoneclient.contrib.tfa import utils as tfa_utils

from keystone.common import controller
#from keystone.common import dependency
#from keystone.common import utils
#from keystone import exception
#from keystone import token


#@dependency.requires('catalog_api', 'credential_api', 'token_provider_api')
class TfaController(controller.V3Controller):
    def hello(self, context, credentials=None, tfaCredentials=None):
        print("hello world")
        return {'hello': 'world'}
