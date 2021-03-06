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
module: azure_rm_webappserviceenvironment_facts
version_added: "2.5"
short_description: Get App Service Environment facts.
description:
    - Get facts of App Service Environment.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of the App Service Environment.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
'''

RETURN = '''
app_service_environments:
    description: A list of dict results where the key is the name of the App Service Environment and the values are the facts for that App Service Environment.
    returned: always
    type: complex
    contains:
        appserviceenvironment_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: id
                status:
                    description:
                        - "Current status of the App Service Environment. Possible values include: 'Preparing', 'Ready', 'Scaling', 'Deleting'"
                    returned: always
                    type: str
                    sample: status
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


class AzureRMAppServiceEnvironmentsFacts(AzureRMModuleBase):
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
        super(AzureRMAppServiceEnvironmentsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.name is not None):
            self.results['app_service_environments'] = self.get()
        elif (self.resource_group is not None):
            self.results['app_service_environments'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.get(resource_group_name=self.resource_group,
                                                                     name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMAppServiceEnvironmentsFacts()
if __name__ == '__main__':
    main()
