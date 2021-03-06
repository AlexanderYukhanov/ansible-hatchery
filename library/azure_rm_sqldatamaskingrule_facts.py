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
module: azure_rm_sqldatamaskingrule_facts
version_added: "2.5"
short_description: Get Data Masking Rule facts.
description:
    - Get facts of Data Masking Rule.

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
    data_masking_policy_name:
        description:
            - The name of the database for which the data masking rule applies.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Data Masking Rule
    azure_rm_sqldatamaskingrule_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      data_masking_policy_name: data_masking_policy_name
'''

RETURN = '''
data_masking_rules:
    description: A list of dict results where the key is the name of the Data Masking Rule and the values are the facts for that Data Masking Rule.
    returned: always
    type: complex
    contains:
        datamaskingrule_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMDataMaskingRulesFacts(AzureRMModuleBase):
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
            data_masking_policy_name=dict(
                type='str',
                required=True
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
        self.data_masking_policy_name = None
        super(AzureRMDataMaskingRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.data_masking_policy_name is not None):
            self.results['data_masking_rules'] = self.list_by_database()
        return self.results

    def list_by_database(self):
        '''
        Gets facts of the specified Data Masking Rule.

        :return: deserialized Data Masking Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.data_masking_rules.list_by_database(resource_group_name=self.resource_group,
                                                                            server_name=self.server_name,
                                                                            database_name=self.database_name,
                                                                            data_masking_policy_name=self.data_masking_policy_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for DataMaskingRules.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMDataMaskingRulesFacts()
if __name__ == '__main__':
    main()
