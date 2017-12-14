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
module: azure_rm_applicationgatewayloadbalancerbackendaddresspool_facts
version_added: "2.5"
short_description: Get LoadBalancerBackendAddressPools facts.
description:
    - Get facts of LoadBalancerBackendAddressPools.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    backend_address_pool_name:
        description:
            - The name of the backend address pool.
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of LoadBalancerBackendAddressPools
    azure_rm_applicationgatewayloadbalancerbackendaddresspool_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      backend_address_pool_name: backend_address_pool_name
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


class AzureRMLoadBalancerBackendAddressPoolsFacts(AzureRMModuleBase):
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
            ),
            backend_address_pool_name=dict(
                type='str',
                required=True
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.load_balancer_name = None
        self.backend_address_pool_name = None
        super(AzureRMLoadBalancerBackendAddressPoolsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.load_balancer_name is not None and
                self.backend_address_pool_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified LoadBalancerBackendAddressPools.

        :return: deserialized LoadBalancerBackendAddressPoolsinstance state dictionary
        '''
        self.log("Checking if the LoadBalancerBackendAddressPools instance {0} is present".format(self.backend_address_pool_name))
        found = False
        try:
            response = self.mgmt_client.load_balancer_backend_address_pools.get(self.resource_group,
                                                                                self.load_balancer_name,
                                                                                self.backend_address_pool_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("LoadBalancerBackendAddressPools instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the LoadBalancerBackendAddressPools instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMLoadBalancerBackendAddressPoolsFacts()
if __name__ == '__main__':
    main()