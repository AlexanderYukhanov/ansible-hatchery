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
module: azure_rm_applicationgatewayloadbalancer_facts
version_added: "2.5"
short_description: Get LoadBalancers facts.
description:
    - Get facts of LoadBalancers.

options:
    resource_group:
        description:
            - The name of the resource group.
    load_balancer_name:
        description:
            - The name of the load balancer.
    expand:
        description:
            - Expands referenced resources.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of LoadBalancers
    azure_rm_applicationgatewayloadbalancer_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      expand: expand

  - name: List instances of LoadBalancers
    azure_rm_applicationgatewayloadbalancer_facts:
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


class AzureRMLoadBalancersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            load_balancer_name=dict(
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
        self.load_balancer_name = None
        self.expand = None
        super(AzureRMLoadBalancersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None):
            self.results['ansible_facts']['get'] = self.get()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def get(self):
        '''
        Gets facts of the specified LoadBalancers.

        :return: deserialized LoadBalancersinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.load_balancers.get(resource_group_name=self.resource_group,
                                                           load_balancer_name=self.load_balancer_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancers.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_all(self):
        '''
        Gets facts of the specified LoadBalancers.

        :return: deserialized LoadBalancersinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.load_balancers.list_all()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancers.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMLoadBalancersFacts()
if __name__ == '__main__':
    main()
