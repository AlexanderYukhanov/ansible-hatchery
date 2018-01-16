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
module: azure_rm_applicationgatewayloadbalancernetworkinterface_facts
version_added: "2.5"
short_description: Get Load Balancer Network Interface facts.
description:
    - Get facts of Load Balancer Network Interface.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Load Balancer Network Interface
    azure_rm_applicationgatewayloadbalancernetworkinterface_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
'''

RETURN = '''
load_balancer_network_interfaces:
    description: A list of dict results where the key is the name of the Load Balancer Network Interface and the values are the facts for that Load Balancer Network Interface.
    returned: always
    type: complex
    contains:
        loadbalancernetworkinterface_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMLoadBalancerNetworkInterfacesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            load_balancer_name=dict(
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
        self.resource_group = None
        self.load_balancer_name = None
        super(AzureRMLoadBalancerNetworkInterfacesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None):
            self.results['load_balancer_network_interfaces'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Load Balancer Network Interface.

        :return: deserialized Load Balancer Network Interfaceinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.load_balancer_network_interfaces.list(resource_group_name=self.resource_group,
                                                                              load_balancer_name=self.load_balancer_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancerNetworkInterfaces.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMLoadBalancerNetworkInterfacesFacts()
if __name__ == '__main__':
    main()
