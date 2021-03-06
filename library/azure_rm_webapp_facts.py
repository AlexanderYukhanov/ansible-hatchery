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
module: azure_rm_webapp_facts
version_added: "2.5"
short_description: Get Web App facts.
description:
    - Get facts of Web App.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    include_slots:
        description:
            - Specify <strong>true</strong> to include deployment slots in results. The default is false, which only gives you the production slot of all apps.
    name:
        description:
            - Name of the app.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Web App
    azure_rm_webapp_facts:
      resource_group: resource_group_name
      include_slots: include_slots

  - name: Get instance of Web App
    azure_rm_webapp_facts:
      resource_group: resource_group_name
      name: name
'''

RETURN = '''
web_apps:
    description: A list of dict results where the key is the name of the Web App and the values are the facts for that Web App.
    returned: always
    type: complex
    contains:
        webapp_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: id
                state:
                    description:
                        - Current state of the app.
                    returned: always
                    type: str
                    sample: state
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


class AzureRMWebAppsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            include_slots=dict(
                type='str'
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
        self.include_slots = None
        self.name = None
        super(AzureRMWebAppsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None):
            self.results['web_apps'] = self.list_by_resource_group()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['web_apps'] = self.get()
        return self.results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Web App.

        :return: deserialized Web Appinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.web_apps.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for WebApps.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def get(self):
        '''
        Gets facts of the specified Web App.

        :return: deserialized Web Appinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.web_apps.get(resource_group_name=self.resource_group,
                                                     name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for WebApps.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMWebAppsFacts()
if __name__ == '__main__':
    main()
