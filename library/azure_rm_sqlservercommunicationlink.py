#!/usr/bin/python
#
# Copyright (c) 2017 Zim Kalinowski, <zikalino@microsoft.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_sqlservercommunicationlink
version_added: "2.5"
short_description: Manage Server Communication Link instance.
description:
    - Create, update and delete instance of Server Communication Link.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    communication_link_name:
        description:
            - The name of the server communication link.
        required: True
    partner_server:
        description:
            - The name of the partner server.
        required: True
    state:
      description:
        - Assert the state of the Server Communication Link.
        - Use 'present' to create or update an Server Communication Link and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Server Communication Link
    azure_rm_sqlservercommunicationlink:
      resource_group: sqlcrudtest-7398
      server_name: sqlcrudtest-4645
      communication_link_name: link1
      partner_server: NOT FOUND
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
state:
    description:
        - The state.
    returned: always
    type: str
    sample: state
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMServerCommunicationLinks(AzureRMModuleBase):
    """Configuration class for an Azure RM Server Communication Link resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            communication_link_name=dict(
                type='str',
                required=True
            ),
            partner_server=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.server_name = None
        self.communication_link_name = None
        self.partner_server = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerCommunicationLinks, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                              supports_check_mode=True,
                                                              supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_servercommunicationlink()

        if not old_response:
            self.log("Server Communication Link instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Server Communication Link instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Server Communication Link instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Server Communication Link instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_servercommunicationlink()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Server Communication Link instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_servercommunicationlink()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_servercommunicationlink():
                time.sleep(20)
        else:
            self.log("Server Communication Link instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]

        return self.results

    def create_update_servercommunicationlink(self):
        '''
        Creates or updates Server Communication Link with the specified configuration.

        :return: deserialized Server Communication Link instance state dictionary
        '''
        self.log("Creating / Updating the Server Communication Link instance {0}".format(self.communication_link_name))

        try:
            response = self.mgmt_client.server_communication_links.create_or_update(resource_group_name=self.resource_group,
                                                                                    server_name=self.server_name,
                                                                                    communication_link_name=self.communication_link_name,
                                                                                    partner_server=self.partner_server)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Server Communication Link instance.')
            self.fail("Error creating the Server Communication Link instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_servercommunicationlink(self):
        '''
        Deletes specified Server Communication Link instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Server Communication Link instance {0}".format(self.communication_link_name))
        try:
            response = self.mgmt_client.server_communication_links.delete(resource_group_name=self.resource_group,
                                                                          server_name=self.server_name,
                                                                          communication_link_name=self.communication_link_name)
        except CloudError as e:
            self.log('Error attempting to delete the Server Communication Link instance.')
            self.fail("Error deleting the Server Communication Link instance: {0}".format(str(e)))

        return True

    def get_servercommunicationlink(self):
        '''
        Gets the properties of the specified Server Communication Link.

        :return: deserialized Server Communication Link instance state dictionary
        '''
        self.log("Checking if the Server Communication Link instance {0} is present".format(self.communication_link_name))
        found = False
        try:
            response = self.mgmt_client.server_communication_links.get(resource_group_name=self.resource_group,
                                                                       server_name=self.server_name,
                                                                       communication_link_name=self.communication_link_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Server Communication Link instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Server Communication Link instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMServerCommunicationLinks()

if __name__ == '__main__':
    main()
