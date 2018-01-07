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
module: azure_rm_applicationgatewayexpressroutecircuit_facts
version_added: "2.5"
short_description: Get Express Route Circuit facts.
description:
    - Get facts of Express Route Circuit.

options:
    resource_group:
        description:
            - The name of the resource group.
    circuit_name:
        description:
            - The name of the express route circuit.
    peering_name:
        description:
            - The name of the peering.
    device_path:
        description:
            - The path of the device.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Express Route Circuit
    azure_rm_applicationgatewayexpressroutecircuit_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      peering_name: peering_name
      device_path: device_path

  - name: List instances of Express Route Circuit
    azure_rm_applicationgatewayexpressroutecircuit_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      peering_name: peering_name
      device_path: device_path

  - name: List instances of Express Route Circuit
    azure_rm_applicationgatewayexpressroutecircuit_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      peering_name: peering_name
      device_path: device_path

  - name: Get instance of Express Route Circuit
    azure_rm_applicationgatewayexpressroutecircuit_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name

  - name: List instances of Express Route Circuit
    azure_rm_applicationgatewayexpressroutecircuit_facts:
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


class AzureRMExpressRouteCircuitsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            circuit_name=dict(
                type='str'
            ),
            peering_name=dict(
                type='str'
            ),
            device_path=dict(
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
        self.circuit_name = None
        self.peering_name = None
        self.device_path = None
        super(AzureRMExpressRouteCircuitsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.circuit_name is not None and
                self.peering_name is not None and
                self.device_path is not None):
            self.results['ansible_facts']['list_arp_table'] = self.list_arp_table()
        elif (self.resource_group is not None and
              self.circuit_name is not None and
              self.peering_name is not None and
              self.device_path is not None):
            self.results['ansible_facts']['list_routes_table'] = self.list_routes_table()
        elif (self.resource_group is not None and
              self.circuit_name is not None and
              self.peering_name is not None and
              self.device_path is not None):
            self.results['ansible_facts']['list_routes_table_summary'] = self.list_routes_table_summary()
        elif (self.resource_group is not None and
              self.circuit_name is not None):
            self.results['ansible_facts']['get'] = self.get()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def list_arp_table(self):
        '''
        Gets facts of the specified Express Route Circuit.

        :return: deserialized Express Route Circuitinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.express_route_circuits.list_arp_table(resource_group_name=self.resource_group,
                                                                              circuit_name=self.circuit_name,
                                                                              peering_name=self.peering_name,
                                                                              device_path=self.device_path)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuits.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_routes_table(self):
        '''
        Gets facts of the specified Express Route Circuit.

        :return: deserialized Express Route Circuitinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.express_route_circuits.list_routes_table(resource_group_name=self.resource_group,
                                                                                 circuit_name=self.circuit_name,
                                                                                 peering_name=self.peering_name,
                                                                                 device_path=self.device_path)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuits.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_routes_table_summary(self):
        '''
        Gets facts of the specified Express Route Circuit.

        :return: deserialized Express Route Circuitinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.express_route_circuits.list_routes_table_summary(resource_group_name=self.resource_group,
                                                                                         circuit_name=self.circuit_name,
                                                                                         peering_name=self.peering_name,
                                                                                         device_path=self.device_path)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuits.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def get(self):
        '''
        Gets facts of the specified Express Route Circuit.

        :return: deserialized Express Route Circuitinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.express_route_circuits.get(resource_group_name=self.resource_group,
                                                                   circuit_name=self.circuit_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuits.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_all(self):
        '''
        Gets facts of the specified Express Route Circuit.

        :return: deserialized Express Route Circuitinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.express_route_circuits.list_all()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuits.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMExpressRouteCircuitsFacts()
if __name__ == '__main__':
    main()
