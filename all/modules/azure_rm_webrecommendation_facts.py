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
short_description: Get Recommendations facts.
description:
    - Get facts of Recommendations.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    site_name:
        description:
            - Name of the app.
        required: True
    featured:
        description:
            - Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
    filter:
        description:
            - "Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Not
               ification'"

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Recommendations
    azure_rm_webrecommendation_facts:
      resource_group: resource_group_name
      site_name: site_name
      featured: featured
      filter: filter

  - name: List instances of Recommendations
    azure_rm_webrecommendation_facts:
      resource_group: resource_group_name
      site_name: site_name
      filter: filter
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
            resource_group=dict(
                type='str',
                required=True
            ),
            site_name=dict(
                type='str',
                required=True
            ),
            featured=dict(
                type='str',
                required=False
            ),
            filter=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.site_name = None
        self.featured = None
        self.filter = None
        super(AzureRMRecommendationsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.site_name is not None):
            self.results['ansible_facts']['list_recommended_rules_for_web_app'] = self.list_recommended_rules_for_web_app()
        elif (self.resource_group_name is not None and
              self.site_name is not None):
            self.results['ansible_facts']['list_history_for_web_app'] = self.list_history_for_web_app()
        return self.results

    def list_recommended_rules_for_web_app(self):
        '''
        Gets facts of the specified Recommendations.

        :return: deserialized Recommendationsinstance state dictionary
        '''
        self.log("Checking if the Recommendations instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.recommendations.list_recommended_rules_for_web_app(self.resource_group,
                                                                                           self.site_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Recommendations instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Recommendations instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_history_for_web_app(self):
        '''
        Gets facts of the specified Recommendations.

        :return: deserialized Recommendationsinstance state dictionary
        '''
        self.log("Checking if the Recommendations instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.recommendations.list_history_for_web_app(self.resource_group,
                                                                                 self.site_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Recommendations instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Recommendations instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMRecommendationsFacts()
if __name__ == '__main__':
    main()
