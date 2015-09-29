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

from kuryr.schemata import endpoint_delete


LEAVE_SCHEMA = endpoint_delete.ENDPOINT_DELETE_SCHEMA
LEAVE_SCHEMA[u'title'] = u'Leave endpoint'
LEAVE_SCHEMA[u'links'] = [{
    u'method': u'POST',
    u'href': u'/NetworkDriver.Leave',
    u'description': u'Unbinds the endpoint from the container.',
    u'rel': u'self',
    u'title': u'Join'
}]