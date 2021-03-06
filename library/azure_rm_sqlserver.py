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
module: azure_rm_sqlserver
version_added: "2.5"
short_description: Manage SQL Server instance.
description:
    - Create, update and delete instance of SQL Server.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    name:
        description:
            - The name of the server.
        required: True
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    admin_username:
        description:
            - Administrator username for the server. Once created it cannot be changed.
    admin_password:
        description:
            - The administrator login password (required for server creation).
    version:
        description:
            - "The version of the server. For example '12.0'."
    identity:
        description:
            - "The identity type. Set this to 'C(system_assigned)' in order to automatically create and assign an Azure Active Directory principal for the
               resource."
        choices:
            - 'system_assigned'
    state:
      description:
        - Assert the state of the SQL Server.
        - Use 'present' to create or update an SQL Server and 'absent' to delete it.
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
  - name: Create (or update) SQL Server
    azure_rm_sqlserver:
      resource_group: resource_group
      name: sqlcrudtest-4645
      location: westus
      admin_username: mylogin
      admin_password: Testpasswordxyz12!
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/sqlcrudtest-7398/providers/Microsoft.Sql/servers/sqlcrudtest-4645
version:
    description:
        - The version of the server.
    returned: always
    type: str
    sample: 12.0
state:
    description:
        - The state of the server.
    returned: always
    type: str
    sample: Ready
fully_qualified_domain_name:
    description:
        - The fully qualified domain name of the server.
    returned: always
    type: str
    sample: sqlcrudtest-4645.database.windows.net
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


class AzureRMServers(AzureRMModuleBase):
    """Configuration class for an Azure RM SQL Server resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str'
            ),
            admin_username=dict(
                type='str'
            ),
            admin_password=dict(
                type='str',
                no_log=True
            ),
            version=dict(
                type='str'
            ),
            identity=dict(
                type='str',
                choices=['system_assigned']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServers, self).__init__(derived_arg_spec=self.module_arg_spec,
                                             supports_check_mode=True,
                                             supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "admin_username":
                    self.parameters["administrator_login"] = kwargs[key]
                elif key == "admin_password":
                    self.parameters["administrator_login_password"] = kwargs[key]
                elif key == "version":
                    self.parameters["version"] = kwargs[key]
                elif key == "identity":
                    self.parameters.setdefault("identity", {})["type"] = _snake_to_camel(kwargs[key], True)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_sqlserver()

        if not old_response:
            self.log("SQL Server instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("SQL Server instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if SQL Server instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the SQL Server instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_sqlserver()
            response.pop('administrator_login_password', None)

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("SQL Server instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_sqlserver()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_sqlserver():
                time.sleep(20)
        else:
            self.log("SQL Server instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["version"] = response["version"]
            self.results["state"] = response["state"]
            self.results["fully_qualified_domain_name"] = response["fully_qualified_domain_name"]

        return self.results

    def create_update_sqlserver(self):
        '''
        Creates or updates SQL Server with the specified configuration.

        :return: deserialized SQL Server instance state dictionary
        '''
        self.log("Creating / Updating the SQL Server instance {0}".format(self.name))

        try:
            response = self.mgmt_client.servers.create_or_update(resource_group_name=self.resource_group,
                                                                 server_name=self.name,
                                                                 parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the SQL Server instance.')
            self.fail("Error creating the SQL Server instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_sqlserver(self):
        '''
        Deletes specified SQL Server instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the SQL Server instance {0}".format(self.name))
        try:
            response = self.mgmt_client.servers.delete(resource_group_name=self.resource_group,
                                                       server_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the SQL Server instance.')
            self.fail("Error deleting the SQL Server instance: {0}".format(str(e)))

        return True

    def get_sqlserver(self):
        '''
        Gets the properties of the specified SQL Server.

        :return: deserialized SQL Server instance state dictionary
        '''
        self.log("Checking if the SQL Server instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.servers.get(resource_group_name=self.resource_group,
                                                    server_name=self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SQL Server instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SQL Server instance.')
        if found is True:
            return response.as_dict()

        return False


def _snake_to_camel(snake, capitalize_first=False):
    if capitalize_first:
        return ''.join(x.capitalize() or '_' for x in snake.split('_'))
    else:
        return snake.split('_')[0] + ''.join(x.capitalize() or '_' for x in snake.split('_')[1:])


def main():
    """Main execution"""
    AzureRMServers()

if __name__ == '__main__':
    main()
