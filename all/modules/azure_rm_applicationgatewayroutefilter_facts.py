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
module: azure_rm_applicationgatewayroutefilter_facts
version_added: "2.5"
short_description: Get Route Filter facts.
description:
    - Get facts of Route Filter.

options:
    resource_group:
        description:
            - The name of the resource group.
    route_filter_name:
        description:
            - The name of the route filter.
    expand:
        description:
            - Expands referenced express route bgp peering resources.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Route Filter
    azure_rm_applicationgatewayroutefilter_facts:
      resource_group: resource_group_name
      route_filter_name: route_filter_name
      expand: expand

  - name: List instances of Route Filter
    azure_rm_applicationgatewayroutefilter_facts:
      resource_group: resource_group_name

  - name: List instances of Route Filter
    azure_rm_applicationgatewayroutefilter_facts:
'''

RETURN = '''
route_filters:
    description: A list of dict results where the key is the name of the Route Filter and the values are the facts for that Route Filter.
    returned: always
    type: complex
    contains:
        routefilter_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsofot.Network/routeFilters/filterName
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: filterName
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsofot.Network/routeFilters
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: West US
                rules:
                    description:
                        - Collection of RouteFilterRules contained within a route filter.
                    returned: always
                    type: complex
                    sample: rules
                    contains:
                peerings:
                    description:
                        - A collection of references to express route circuit peerings.
                    returned: always
                    type: complex
                    sample: peerings
                    contains:
                etag:
                    description:
                        - Gets a unique read-only string that changes whenever the resource is updated.
                    returned: always
                    type: str
                    sample: w/\00000000-0000-0000-0000-000000000000\
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


class AzureRMRouteFiltersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            route_filter_name=dict(
                type='str'
            ),
            expand=dict(
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
        self.expand = None
        super(AzureRMRouteFiltersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.route_filter_name is not None):
            self.results['route_filters'] = self.get()
        elif (self.resource_group is not None):
            self.results['route_filters'] = self.list_by_resource_group()
            self.results['route_filters'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Route Filter.

        :return: deserialized Route Filterinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.route_filters.get(resource_group_name=self.resource_group,
                                                          route_filter_name=self.route_filter_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RouteFilters.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Route Filter.

        :return: deserialized Route Filterinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.route_filters.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RouteFilters.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Route Filter.

        :return: deserialized Route Filterinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.route_filters.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RouteFilters.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMRouteFiltersFacts()
if __name__ == '__main__':
    main()
