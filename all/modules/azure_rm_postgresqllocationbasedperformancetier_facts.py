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
module: azure_rm_postgresqllocationbasedperformancetier_facts
version_added: "2.5"
short_description: Get Location Based Performance Tier facts.
description:
    - Get facts of Location Based Performance Tier.

options:
    location_name:
        description:
            - The name of the location.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Location Based Performance Tier
    azure_rm_postgresqllocationbasedperformancetier_facts:
      location_name: location_name
'''

RETURN = '''
location_based_performance_tier:
    description: A list of dict results where the key is the name of the Location Based Performance Tier and the values are the facts for that Location Based Performance Tier.
    returned: always
    type: complex
    contains:
        locationbasedperformancetier_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLocationBasedPerformanceTierFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            location_name=dict(
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
        self.location_name = None
        super(AzureRMLocationBasedPerformanceTierFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.location_name is not None):
            self.results['location_based_performance_tier'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Location Based Performance Tier.

        :return: deserialized Location Based Performance Tierinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.location_based_performance_tier.list(location_name=self.location_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LocationBasedPerformanceTier.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMLocationBasedPerformanceTierFacts()
if __name__ == '__main__':
    main()
