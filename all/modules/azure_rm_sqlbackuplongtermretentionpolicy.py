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
module: azure_rm_sqlbackuplongtermretentionpolicy
version_added: "2.5"
short_description: Manage BackupLongTermRetentionPolicies instance
description:
    - Create, update and delete instance of BackupLongTermRetentionPolicies

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
            - The name of the database
        required: True
    backup_long_term_retention_policy_name:
        description:
            - The name of the backup long term retention policy
        required: True
    state:
        description:
            - "The status of the backup long term retention policy. Possible values include: 'Disabled', 'Enabled'"
        required: True
    recovery_services_backup_policy_resource_id:
        description:
            - The azure recovery services backup protection policy resource id
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) BackupLongTermRetentionPolicies
    azure_rm_sqlbackuplongtermretentionpolicy:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      backup_long_term_retention_policy_name: backup_long_term_retention_policy_name
      state: state
      recovery_services_backup_policy_resource_id: recovery_services_backup_policy_resource_id
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
        - "The status of the backup long term retention policy. Possible values include: 'Disabled', 'Enabled'"
    returned: always
    type: str
    sample: state
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


class AzureRMBackupLongTermRetentionPolicies(AzureRMModuleBase):
    """Configuration class for an Azure RM BackupLongTermRetentionPolicies resource"""

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
            backup_long_term_retention_policy_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                required=True
            ),
            recovery_services_backup_policy_resource_id=dict(
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
        self.database_name = None
        self.backup_long_term_retention_policy_name = None
        self.state = None
        self.recovery_services_backup_policy_resource_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBackupLongTermRetentionPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                     supports_check_mode=True,
                                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self.key)

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_backuplongtermretentionpolicies()

        if not old_response:
            self.log("BackupLongTermRetentionPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("BackupLongTermRetentionPolicies instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if BackupLongTermRetentionPolicies instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the BackupLongTermRetentionPolicies instance")

            if self.check_mode:
                return self.results

            response = self.create_update_backuplongtermretentionpolicies()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)

            self.results.update(response)

            # remove unnecessary fields from return state
            self.results.pop('name', None)
            self.results.pop('type', None)
            self.results.pop('location', None)
            self.results.pop('recovery_services_backup_policy_resource_id', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("BackupLongTermRetentionPolicies instance deleted")
            self.delete_backuplongtermretentionpolicies()
            self.results['changed'] = True
        else:
            self.log("BackupLongTermRetentionPolicies instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_backuplongtermretentionpolicies(self):
        '''
        Creates or updates BackupLongTermRetentionPolicies with the specified configuration.

        :return: deserialized BackupLongTermRetentionPolicies instance state dictionary
        '''
        self.log("Creating / Updating the BackupLongTermRetentionPolicies instance {0}".format(self.backup_long_term_retention_policy_name))

        try:
            response = self.mgmt_client.backup_long_term_retention_policies.create_or_update(self.resource_group,
                                                                                             self.server_name,
                                                                                             self.database_name,
                                                                                             self.backup_long_term_retention_policy_name,
                                                                                             self.state,
                                                                                             self.recovery_services_backup_policy_resource_id)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the BackupLongTermRetentionPolicies instance.')
            self.fail("Error creating the BackupLongTermRetentionPolicies instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_backuplongtermretentionpolicies(self):
        '''
        Deletes specified BackupLongTermRetentionPolicies instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the BackupLongTermRetentionPolicies instance {0}".format(self.backup_long_term_retention_policy_name))
        try:
            response = self.mgmt_client.backup_long_term_retention_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the BackupLongTermRetentionPolicies instance.')
            self.fail("Error deleting the BackupLongTermRetentionPolicies instance: {0}".format(str(e)))

        return True

    def get_backuplongtermretentionpolicies(self):
        '''
        Gets the properties of the specified BackupLongTermRetentionPolicies.

        :return: deserialized BackupLongTermRetentionPolicies instance state dictionary
        '''
        self.log("Checking if the BackupLongTermRetentionPolicies instance {0} is present".format(self.backup_long_term_retention_policy_name))
        found = False
        try:
            response = self.mgmt_client.backup_long_term_retention_policies.get(self.resource_group,
                                                                                self.server_name,
                                                                                self.database_name,
                                                                                self.backup_long_term_retention_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("BackupLongTermRetentionPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the BackupLongTermRetentionPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMBackupLongTermRetentionPolicies()

if __name__ == '__main__':
    main()
