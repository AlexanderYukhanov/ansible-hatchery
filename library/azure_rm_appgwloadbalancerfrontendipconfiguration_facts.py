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
module: azure_rm_appgwloadbalancerfrontendipconfiguration_facts
version_added: "2.5"
short_description: Get Load Balancer Frontend I P Configuration facts.
description:
    - Get facts of Load Balancer Frontend I P Configuration.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    frontend_ip_configuration_name:
        description:
            - The name of the frontend IP configuration.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Load Balancer Frontend I P Configuration
    azure_rm_appgwloadbalancerfrontendipconfiguration_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      frontend_ip_configuration_name: frontend_ip_configuration_name
'''

RETURN = '''
load_balancer_frontend_ip_configurations:
    description: A list of dict results where the key is the name of the Load Balancer Frontend I P Configuration and the values are the facts for that Load Balancer Frontend I P Configuration.
    returned: always
    type: complex
    contains:
        loadbalancerfrontendipconfiguration_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/frontend
                subnet:
                    description:
                        - The reference of the subnet resource.
                    returned: always
                    type: complex
                    sample: subnet
                    contains:
                        id:
                            description:
                                - Resource ID.
                            returned: always
                            type: str
                            sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/vnetlb/subnets/subnetlb
                name:
                    description:
                        - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: frontend
                etag:
                    description:
                        - A unique read-only string that changes whenever the resource is updated.
                    returned: always
                    type: str
                    sample: "W/\'00000000-0000-0000-0000-000000000000\'"
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


class AzureRMLoadBalancerFrontendIPConfigurationsFacts(AzureRMModuleBase):
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
            frontend_ip_configuration_name=dict(
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
        self.frontend_ip_configuration_name = None
        super(AzureRMLoadBalancerFrontendIPConfigurationsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None and
                self.frontend_ip_configuration_name is not None):
            self.results['load_balancer_frontend_ip_configurations'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Load Balancer Frontend I P Configuration.

        :return: deserialized Load Balancer Frontend I P Configurationinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.load_balancer_frontend_ip_configurations.get(resource_group_name=self.resource_group,
                                                                                     load_balancer_name=self.load_balancer_name,
                                                                                     frontend_ip_configuration_name=self.frontend_ip_configuration_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancerFrontendIPConfigurations.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMLoadBalancerFrontendIPConfigurationsFacts()
if __name__ == '__main__':
    main()
