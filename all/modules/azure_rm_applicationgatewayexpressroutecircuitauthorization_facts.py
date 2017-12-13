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
module: azure_rm_applicationgatewayexpressroutecircuitauthorization_facts
version_added: "2.5"
short_description: Get ExpressRouteCircuitAuthorizations facts.
description:
    - Get facts of ExpressRouteCircuitAuthorizations.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of ExpressRouteCircuitAuthorizations
    azure_rm_applicationgatewayexpressroutecircuitauthorization_facts:
      resource_group: resource_group_name
      circuit_name: circuit_name
      authorization_name: authorization_name
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
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.circuit_name = None
        self.authorization_name = None
        super(AzureRMExpressRouteCircuitAuthorizationsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.circuit_name is not None and
                self.authorization_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified ExpressRouteCircuitAuthorizations.

        :return: deserialized ExpressRouteCircuitAuthorizationsinstance state dictionary
        '''
        self.log("Checking if the ExpressRouteCircuitAuthorizations instance {0} is present".format(self.authorization_name))
        found = False
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.get(self.resource_group,
                                                                                 self.circuit_name,
                                                                                 self.authorization_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ExpressRouteCircuitAuthorizations instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ExpressRouteCircuitAuthorizations instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMExpressRouteCircuitAuthorizationsFacts()
if __name__ == '__main__':
    main()
