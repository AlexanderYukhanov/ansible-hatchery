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
module: azure_rm_batchmanagementpool_facts
version_added: "2.5"
short_description: Get Pool facts.
description:
    - Get facts of Pool.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.
        required: True
    maxresults:
        description:
            - The maximum number of items to return in the response.
    select:
        description:
            - "Comma separated list of properties that should be returned. e.g. 'properties/provisioningState'. Only top level properties under properties/
               are valid for selection."
    filter:
        description:
            - "OData filter expression. Valid properties for filtering are:"
            -  name
            -  properties/allocationState
            -  properties/allocationStateTransitionTime
            -  properties/creationTime
            -  properties/provisioningState
            -  properties/provisioningStateTransitionTime
            -  properties/lastModified
            -  properties/vmSize
            -  properties/interNodeCommunication
            -  properties/scaleSettings/autoScale
            -  properties/scaleSettings/fixedScale
    pool_name:
        description:
            - The pool name. This must be unique within the account.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Pool
    azure_rm_batchmanagementpool_facts:
      resource_group: resource_group_name
      account_name: account_name
      maxresults: maxresults
      select: select
      filter: filter

  - name: Get instance of Pool
    azure_rm_batchmanagementpool_facts:
      resource_group: resource_group_name
      account_name: account_name
      pool_name: pool_name
'''

RETURN = '''
pool:
    description: A list of dict results where the key is the name of the Pool and the values are the facts for that Pool.
    returned: always
    type: complex
    contains:
        pool_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - The ID of the resource.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.Batch/batchAccounts/sampleacct/pools/testpool
                name:
                    description:
                        - The name of the resource.
                    returned: always
                    type: str
                    sample: testpool
                type:
                    description:
                        - The type of the resource.
                    returned: always
                    type: str
                    sample: Microsoft.Batch/batchAccounts/pools
                etag:
                    description:
                        - The ETag of the resource, used for concurrency statements.
                    returned: always
                    type: str
                    sample: "W/'0x8D4EDFEBFADF4AB'"
                metadata:
                    description:
                        - The Batch service does not assign any meaning to metadata; it is solely for the use of user code.
                    returned: always
                    type: complex
                    sample: metadata
                    contains:
                certificates:
                    description:
                        - "For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux
                           compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable
                           AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of 'remoteUser',
                           a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and certificates are placed in that
                           directory."
                    returned: always
                    type: complex
                    sample: certificates
                    contains:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batchmanagement import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPoolFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            maxresults=dict(
                type='int'
            ),
            select=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            pool_name=dict(
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
        self.maxresults = None
        self.select = None
        self.filter = None
        self.pool_name = None
        super(AzureRMPoolFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.account_name is not None):
            self.results['pool'] = self.list_by_batch_account()
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.pool_name is not None):
            self.results['pool'] = self.get()
        return self.results

    def list_by_batch_account(self):
        '''
        Gets facts of the specified Pool.

        :return: deserialized Poolinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.pool.list_by_batch_account(resource_group_name=self.resource_group,
                                                                   account_name=self.account_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Pool.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def get(self):
        '''
        Gets facts of the specified Pool.

        :return: deserialized Poolinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.pool.get(resource_group_name=self.resource_group,
                                                 account_name=self.account_name,
                                                 pool_name=self.pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Pool.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMPoolFacts()
if __name__ == '__main__':
    main()
