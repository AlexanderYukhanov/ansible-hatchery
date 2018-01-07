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
module: azure_rm_sqlsubscriptionusage_facts
version_added: "2.5"
short_description: Get Subscription Usage facts.
description:
    - Get facts of Subscription Usage.

options:
    location_name:
        description:
            - The name of the region where the resource is located.
        required: True
    usage_name:
        description:
            - Name of usage metric to return.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Subscription Usage
    azure_rm_sqlsubscriptionusage_facts:
      location_name: location_name
      usage_name: usage_name

  - name: List instances of Subscription Usage
    azure_rm_sqlsubscriptionusage_facts:
      location_name: location_name
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


class AzureRMSubscriptionUsagesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            usage_name=dict(
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.location_name = None
        self.usage_name = None
        super(AzureRMSubscriptionUsagesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.location_name is not None and
                self.usage_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.location_name is not None):
            self.results['ansible_facts']['list_by_location'] = self.list_by_location()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Subscription Usage.

        :return: deserialized Subscription Usageinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.subscription_usages.get(location_name=self.location_name,
                                                                usage_name=self.usage_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SubscriptionUsages.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_by_location(self):
        '''
        Gets facts of the specified Subscription Usage.

        :return: deserialized Subscription Usageinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.subscription_usages.list_by_location(location_name=self.location_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SubscriptionUsages.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMSubscriptionUsagesFacts()
if __name__ == '__main__':
    main()
