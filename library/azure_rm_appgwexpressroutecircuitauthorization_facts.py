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
module: azure_rm_appgwexpressroutecircuitauthorization_facts
version_added: "2.5"
short_description: Get Express Route Circuit Authorization facts.
description:
    - Get facts of Express Route Circuit Authorization.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    circuit_name:
        description:
            - The name of the express route circuit.
        required: True
    authorization_name:
        description:
            - The name of the authorization.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Express Route Circuit Authorization
    azure_rm_appgwexpressroutecircuitauthorization_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      authorization_name: authorization_name
'''

RETURN = '''
express_route_circuit_authorizations:
    description: A list of dict results where the key is the name of the Express Route Circuit Authorization and the values are the facts for that Express Route Circuit Authorization.
    returned: always
    type: complex
    contains:
        expressroutecircuitauthorization_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: id
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


class AzureRMExpressRouteCircuitAuthorizationsFacts(AzureRMModuleBase):
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
            authorization_name=dict(
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
        self.authorization_name = None
        super(AzureRMExpressRouteCircuitAuthorizationsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.circuit_name is not None and
                self.authorization_name is not None):
            self.results['express_route_circuit_authorizations'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Express Route Circuit Authorization.

        :return: deserialized Express Route Circuit Authorizationinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.get(resource_group_name=self.resource_group,
                                                                                 circuit_name=self.circuit_name,
                                                                                 authorization_name=self.authorization_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteCircuitAuthorizations.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMExpressRouteCircuitAuthorizationsFacts()
if __name__ == '__main__':
    main()
