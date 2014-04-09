# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014 OpenStack Foundation
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

from keystone import identity
from keystone import exception
from keystone.common import controller
from keystone.common import utils


class TfaController(identity.controllers.UserV3):

    @controller.protected()
    def reset_secret(self, context, user_id):
        token_id = context.get('token_id')
        token_ref = self.token_api.get_token(token_id)
        user_id_from_token = token_ref['user']['id']

        # You have to be either the user, or an admin
        if user_id_from_token != user_id and self.assert_admin(context) is not None:
            raise exception.Forbidden('Token belongs to another user')

        user = self.get_user(context, user_id)['user']
        user['tfa_secret'] = utils.generate_tfa_secret()
        super(TfaController, self).update_user(context, user_id, user)
        return {'secret': user['tfa_secret']}
