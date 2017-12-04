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
module: azure_rm_sql_serverconnectionpolicies
version_added: "2.5"
short_description: Manage ServerConnectionPolicies instance
description:
    - Create, update and delete instance of ServerConnectionPolicies

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    connection_policy_name:
        description:
            - The name of the connection policy.
        required: True
    connection_type:
        description:
            - "The server connection type. Possible values include: 'Default', 'Proxy', 'Redirect'"
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) ServerConnectionPolicies
    azure_rm_sql_serverconnectionpolicies:
      resource_group: resource_group_name
      server_name: server_name
      connection_policy_name: connection_policy_name
      connection_type: connection_type
'''

RETURN = '''
state:
    description: Current state of ServerConnectionPolicies
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID.
            returned: always
            type: str
            sample: id
        name:
            description:
                - Resource name.
            returned: always
            type: str
            sample: name
        type:
            description:
                - Resource type.
            returned: always
            type: str
            sample: type
        kind:
            description:
                - Metadata used for the Azure portal experience.
            returned: always
            type: str
            sample: kind
        location:
            description:
                - Resource location.
            returned: always
            type: str
            sample: location
        connection_type:
            description:
                - "The server connection type. Possible values include: 'Default', 'Proxy', 'Redirect'"
            returned: always
            type: str
            sample: connection_type
'''

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


class AzureRMServerConnectionPolicies(AzureRMModuleBase):
    """Configuration class for an Azure RM ServerConnectionPolicies resource"""

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
            connection_policy_name=dict(
                type='str',
                required=True
            ),
            connection_type=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.server_name = None
        self.connection_policy_name = None
        self.connection_type = None

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerConnectionPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                              supports_check_mode=True,
                                                              supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_serverconnectionpolicies()

        if not old_response:
            self.log("ServerConnectionPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ServerConnectionPolicies instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ServerConnectionPolicies instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ServerConnectionPolicies instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_serverconnectionpolicies()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(self.results['state'])

            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ServerConnectionPolicies instance deleted")
            self.delete_serverconnectionpolicies()
            self.results['changed'] = True
        else:
            self.log("ServerConnectionPolicies instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_serverconnectionpolicies(self):
        '''
        Creates or updates ServerConnectionPolicies with the specified configuration.

        :return: deserialized ServerConnectionPolicies instance state dictionary
        '''
        self.log("Creating / Updating the ServerConnectionPolicies instance {0}".format(self.connection_policy_name))

        try:
            response = self.mgmt_client.server_connection_policies.create_or_update(self.resource_group,
                                                                                    self.server_name,
                                                                                    self.connection_policy_name,
                                                                                    self.connection_type)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ServerConnectionPolicies instance.')
            self.fail("Error creating the ServerConnectionPolicies instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_serverconnectionpolicies(self):
        '''
        Deletes specified ServerConnectionPolicies instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ServerConnectionPolicies instance {0}".format(self.connection_policy_name))
        try:
            response = self.mgmt_client.server_connection_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ServerConnectionPolicies instance.')
            self.fail("Error deleting the ServerConnectionPolicies instance: {0}".format(str(e)))

        return True

    def get_serverconnectionpolicies(self):
        '''
        Gets the properties of the specified ServerConnectionPolicies.

        :return: deserialized ServerConnectionPolicies instance state dictionary
        '''
        self.log("Checking if the ServerConnectionPolicies instance {0} is present".format(self.connection_policy_name))
        found = False
        try:
            response = self.mgmt_client.server_connection_policies.get(self.resource_group,
                                                                       self.server_name,
                                                                       self.connection_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ServerConnectionPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ServerConnectionPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMServerConnectionPolicies()

if __name__ == '__main__':
    main()
