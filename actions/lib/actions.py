# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

import redfish
from st2common.runners.base_action import Action

class HpeIloBaseAction(Action):
    def __init__(self,config):
        super(HpeIloBaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        login_host = self.config['login_host']
        login_account = self.config['login_account']
        login_password = self.config['login_password']
        ### Create a REDFISH object
        client = redfish.redfish_client(base_url="172.18.35.193",username="Administrator",password="Plexxi100!",default_prefix='/redfish/v1')
        # Login into the server and create a session
        client.login(auth="session")
        return client
