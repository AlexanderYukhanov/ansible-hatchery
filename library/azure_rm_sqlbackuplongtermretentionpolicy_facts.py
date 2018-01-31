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
module: azure_rm_sqlbackuplongtermretentionpolicy_facts
version_added: "2.5"
short_description: Get Backup Long Term Retention Policy facts.
description:
    - Get facts of Backup Long Term Retention Policy.

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
            - The name of the database.
        required: True
    backup_long_term_retention_policy_name:
        description:
            - The name of the backup long term retention policy

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Backup Long Term Retention Policy
    azure_rm_sqlbackuplongtermretentionpolicy_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      backup_long_term_retention_policy_name: backup_long_term_retention_policy_name

  - name: List instances of Backup Long Term Retention Policy
    azure_rm_sqlbackuplongtermretentionpolicy_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
'''

RETURN = '''
backup_long_term_retention_policies:
    description: A list of dict results where the key is the name of the Backup Long Term Retention Policy and the values are the facts for that Backup Long Term Retention Policy.
    returned: always
    type: complex
    contains:
        backuplongtermretentionpolicy_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/longtermretentiontest-1234/providers/Microsoft.Sql/servers/lo
                            ngtermretentiontest-5678/databases/longtermretentiontest-9012/backupLongTermRetentionPolicies/Default"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: Default
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Sql/servers/databases/backupLongTermRetentionPolicies
                location:
                    description:
                        - The geo-location where the resource lives
                    returned: always
                    type: str
                    sample: Japan East
                state:
                    description:
                        - "The status of the backup long term retention policy. Possible values include: 'Disabled', 'Enabled'"
                    returned: always
                    type: str
                    sample: Enabled
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


class AzureRMBackupLongTermRetentionPoliciesFacts(AzureRMModuleBase):
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
            database_name=dict(
                type='str',
                required=True
            ),
            backup_long_term_retention_policy_name=dict(
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
        self.database_name = None
        self.backup_long_term_retention_policy_name = None
        super(AzureRMBackupLongTermRetentionPoliciesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.backup_long_term_retention_policy_name is not None):
            self.results['backup_long_term_retention_policies'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['backup_long_term_retention_policies'] = self.list_by_database()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Backup Long Term Retention Policy.

        :return: deserialized Backup Long Term Retention Policyinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.backup_long_term_retention_policies.get(resource_group_name=self.resource_group,
                                                                                server_name=self.server_name,
                                                                                database_name=self.database_name,
                                                                                backup_long_term_retention_policy_name=self.backup_long_term_retention_policy_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BackupLongTermRetentionPolicies.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_database(self):
        '''
        Gets facts of the specified Backup Long Term Retention Policy.

        :return: deserialized Backup Long Term Retention Policyinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.backup_long_term_retention_policies.list_by_database(resource_group_name=self.resource_group,
                                                                                             server_name=self.server_name,
                                                                                             database_name=self.database_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BackupLongTermRetentionPolicies.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMBackupLongTermRetentionPoliciesFacts()
if __name__ == '__main__':
    main()
