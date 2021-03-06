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
module: azure_rm_batchmanagementcertificate
version_added: "2.5"
short_description: Manage Certificate instance.
description:
    - Create, update and delete instance of Certificate.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.
        required: True
    certificate_name:
        description:
            - "The identifier for the certificate. This must be made up of algorithm and I(thumbprint) separated by a dash, and must match the certificate
               I(data) in the request. For example SHA1-a3d1c5."
        required: True
    thumbprint_algorithm:
        description:
            - "This must match the first portion of the certificate name. Currently required to be 'SHA1'."
    thumbprint:
        description:
            - This must match the thumbprint from the name.
    format:
        description:
            - The format of the certificate - either C(pfx) or C(cer). If omitted, the default is C(pfx).
        choices:
            - 'pfx'
            - 'cer'
    data:
        description:
            - The maximum size is 10KB.
    password:
        description:
            - This is required if the certificate I(format) is C(pfx) and must be omitted if the certificate I(format) is C(cer).
    if_match:
        description:
            - "The entity state (ETag) version of the certificate to update. A value of '*' can be used to apply the operation only if the certificate
               already exists. If omitted, this operation will always be applied."
    if_none_match:
        description:
            - "Set to '*' to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored."
    state:
      description:
        - Assert the state of the Certificate.
        - Use 'present' to create or update an Certificate and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Certificate
    azure_rm_batchmanagementcertificate:
      resource_group: default-azurebatch-japaneast
      account_name: sampleacct
      certificate_name: SHA1-0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E
      if_match: NOT FOUND
      if_none_match: NOT FOUND
'''

RETURN = '''
id:
    description:
        - The ID of the resource.
    returned: always
    type: str
    sample: "/subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.Batch/batchAccounts/samplecct/certificates/SHA1-0A0E4F50D51
            BEADEAC1D35AFC5116098E7902E6E"
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batch import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCertificate(AzureRMModuleBase):
    """Configuration class for an Azure RM Certificate resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            certificate_name=dict(
                type='str',
                required=True
            ),
            thumbprint_algorithm=dict(
                type='str'
            ),
            thumbprint=dict(
                type='str'
            ),
            format=dict(
                type='str',
                choices=['pfx',
                         'cer']
            ),
            data=dict(
                type='str'
            ),
            password=dict(
                type='str',
                no_log=True
            ),
            if_match=dict(
                type='str'
            ),
            if_none_match=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.certificate_name = None
        self.parameters = dict()
        self.if_match = None
        self.if_none_match = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                 supports_check_mode=True,
                                                 supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "thumbprint_algorithm":
                    self.parameters["thumbprint_algorithm"] = kwargs[key]
                elif key == "thumbprint":
                    self.parameters["thumbprint"] = kwargs[key]
                elif key == "format":
                    self.parameters["format"] = _snake_to_camel(kwargs[key], True)
                elif key == "data":
                    self.parameters["data"] = kwargs[key]
                elif key == "password":
                    self.parameters["password"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_certificate()

        if not old_response:
            self.log("Certificate instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Certificate instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Certificate instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Certificate instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_certificate()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Certificate instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_certificate()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_certificate():
                time.sleep(20)
        else:
            self.log("Certificate instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_certificate(self):
        '''
        Creates or updates Certificate with the specified configuration.

        :return: deserialized Certificate instance state dictionary
        '''
        self.log("Creating / Updating the Certificate instance {0}".format(self.certificate_name))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.certificate.create(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               certificate_name=self.certificate_name,
                                                               parameters=self.parameters)
            else:
                response = self.mgmt_client.certificate.update(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               certificate_name=self.certificate_name,
                                                               parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Certificate instance.')
            self.fail("Error creating the Certificate instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_certificate(self):
        '''
        Deletes specified Certificate instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Certificate instance {0}".format(self.certificate_name))
        try:
            response = self.mgmt_client.certificate.delete(resource_group_name=self.resource_group,
                                                           account_name=self.account_name,
                                                           certificate_name=self.certificate_name)
        except CloudError as e:
            self.log('Error attempting to delete the Certificate instance.')
            self.fail("Error deleting the Certificate instance: {0}".format(str(e)))

        return True

    def get_certificate(self):
        '''
        Gets the properties of the specified Certificate.

        :return: deserialized Certificate instance state dictionary
        '''
        self.log("Checking if the Certificate instance {0} is present".format(self.certificate_name))
        found = False
        try:
            response = self.mgmt_client.certificate.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        certificate_name=self.certificate_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Certificate instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Certificate instance.')
        if found is True:
            return response.as_dict()

        return False


def _snake_to_camel(snake, capitalize_first=False):
    if capitalize_first:
        return ''.join(x.capitalize() or '_' for x in snake.split('_'))
    else:
        return snake.split('_')[0] + ''.join(x.capitalize() or '_' for x in snake.split('_')[1:])


def main():
    """Main execution"""
    AzureRMCertificate()

if __name__ == '__main__':
    main()
