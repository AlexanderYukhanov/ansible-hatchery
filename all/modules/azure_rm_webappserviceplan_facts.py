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
module: azure_rm_webappserviceplan_facts
version_added: "2.5"
short_description: Get App Service Plan facts.
description:
    - Get facts of App Service Plan.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
    name:
        description:
            - Name of the App Service plan.
    detailed:
        description:
            - "Specify <code>true</code> to return all App Service plan properties. The default is <code>false</code>, which returns a subset of the properti
              es.\n Retrieval of all properties may increase the API latency."

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      detailed: detailed

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
'''

RETURN = '''
app_service_plans:
    description: A list of dict results where the key is the name of the App Service Plan and the values are the facts for that App Service Plan.
    returned: always
    type: complex
    contains:
        appserviceplan_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: /subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testrg123/providers/Microsoft.Web/serverfarms/testsf6141
                name:
                    description:
                        - Resource Name.
                    returned: always
                    type: str
                    sample: testsf6141
                kind:
                    description:
                        - Kind of resource.
                    returned: always
                    type: str
                    sample: app
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
                    sample: Microsoft.Web/serverfarms
                status:
                    description:
                        - "App Service plan status. Possible values include: C(Ready), C(Pending), C(Creating)"
                    returned: always
                    type: str
                    sample: Ready
                reserved:
                    description:
                        - If Linux app service plan <code>true</code>, <code>false</code> otherwise.
                    returned: always
                    type: str
                    sample: False
                sku:
                    description:
                        -
                    returned: always
                    type: complex
                    sample: sku
                    contains:
                        name:
                            description:
                                - Name of the resource SKU.
                            returned: always
                            type: str
                            sample: P1
                        tier:
                            description:
                                - Service tier of the resource SKU.
                            returned: always
                            type: str
                            sample: Premium
                        size:
                            description:
                                - Size specifier of the resource SKU.
                            returned: always
                            type: str
                            sample: P1
                        family:
                            description:
                                - Family code of the resource SKU.
                            returned: always
                            type: str
                            sample: P
                        capacity:
                            description:
                                - Current number of instances assigned to the resource.
                            returned: always
                            type: int
                            sample: 1
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


class AzureRMAppServicePlansFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            detailed=dict(
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
        self.detailed = None
        super(AzureRMAppServicePlansFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.name is not None):
            self.results['app_service_plans'] = self.get()
            self.results['app_service_plans'] = self.list()
        elif (self.resource_group is not None):
            self.results['app_service_plans'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_plans.get(resource_group_name=self.resource_group,
                                                              name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_plans.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_plans.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMAppServicePlansFacts()
if __name__ == '__main__':
    main()
