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
module: azure_rm_webdomainregistrationprovider_facts
version_added: "2.5"
short_description: Get DomainRegistrationProvider facts.
description:
    - Get facts of DomainRegistrationProvider.

options:

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of DomainRegistrationProvider
    azure_rm_webdomainregistrationprovider_facts:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.web import WebSiteManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDomainRegistrationProviderFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        super(AzureRMDomainRegistrationProviderFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

            self.results['ansible_facts']['list_operations'] = self.list_operations()
        return self.results

    def list_operations(self):
        '''
        Gets facts of the specified DomainRegistrationProvider.

        :return: deserialized DomainRegistrationProviderinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.domain_registration_provider.list_operations()
            found = True
            self.log("Response : {0}".format(response))
            self.log("DomainRegistrationProvider instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DomainRegistrationProvider instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMDomainRegistrationProviderFacts()
if __name__ == '__main__':
    main()
