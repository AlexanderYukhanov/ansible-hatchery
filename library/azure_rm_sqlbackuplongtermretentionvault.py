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
module: azure_rm_sqlbackuplongtermretentionvault
version_added: "2.5"
short_description: Manage Backup Long Term Retention Vault instance.
description:
    - Create, update and delete instance of Backup Long Term Retention Vault.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    backup_long_term_retention_vault_name:
        description:
            - The name of the backup long term retention vault
        required: True
    recovery_services_vault_resource_id:
        description:
            - The azure recovery services vault resource id
        required: True
    state:
      description:
        - Assert the state of the Backup Long Term Retention Vault.
        - Use 'present' to create or update an Backup Long Term Retention Vault and 'absent' to delete it.
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
  - name: Create (or update) Backup Long Term Retention Vault
    azure_rm_sqlbackuplongtermretentionvault:
      resource_group: longtermretentiontest-1234
      server_name: longtermretentiontest-5678
      backup_long_term_retention_vault_name: RegisteredVault
      recovery_services_vault_resource_id: NOT FOUND
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/longtermretentiontest-1234/providers/Microsoft.Sql/servers/longtermretentiont
            est-5678/backupLongTermRetentionVaults/RegisteredVault"
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


class AzureRMBackupLongTermRetentionVaults(AzureRMModuleBase):
    """Configuration class for an Azure RM Backup Long Term Retention Vault resource"""

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
            backup_long_term_retention_vault_name=dict(
                type='str',
                required=True
            ),
            recovery_services_vault_resource_id=dict(
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
        self.backup_long_term_retention_vault_name = None
        self.recovery_services_vault_resource_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBackupLongTermRetentionVaults, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        old_response = self.get_backuplongtermretentionvault()

        if not old_response:
            self.log("Backup Long Term Retention Vault instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Backup Long Term Retention Vault instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Backup Long Term Retention Vault instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Backup Long Term Retention Vault instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_backuplongtermretentionvault()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Backup Long Term Retention Vault instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_backuplongtermretentionvault()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_backuplongtermretentionvault():
                time.sleep(20)
        else:
            self.log("Backup Long Term Retention Vault instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_backuplongtermretentionvault(self):
        '''
        Creates or updates Backup Long Term Retention Vault with the specified configuration.

        :return: deserialized Backup Long Term Retention Vault instance state dictionary
        '''
        self.log("Creating / Updating the Backup Long Term Retention Vault instance {0}".format(self.backup_long_term_retention_vault_name))

        try:
            response = self.mgmt_client.backup_long_term_retention_vaults.create_or_update(resource_group_name=self.resource_group,
                                                                                           server_name=self.server_name,
                                                                                           backup_long_term_retention_vault_name=self.backup_long_term_retention_vault_name,
                                                                                           recovery_services_vault_resource_id=self.recovery_services_vault_resource_id)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Backup Long Term Retention Vault instance.')
            self.fail("Error creating the Backup Long Term Retention Vault instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_backuplongtermretentionvault(self):
        '''
        Deletes specified Backup Long Term Retention Vault instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Backup Long Term Retention Vault instance {0}".format(self.backup_long_term_retention_vault_name))
        try:
            response = self.mgmt_client.backup_long_term_retention_vaults.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Backup Long Term Retention Vault instance.')
            self.fail("Error deleting the Backup Long Term Retention Vault instance: {0}".format(str(e)))

        return True

    def get_backuplongtermretentionvault(self):
        '''
        Gets the properties of the specified Backup Long Term Retention Vault.

        :return: deserialized Backup Long Term Retention Vault instance state dictionary
        '''
        self.log("Checking if the Backup Long Term Retention Vault instance {0} is present".format(self.backup_long_term_retention_vault_name))
        found = False
        try:
            response = self.mgmt_client.backup_long_term_retention_vaults.get(resource_group_name=self.resource_group,
                                                                              server_name=self.server_name,
                                                                              backup_long_term_retention_vault_name=self.backup_long_term_retention_vault_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Backup Long Term Retention Vault instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Backup Long Term Retention Vault instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMBackupLongTermRetentionVaults()

if __name__ == '__main__':
    main()
