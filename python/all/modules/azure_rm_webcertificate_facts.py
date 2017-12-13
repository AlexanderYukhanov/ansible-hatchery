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
short_description: Get Certificates facts.
description:
    - Get facts of Certificates.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Certificates
    azure_rm_webcertificate_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of Certificates
    azure_rm_webcertificate_facts:
      resource_group: resource_group_name
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
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.name = None
        super(AzureRMCertificatesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Certificates.

        :return: deserialized Certificatesinstance state dictionary
        '''
        self.log("Checking if the Certificates instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.certificates.get(self.resource_group,
                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Certificates instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Certificates instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Certificates.

        :return: deserialized Certificatesinstance state dictionary
        '''
        self.log("Checking if the Certificates instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.certificates.list_by_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Certificates instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Certificates instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMCertificatesFacts()
if __name__ == '__main__':
    main()
