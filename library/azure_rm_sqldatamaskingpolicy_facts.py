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
module: azure_rm_sqldatamaskingpolicy_facts
version_added: "2.5"
short_description: Get Data Masking Policy facts.
description:
    - Get facts of Data Masking Policy.

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
  - name: Get instance of Data Masking Policy
    azure_rm_sqldatamaskingpolicy_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      data_masking_policy_name: data_masking_policy_name
'''

RETURN = '''
data_masking_policies:
    description: A list of dict results where the key is the name of the Data Masking Policy and the values are the facts for that Data Masking Policy.
    returned: always
    type: complex
    contains:
        datamaskingpolicy_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/sqlcrudtest-6852/providers/Microsoft.Sql/servers/sqlcrudtest-
                            2080/databases/sqlcrudtest-331/dataMaskingPolicies/Default"
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
                    sample: Microsoft.Sql/servers/databases/dataMaskingPolicies
                location:
                    description:
                        - The location of the data masking policy.
                    returned: always
                    type: str
                    sample: Central US
                kind:
                    description:
                        - The kind of data masking policy. Metadata, used for Azure portal.
                    returned: always
                    type: str
                    sample: kind
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


class AzureRMDataMaskingPoliciesFacts(AzureRMModuleBase):
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
        super(AzureRMDataMaskingPoliciesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.data_masking_policy_name is not None):
            self.results['data_masking_policies'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Data Masking Policy.

        :return: deserialized Data Masking Policyinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.data_masking_policies.get(resource_group_name=self.resource_group,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  data_masking_policy_name=self.data_masking_policy_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for DataMaskingPolicies.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMDataMaskingPoliciesFacts()
if __name__ == '__main__':
    main()
