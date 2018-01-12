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
module: azure_rm_sqlbackuplongtermretentionvault_facts
version_added: "2.5"
short_description: Get Backup Long Term Retention Vault facts.
description:
    - Get facts of Backup Long Term Retention Vault.

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
            - The name of the Azure SQL Server backup LongTermRetention vault

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Backup Long Term Retention Vault
    azure_rm_sqlbackuplongtermretentionvault_facts:
      resource_group: resource_group_name
      server_name: server_name
      backup_long_term_retention_vault_name: backup_long_term_retention_vault_name

  - name: List instances of Backup Long Term Retention Vault
    azure_rm_sqlbackuplongtermretentionvault_facts:
      resource_group: resource_group_name
      server_name: server_name
'''

RETURN = '''
backup_long_term_retention_vaults:
    description: A list of dict results where the key is the name of the Backup Long Term Retention Vault and the values are the facts for that Backup Long Term Retention Vault.
    returned: always
    type: complex
    contains:
        backuplongtermretentionvault_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/longtermretentiontest-1234/providers/Microsoft.Sql/servers/lo
                            ngtermretentiontest-5678/backupLongTermRetentionVaults/RegisteredVault"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: RegisteredVault
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Sql/servers/backupLongTermRetentionVaults
                location:
                    description:
                        - The geo-location where the resource lives
                    returned: always
                    type: str
                    sample: Japan East
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


class AzureRMBackupLongTermRetentionVaultsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
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
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.server_name = None
        self.backup_long_term_retention_vault_name = None
        super(AzureRMBackupLongTermRetentionVaultsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.backup_long_term_retention_vault_name is not None):
            self.results['backup_long_term_retention_vaults'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None):
            self.results['backup_long_term_retention_vaults'] = self.list_by_server()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Backup Long Term Retention Vault.

        :return: deserialized Backup Long Term Retention Vaultinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.backup_long_term_retention_vaults.get(resource_group_name=self.resource_group,
                                                                              server_name=self.server_name,
                                                                              backup_long_term_retention_vault_name=self.backup_long_term_retention_vault_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BackupLongTermRetentionVaults.')

        if response is not None:
            results = {}
            results[response.name] = response.as_dict()

        return results

    def list_by_server(self):
        '''
        Gets facts of the specified Backup Long Term Retention Vault.

        :return: deserialized Backup Long Term Retention Vaultinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.backup_long_term_retention_vaults.list_by_server(resource_group_name=self.resource_group,
                                                                                         server_name=self.server_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BackupLongTermRetentionVaults.')

        if response is not None:
            results = {}
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMBackupLongTermRetentionVaultsFacts()
if __name__ == '__main__':
    main()
