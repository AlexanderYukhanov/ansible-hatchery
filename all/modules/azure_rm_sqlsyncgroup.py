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
module: azure_rm_sqlsyncgroup
version_added: "2.5"
short_description: Manage SyncGroups instance
description:
    - Create, update and delete instance of SyncGroups

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    database_name:
        description:
            - The name of the database on which the sync group is hosted.
        required: True
    sync_group_name:
        description:
            - The name of the sync group.
        required: True
    interval:
        description:
            - Sync interval of the sync group.
    conflict_resolution_policy:
        description:
            - "Conflict resolution policy of the sync group. Possible values include: 'HubWin', 'MemberWin'"
    sync_database_id:
        description:
            - ARM resource id of the sync database in the sync group.
    hub_database_user_name:
        description:
            - User name for the sync group hub database credential.
    hub_database_password:
        description:
            - Password for the sync group hub database credential.
    schema:
        description:
            - Sync schema of the sync group.
        suboptions:
            tables:
                description:
                    - List of tables in sync group schema.
                suboptions:
                    columns:
                        description:
                            - List of columns in sync group schema.
                        suboptions:
                            quoted_name:
                                description:
                                    - Quoted name of sync group table column.
                            data_size:
                                description:
                                    - Data size of the column.
                            data_type:
                                description:
                                    - Data type of the column.
                    quoted_name:
                        description:
                            - Quoted name of sync group schema table.
            master_sync_member_name:
                description:
                    - Name of master sync member where the schema is from.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) SyncGroups
    azure_rm_sqlsyncgroup:
      resource_group: syncgroupcrud-65440
      server_name: syncgroupcrud-8475
      database_name: syncgroupcrud-4328
      sync_group_name: syncgroupcrud-3187
      schema:
        tables:
          - columns:
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
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


class AzureRMSyncGroups(AzureRMModuleBase):
    """Configuration class for an Azure RM SyncGroups resource"""

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
            database_name=dict(
                type='str',
                required=True
            ),
            sync_group_name=dict(
                type='str',
                required=True
            ),
            interval=dict(
                type='int',
                required=False
            ),
            conflict_resolution_policy=dict(
                type='str',
                required=False
            ),
            sync_database_id=dict(
                type='str',
                required=False
            ),
            hub_database_user_name=dict(
                type='str',
                required=False
            ),
            hub_database_password=dict(
                type='str',
                no_log=True,
                required=False
            ),
            schema=dict(
                type='dict',
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
        self.database_name = None
        self.sync_group_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSyncGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                supports_check_mode=True,
                                                supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "interval":
                    self.parameters["interval"] = kwargs[key]
                elif key == "conflict_resolution_policy":
                    self.parameters["conflict_resolution_policy"] = kwargs[key]
                elif key == "sync_database_id":
                    self.parameters["sync_database_id"] = kwargs[key]
                elif key == "hub_database_user_name":
                    self.parameters["hub_database_user_name"] = kwargs[key]
                elif key == "hub_database_password":
                    self.parameters["hub_database_password"] = kwargs[key]
                elif key == "schema":
                    self.parameters["schema"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_syncgroups()

        if not old_response:
            self.log("SyncGroups instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("SyncGroups instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if SyncGroups instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the SyncGroups instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_syncgroups()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("SyncGroups instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_syncgroups()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_syncgroups():
                time.sleep(20)
        else:
            self.log("SyncGroups instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_syncgroups(self):
        '''
        Creates or updates SyncGroups with the specified configuration.

        :return: deserialized SyncGroups instance state dictionary
        '''
        self.log("Creating / Updating the SyncGroups instance {0}".format(self.sync_group_name))

        try:
            response = self.mgmt_client.sync_groups.create_or_update(self.resource_group,
                                                                     self.server_name,
                                                                     self.database_name,
                                                                     self.sync_group_name,
                                                                     self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the SyncGroups instance.')
            self.fail("Error creating the SyncGroups instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_syncgroups(self):
        '''
        Deletes specified SyncGroups instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the SyncGroups instance {0}".format(self.sync_group_name))
        try:
            response = self.mgmt_client.sync_groups.delete(self.resource_group,
                                                           self.server_name,
                                                           self.database_name,
                                                           self.sync_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the SyncGroups instance.')
            self.fail("Error deleting the SyncGroups instance: {0}".format(str(e)))

        return True

    def get_syncgroups(self):
        '''
        Gets the properties of the specified SyncGroups.

        :return: deserialized SyncGroups instance state dictionary
        '''
        self.log("Checking if the SyncGroups instance {0} is present".format(self.sync_group_name))
        found = False
        try:
            response = self.mgmt_client.sync_groups.get(self.resource_group,
                                                        self.server_name,
                                                        self.database_name,
                                                        self.sync_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SyncGroups instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SyncGroups instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMSyncGroups()

if __name__ == '__main__':
    main()
