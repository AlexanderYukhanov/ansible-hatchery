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
module: azure_rm_authorizationprovideroperationsmetadata_facts
version_added: "2.5"
short_description: Get ProviderOperationsMetadata facts.
description:
    - Get facts of ProviderOperationsMetadata.

options:
    resource_provider_namespace:
        description:
            - The namespace of the resource provider.
        required: True
    expand:
        description:
            - Specifies whether to expand the values.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of ProviderOperationsMetadata
    azure_rm_authorizationprovideroperationsmetadata_facts:
      resource_provider_namespace: resource_provider_namespace
      expand: expand
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProviderOperationsMetadataFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_provider_namespace=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_provider_namespace = None
        self.expand = None
        super(AzureRMProviderOperationsMetadataFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_provider_namespace is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified ProviderOperationsMetadata.

        :return: deserialized ProviderOperationsMetadatainstance state dictionary
        '''
        self.log("Checking if the ProviderOperationsMetadata instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.provider_operations_metadata.get(self.resource_provider_namespace)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ProviderOperationsMetadata instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ProviderOperationsMetadata instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMProviderOperationsMetadataFacts()
if __name__ == '__main__':
    main()
