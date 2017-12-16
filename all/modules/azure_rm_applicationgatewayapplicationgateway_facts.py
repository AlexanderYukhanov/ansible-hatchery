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
module: azure_rm_applicationgatewayapplicationgateway_facts
version_added: "2.5"
short_description: Get ApplicationGateways facts.
description:
    - Get facts of ApplicationGateways.

options:
    resource_group:
        description:
            - The name of the resource group.
    application_gateway_name:
        description:
            - The name of the application gateway.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway_facts:
      resource_group: resource_group_name
      application_gateway_name: application_gateway_name

  - name: List instances of ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway_facts:

  - name: List instances of ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway_facts:

  - name: List instances of ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway_facts:

  - name: List instances of ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway_facts:
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


class AzureRMApplicationGatewaysFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=False
            ),
            application_gateway_name=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.resource_group = None
        self.application_gateway_name = None
        super(AzureRMApplicationGatewaysFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.application_gateway_name is not None):
            self.results['ansible_facts']['get'] = self.get()
            self.results['ansible_facts']['list_all'] = self.list_all()
            self.results['ansible_facts']['list_available_waf_rule_sets'] = self.list_available_waf_rule_sets()
            self.results['ansible_facts']['list_available_ssl_options'] = self.list_available_ssl_options()
            self.results['ansible_facts']['list_available_ssl_predefined_policies'] = self.list_available_ssl_predefined_policies()
        return self.results

    def get(self):
        '''
        Gets facts of the specified ApplicationGateways.

        :return: deserialized ApplicationGatewaysinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.application_gateways.get(self.resource_group,
                                                                 self.application_gateway_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_all(self):
        '''
        Gets facts of the specified ApplicationGateways.

        :return: deserialized ApplicationGatewaysinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.application_gateways.list_all()
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_available_waf_rule_sets(self):
        '''
        Gets facts of the specified ApplicationGateways.

        :return: deserialized ApplicationGatewaysinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.application_gateways.list_available_waf_rule_sets()
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_available_ssl_options(self):
        '''
        Gets facts of the specified ApplicationGateways.

        :return: deserialized ApplicationGatewaysinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.application_gateways.list_available_ssl_options()
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_available_ssl_predefined_policies(self):
        '''
        Gets facts of the specified ApplicationGateways.

        :return: deserialized ApplicationGatewaysinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.application_gateways.list_available_ssl_predefined_policies()
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMApplicationGatewaysFacts()
if __name__ == '__main__':
    main()
