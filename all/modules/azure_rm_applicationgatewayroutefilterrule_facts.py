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
module: azure_rm_applicationgatewayroutefilterrule_facts
version_added: "2.5"
short_description: Get RouteFilterRules facts.
description:
    - Get facts of RouteFilterRules.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    route_filter_name:
        description:
            - The name of the route filter.
        required: True
    rule_name:
        description:
            - The name of the rule.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of RouteFilterRules
    azure_rm_applicationgatewayroutefilterrule_facts:
      resource_group: resource_group_name
      route_filter_name: route_filter_name
      rule_name: rule_name

  - name: List instances of RouteFilterRules
    azure_rm_applicationgatewayroutefilterrule_facts:
      resource_group: resource_group_name
      route_filter_name: route_filter_name
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRouteFilterRulesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            route_filter_name=dict(
                type='str',
                required=True
            ),
            rule_name=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.resource_group = None
        self.route_filter_name = None
        self.rule_name = None
        super(AzureRMRouteFilterRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.route_filter_name is not None and
                self.rule_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.route_filter_name is not None):
            self.results['ansible_facts']['list_by_route_filter'] = self.list_by_route_filter()
        return self.results

    def get(self):
        '''
        Gets facts of the specified RouteFilterRules.

        :return: deserialized RouteFilterRulesinstance state dictionary
        '''
        self.log("Checking if the RouteFilterRules instance {0} is present".format(self.rule_name))
        found = False
        try:
            response = self.mgmt_client.route_filter_rules.get(self.resource_group,
                                                               self.route_filter_name,
                                                               self.rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RouteFilterRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RouteFilterRules instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_route_filter(self):
        '''
        Gets facts of the specified RouteFilterRules.

        :return: deserialized RouteFilterRulesinstance state dictionary
        '''
        self.log("Checking if the RouteFilterRules instance {0} is present".format(self.rule_name))
        found = False
        try:
            response = self.mgmt_client.route_filter_rules.list_by_route_filter(self.resource_group,
                                                                                self.route_filter_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RouteFilterRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RouteFilterRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMRouteFilterRulesFacts()
if __name__ == '__main__':
    main()
