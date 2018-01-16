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
module: azure_rm_webrecommendation_facts
version_added: "2.5"
short_description: Get Recommendation facts.
description:
    - Get facts of Recommendation.

options:
    featured:
        description:
            - Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
    filter:
        description:
            - "Filter is specified by using OData syntax. Example: $filter=channels eq C(Api) or channel eq C(Notification) and startTime eq C(2014-01-01T00:
              00:00Z) and endTime eq C(2014-12-31T23:59:59Z) and timeGrain eq duration'[PT1H|PT1M|P1D]"

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Recommendation
    azure_rm_webrecommendation_facts:
      featured: featured
      filter: filter
'''

RETURN = '''
recommendations:
    description: A list of dict results where the key is the name of the Recommendation and the values are the facts for that Recommendation.
    returned: always
    type: complex
    contains:
        recommendation_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.web import WebSiteManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecommendationsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            featured=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.featured = None
        self.filter = None
        super(AzureRMRecommendationsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results['recommendations'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Recommendation.

        :return: deserialized Recommendationinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.recommendations.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Recommendations.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMRecommendationsFacts()
if __name__ == '__main__':
    main()
