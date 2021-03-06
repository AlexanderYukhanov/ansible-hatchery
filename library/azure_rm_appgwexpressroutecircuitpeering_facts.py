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
module: azure_rm_appgwexpressroutecircuitpeering_facts
version_added: "2.5"
short_description: Get Express Route Circuit Peering facts.
description:
    - Get facts of Express Route Circuit Peering.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    circuit_name:
        description:
            - The name of the express route circuit.
        required: True
    peering_name:
        description:
            - The name of the peering.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Express Route Circuit Peering
    azure_rm_appgwexpressroutecircuitpeering_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      peering_name: peering_name
'''

RETURN = '''
express_route_circuit_peerings:
    description: A list of dict results where the key is the name of the Express Route Circuit Peering and the values are the facts for that Express Route Circuit Peering.
    returned: always
    type: complex
    contains:
        expressroutecircuitpeering_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: id
                state:
                    description:
                        - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
                    returned: always
                    type: str
                    sample: state
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


class AzureRMExpressRouteCircuitPeeringsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            circuit_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
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
        self.circuit_name = None
        self.peering_name = None
        super(AzureRMExpressRouteCircuitPeeringsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.circuit_name is not None and
                self.peering_name is not None):
            self.results['express_route_circuit_peerings'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Express Route Circuit Peering.

        :return: deserialized Express Route Circuit Peeringinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.express_route_circuit_peerings.get(resource_group_name=self.resource_group,
                                                                           circuit_name=self.circuit_name,
                                                                           peering_name=self.peering_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuitPeerings.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMExpressRouteCircuitPeeringsFacts()
if __name__ == '__main__':
    main()
