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
module: azure_rm_postgresql_database
version_added: "2.5"
short_description: Manage Databases instance
description:
    - Create, update and delete instance of Databases

options:
    resource_group_name:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    database_name:
        description:
            - The name of the database.
        required: True
    charset:
        description:
            - The charset of the database.
    collation:
        description:
            - The collation of the database.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Databases
    azure_rm_postgresql_database:
      resource_group_name: resource_group_name
      server_name: server_name
      database_name: database_name
      charset: charset
      collation: collation
'''

RETURN = '''
state:
    description: Current state of Databases
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID
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
        charset:
            description:
                - The charset of the database.
            returned: always
            type: str
            sample: charset
        collation:
            description:
                - The collation of the database.
            returned: always
            type: str
            sample: collation
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.postgresql import PostgreSQLManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDatabases(AzureRMModuleBase):
    """Configuration class for an Azure RM Databases resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            charset=dict(
                type='str',
                required=False
            ),
            collation=dict(
                type='str',
                required=False
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.parameters = dict()

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None

        super(AzureRMDatabases, self).__init__(derived_arg_spec=self.module_arg_spec,
                                               supports_check_mode=True,
                                               supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif key == "charset":
                self.parameters["charset"] = kwargs[key]
            elif key == "collation":
                self.parameters["collation"] = kwargs[key]

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_databases()

        if not old_response:
            self.log("Databases instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
        else:
            self.log("Databases instance already exists")
            if self.state == 'absent':
                self.delete_databases()
                self.results['changed'] = True
                self.log("Databases instance deleted")
            elif self.state == 'present':
                self.log("Need to check if Databases instance has to be deleted or may be updated")

        if self.state == 'present':

            self.log("Need to Create / Update the Databases instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_databases()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = (cmp(old_response, self.results['state']) != 0)

            self.log("Creation / Update done")

        return self.results

    def create_update_databases(self):
        '''
        Creates or updates Databases with the specified configuration.

        :return: deserialized Databases instance state dictionary
        '''
        self.log("Creating / Updating the Databases instance {0}".format(self.database_name))

        try:
            response = self.mgmt_client.databases.create_or_update(self.resource_group_name,
                                                                   self.server_name,
                                                                   self.database_name,
                                                                   self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Databases instance.')
            self.fail("Error creating the Databases instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_databases(self):
        '''
        Deletes specified Databases instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Databases instance {0}".format(self.database_name))
        try:
            response = self.mgmt_client.databases.delete(self.resource_group_name,
                                                         self.server_name,
                                                         self.database_name)
        except CloudError as e:
            self.log('Error attempting to delete the Databases instance.')
            self.fail("Error deleting the Databases instance: {0}".format(str(e)))

        return True

    def get_databases(self):
        '''
        Gets the properties of the specified Databases.

        :return: deserialized Databases instance state dictionary
        '''
        self.log("Checking if the Databases instance {0} is present".format(self.database_name))
        found = False
        try:
            response = self.mgmt_client.databases.get(self.resource_group_name,
                                                      self.server_name,
                                                      self.database_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Databases instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Databases instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMDatabases()

if __name__ == '__main__':
    main()