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
# To access what is returned
# json load the response.text in your script...like this
# ----------------------------------------------------------------
# managers=json.loads(iLo_managers.text)
# print(managers['Members'])


from lib.actions import HpeIloBaseAction
import json

class chassis(HpeIloBaseAction):
    def run(self):
        # Do a GET on a given path
        iLo_managers = self.client.get("/redfish/v1/managers/", None)
        return (True, iLo_managers)
