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
module: azure_rm_postgresqldatabase
version_added: "2.5"
short_description: Manage PostgreSQL Database instance
description:
    - Create, update and delete instance of PostgreSQL Database

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    name:
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
  - name: Create (or update) PostgreSQL Database
    azure_rm_postgresqldatabase:
      resource_group: resource_group_name
      server_name: server_name
      name: database_name
      charset: charset
      collation: collation
'''

RETURN = '''
state:
    description: Current state of PostgreSQL Database
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID
            returned: always
            type: str
            sample: id
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


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDatabases(AzureRMModuleBase):
    """Configuration class for an Azure RM PostgreSQL Database resource"""

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
            name=dict(
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

        self.resource_group = None
        self.server_name = None
        self.name = None
        self.parameters = dict()

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

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

        old_response = self.get_postgresqldatabase()

        if not old_response:
            self.log("PostgreSQL Database instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("PostgreSQL Database instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if PostgreSQL Database instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the PostgreSQL Database instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_postgresqldatabase()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(self.results['state'])

            # remove unnecessary fields from return state
            self.results['state'].pop('name', None)
            self.results['state'].pop('type', None)
            self.results['state'].pop('charset', None)
            self.results['state'].pop('collation', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("PostgreSQL Database instance deleted")
            self.delete_postgresqldatabase()
            self.results['changed'] = True
        else:
            self.log("PostgreSQL Database instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_postgresqldatabase(self):
        '''
        Creates or updates PostgreSQL Database with the specified configuration.

        :return: deserialized PostgreSQL Database instance state dictionary
        '''
        self.log("Creating / Updating the PostgreSQL Database instance {0}".format(self.name))

        try:
            response = self.mgmt_client.databases.create_or_update(self.resource_group,
                                                                   self.server_name,
                                                                   self.name,
                                                                   self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the PostgreSQL Database instance.')
            self.fail("Error creating the PostgreSQL Database instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_postgresqldatabase(self):
        '''
        Deletes specified PostgreSQL Database instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the PostgreSQL Database instance {0}".format(self.name))
        try:
            response = self.mgmt_client.databases.delete(self.resource_group,
                                                         self.server_name,
                                                         self.name)
        except CloudError as e:
            self.log('Error attempting to delete the PostgreSQL Database instance.')
            self.fail("Error deleting the PostgreSQL Database instance: {0}".format(str(e)))

        return True

    def get_postgresqldatabase(self):
        '''
        Gets the properties of the specified PostgreSQL Database.

        :return: deserialized PostgreSQL Database instance state dictionary
        '''
        self.log("Checking if the PostgreSQL Database instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.databases.get(self.resource_group,
                                                      self.server_name,
                                                      self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("PostgreSQL Database instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the PostgreSQL Database instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMDatabases()

if __name__ == '__main__':
    main()
