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
module: azure_rm_applicationgatewaypublicipaddresse_facts
version_added: "2.5"
short_description: Get Public I P Addresse facts.
description:
    - Get facts of Public I P Addresse.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    public_ip_address_name:
        description:
            - The name of the subnet.
        required: True
    expand:
        description:
            - Expands referenced resources.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Public I P Addresse
    azure_rm_applicationgatewaypublicipaddresse_facts:
      resource_group: resource_group_name
      public_ip_address_name: public_ip_address_name
      expand: expand
'''

RETURN = '''
public_ip_addresses:
    description: A list of dict results where the key is the name of the Public I P Addresse and the values are the facts for that Public I P Addresse.
    returned: always
    type: complex
    contains:
        publicipaddresse_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/testDNS-ip
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: testDNS-ip
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Network/publicIPAddresses
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: westus
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


class AzureRMPublicIPAddressesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            public_ip_address_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
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
        self.public_ip_address_name = None
        self.expand = None
        super(AzureRMPublicIPAddressesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.public_ip_address_name is not None):
            self.results['public_ip_addresses'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Public I P Addresse.

        :return: deserialized Public I P Addresseinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.public_ip_addresses.get(resource_group_name=self.resource_group,
                                                                public_ip_address_name=self.public_ip_address_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PublicIPAddresses.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMPublicIPAddressesFacts()
if __name__ == '__main__':
    main()
