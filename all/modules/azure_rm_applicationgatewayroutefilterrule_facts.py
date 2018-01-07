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
short_description: Get Route Filter Rule facts.
description:
    - Get facts of Route Filter Rule.

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

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Route Filter Rule
    azure_rm_applicationgatewayroutefilterrule_facts:
      resource_group: resource_group_name
      route_filter_name: route_filter_name
      rule_name: rule_name

  - name: List instances of Route Filter Rule
    azure_rm_applicationgatewayroutefilterrule_facts:
      resource_group: resource_group_name
      route_filter_name: route_filter_name
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
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
        self.route_filter_name = None
        self.rule_name = None
        super(AzureRMRouteFilterRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.route_filter_name is not None and
                self.rule_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.route_filter_name is not None):
            self.results['ansible_facts']['list_by_route_filter'] = self.list_by_route_filter()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Route Filter Rule.

        :return: deserialized Route Filter Ruleinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.route_filter_rules.get(resource_group_name=self.resource_group,
                                                               route_filter_name=self.route_filter_name,
                                                               rule_name=self.rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RouteFilterRules.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_by_route_filter(self):
        '''
        Gets facts of the specified Route Filter Rule.

        :return: deserialized Route Filter Ruleinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.route_filter_rules.list_by_route_filter(resource_group_name=self.resource_group,
                                                                                route_filter_name=self.route_filter_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RouteFilterRules.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMRouteFilterRulesFacts()
if __name__ == '__main__':
    main()
