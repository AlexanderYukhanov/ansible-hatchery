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
module: azure_rm_applicationgatewayexpressrouteserviceprovider_facts
version_added: "2.5"
short_description: Get Express Route Service Provider facts.
description:
    - Get facts of Express Route Service Provider.

options:

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Express Route Service Provider
    azure_rm_applicationgatewayexpressrouteserviceprovider_facts:
'''

RETURN = '''
express_route_service_providers:
    description: A list of dict results where the key is the name of the Express Route Service Provider and the values are the facts for that Express Route Service Provider.
    returned: always
    type: complex
    contains:
        expressrouteserviceprovider_name:
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


class AzureRMExpressRouteServiceProvidersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        super(AzureRMExpressRouteServiceProvidersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results['express_route_service_providers'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Express Route Service Provider.

        :return: deserialized Express Route Service Providerinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.express_route_service_providers.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ExpressRouteServiceProviders.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMExpressRouteServiceProvidersFacts()
if __name__ == '__main__':
    main()
