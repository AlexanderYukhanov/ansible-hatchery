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
module: azure_rm_sql_databaseblobauditingpolicies_facts
version_added: "2.5"
short_description: Get DatabaseBlobAuditingPolicies facts.
description:
    - Get facts of DatabaseBlobAuditingPolicies.

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
            - The name of the database for which the blob audit policy is defined.
        required: True
    blob_auditing_policy_name:
        description:
            - The name of the blob auditing policy.
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of DatabaseBlobAuditingPolicies
    azure_rm_sql_databaseblobauditingpolicies_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      blob_auditing_policy_name: blob_auditing_policy_name
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


class AzureRMDatabaseBlobAuditingPoliciesFacts(AzureRMModuleBase):
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
            blob_auditing_policy_name=dict(
                type='str',
                required=True
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.server_name = None
        self.database_name = None
        self.blob_auditing_policy_name = None
        super(AzureRMDatabaseBlobAuditingPoliciesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.blob_auditing_policy_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified DatabaseBlobAuditingPolicies.

        :return: deserialized DatabaseBlobAuditingPoliciesinstance state dictionary
        '''
        self.log("Checking if the DatabaseBlobAuditingPolicies instance {0} is present".format(self.blob_auditing_policy_name))
        found = False
        try:
            response = self.mgmt_client.database_blob_auditing_policies.get(self.resource_group,
                                                                            self.server_name,
                                                                            self.database_name,
                                                                            self.blob_auditing_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("DatabaseBlobAuditingPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DatabaseBlobAuditingPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMDatabaseBlobAuditingPoliciesFacts()
if __name__ == '__main__':
    main()