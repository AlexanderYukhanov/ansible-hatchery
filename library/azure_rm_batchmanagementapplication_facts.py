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
module: azure_rm_batchmanagementapplication_facts
version_added: "2.5"
short_description: Get Application facts.
description:
    - Get facts of Application.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.
        required: True
    application_id:
        description:
            - The ID of the application.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Application
    azure_rm_batchmanagementapplication_facts:
      resource_group: resource_group_name
      account_name: account_name
      application_id: application_id
'''

RETURN = '''
application:
    description: A list of dict results where the key is the name of the Application and the values are the facts for that Application.
    returned: always
    type: complex
    contains:
        application_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - A string that uniquely identifies the application within the account.
                    returned: always
                    type: str
                    sample: id
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batch import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMApplicationFacts(AzureRMModuleBase):
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
            application_id=dict(
                type='str',
                required=True
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
        self.application_id = None
        super(AzureRMApplicationFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.account_name is not None and
                self.application_id is not None):
            self.results['application'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Application.

        :return: deserialized Applicationinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.application.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        application_id=self.application_id)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Application.')

        if response is not None:
            results[response.id] = response.as_dict()

        return results


def main():
    AzureRMApplicationFacts()
if __name__ == '__main__':
    main()
