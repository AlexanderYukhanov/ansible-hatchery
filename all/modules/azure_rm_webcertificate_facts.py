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
module: azure_rm_webcertificate_facts
version_added: "2.5"
short_description: Get Certificate facts.
description:
    - Get facts of Certificate.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of the certificate.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Certificate
    azure_rm_webcertificate_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of Certificate
    azure_rm_webcertificate_facts:
      resource_group: resource_group_name
'''

RETURN = '''
    id:
        description:
            - Resource Id.
        returned: always
        type: str
        sample: /subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Web/certificates/testc6282
    name:
        description:
            - Resource Name.
        returned: always
        type: str
        sample: testc6282
    location:
        description:
            - Resource Location.
        returned: always
        type: str
        sample: East US
    type:
        description:
            - Resource type.
        returned: always
        type: str
        sample: Microsoft.Web/certificates
    issuer:
        description:
            - Certificate issuer.
        returned: always
        type: str
        sample: CACert
    password:
        description:
            - Certificate password.
        returned: always
        type: str
        sample: SWsSsd__233$Sdsds#%Sd!
    thumbprint:
        description:
            - Certificate thumbprint.
        returned: always
        type: str
        sample: FE703D7411A44163B6D32B3AD9B03E175886EBFE
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


class AzureRMCertificatesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
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
        self.name = None
        super(AzureRMCertificatesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Certificate.

        :return: deserialized Certificateinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.certificates.get(resource_group_name=self.resource_group,
                                                         name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Certificates.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Certificate.

        :return: deserialized Certificateinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.certificates.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Certificates.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMCertificatesFacts()
if __name__ == '__main__':
    main()
