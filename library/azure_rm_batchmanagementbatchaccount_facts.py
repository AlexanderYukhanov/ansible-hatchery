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
module: azure_rm_batchmanagementbatchaccount_facts
version_added: "2.5"
short_description: Get Batch Account facts.
description:
    - Get facts of Batch Account.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Batch Account
    azure_rm_batchmanagementbatchaccount_facts:
      resource_group: resource_group_name
      account_name: account_name

  - name: List instances of Batch Account
    azure_rm_batchmanagementbatchaccount_facts:
      resource_group: resource_group_name
'''

RETURN = '''
batch_account:
    description: A list of dict results where the key is the name of the Batch Account and the values are the facts for that Batch Account.
    returned: always
    type: complex
    contains:
        batchaccount_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - The ID of the resource.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.Batch/batchAccounts/sampleacct
                name:
                    description:
                        - The name of the resource.
                    returned: always
                    type: str
                    sample: sampleacct
                type:
                    description:
                        - The type of the resource.
                    returned: always
                    type: str
                    sample: Microsoft.Batch/batchAccounts
                location:
                    description:
                        - The location of the resource.
                    returned: always
                    type: str
                    sample: japaneast
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batch import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBatchAccountFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            account_name=dict(
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
        self.account_name = None
        super(AzureRMBatchAccountFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.account_name is not None):
            self.results['batch_account'] = self.get()
        elif (self.resource_group is not None):
            self.results['batch_account'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Batch Account.

        :return: deserialized Batch Accountinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.batch_account.get(resource_group_name=self.resource_group,
                                                          account_name=self.account_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BatchAccount.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Batch Account.

        :return: deserialized Batch Accountinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.batch_account.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BatchAccount.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMBatchAccountFacts()
if __name__ == '__main__':
    main()
