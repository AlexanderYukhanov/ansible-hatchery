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
module: azure_rm_batchmanagementcertificate_facts
version_added: "2.5"
short_description: Get Certificate facts.
description:
    - Get facts of Certificate.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.
        required: True
    maxresults:
        description:
            - The maximum number of items to return in the response.
    select:
        description:
            - "Comma separated list of properties that should be returned. e.g. 'properties/provisioningState'. Only top level properties under properties/
               are valid for selection."
    filter:
        description:
            - "OData filter expression. Valid properties for filtering are 'properties/provisioningState', 'properties/provisioningStateTransitionTime',
               'name'."
    certificate_name:
        description:
            - "The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data
               in the request. For example SHA1-a3d1c5."

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Certificate
    azure_rm_batchmanagementcertificate_facts:
      resource_group: resource_group_name
      account_name: account_name
      maxresults: maxresults
      select: select
      filter: filter

  - name: Get instance of Certificate
    azure_rm_batchmanagementcertificate_facts:
      resource_group: resource_group_name
      account_name: account_name
      certificate_name: certificate_name
'''

RETURN = '''
certificate:
    description: A list of dict results where the key is the name of the Certificate and the values are the facts for that Certificate.
    returned: always
    type: complex
    contains:
        certificate_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - The ID of the resource.
                    returned: always
                    type: str
                    sample: "/subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.Batch/batchAccounts/samplecct/certificates/
                            SHA1-0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E"
                name:
                    description:
                        - The name of the resource.
                    returned: always
                    type: str
                    sample: SHA1-0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E
                type:
                    description:
                        - The type of the resource.
                    returned: always
                    type: str
                    sample: Microsoft.Batch/batchAccounts/certificates
                etag:
                    description:
                        - The ETag of the resource, used for concurrency statements.
                    returned: always
                    type: str
                    sample: "W/'0x8D4EDD5118668F7'"
                thumbprint:
                    description:
                        - This must match the thumbprint from the name.
                    returned: always
                    type: str
                    sample: 0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E
                format:
                    description:
                        - "The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx. Possible values include: 'Pfx', 'Cer'"
                    returned: always
                    type: str
                    sample: Pfx
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batchmanagement import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCertificateFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            maxresults=dict(
                type='int'
            ),
            select=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            certificate_name=dict(
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
        self.account_name = None
        self.maxresults = None
        self.select = None
        self.filter = None
        self.certificate_name = None
        super(AzureRMCertificateFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.account_name is not None):
            self.results['certificate'] = self.list_by_batch_account()
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.certificate_name is not None):
            self.results['certificate'] = self.get()
        return self.results

    def list_by_batch_account(self):
        '''
        Gets facts of the specified Certificate.

        :return: deserialized Certificateinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.certificate.list_by_batch_account(resource_group_name=self.resource_group,
                                                                          account_name=self.account_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Certificate.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def get(self):
        '''
        Gets facts of the specified Certificate.

        :return: deserialized Certificateinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.certificate.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        certificate_name=self.certificate_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Certificate.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMCertificateFacts()
if __name__ == '__main__':
    main()