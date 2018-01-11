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
        required: True
    name:
        description:
            - Name of the App Service plan.
    skip_token:
        description:
            - "Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting fro
              m (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list"
    filter:
        description:
            - "Supported filter: $filter=state eq running. Returns only web apps that are currently running"
    top:
        description:
            - List page size. If specified, results are paged.
    namespace_name:
        description:
            - The name of the Service Bus namespace.
    relay_name:
        description:
            - The name of the Service Bus relay.
    details:
        description:
            - Specify <code>true</code> to include instance details. The default is <code>false</code>.
    vnet_name:
        description:
            - Name of the Virtual Network.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      skip_token: skip_token
      filter: filter
      top: top

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      details: details
      filter: filter

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      vnet_name: vnet_name

  - name: Get instance of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Plan
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
'''

RETURN = '''
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
                type='str',
                required=True
            ),
            name=dict(
                type='str'
            ),
            skip_token=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='str'
            ),
            namespace_name=dict(
                type='str'
            ),
            relay_name=dict(
                type='str'
            ),
            details=dict(
                type='str'
            ),
            vnet_name=dict(
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
        self.skip_token = None
        self.filter = None
        self.top = None
        self.namespace_name = None
        self.relay_name = None
        self.details = None
        self.vnet_name = None
        super(AzureRMAppServicePlansFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.name is not None):
            self.results['ansible_facts']['list_web_apps'] = self.list_web_apps()
        elif (self.resource_group is not None and
              self.name is not None and
              self.namespace_name is not None and
              self.relay_name is not None):
            self.results['ansible_facts']['list_hybrid_connection_keys'] = self.list_hybrid_connection_keys()
        elif (self.resource_group is not None and
              self.name is not None and
              self.namespace_name is not None and
              self.relay_name is not None):
            self.results['ansible_facts']['list_web_apps_by_hybrid_connection'] = self.list_web_apps_by_hybrid_connection()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metrics'] = self.list_metrics()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_usages'] = self.list_usages()
        elif (self.resource_group is not None and
              self.name is not None and
              self.vnet_name is not None):
            self.results['ansible_facts']['list_routes_for_vnet'] = self.list_routes_for_vnet()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_capabilities'] = self.list_capabilities()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_hybrid_connections'] = self.list_hybrid_connections()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metric_defintions'] = self.list_metric_defintions()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['ansible_facts']['list_vnets'] = self.list_vnets()
        elif (self.resource_group is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def list_web_apps(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_web_apps(resource_group_name=self.resource_group,
                                                                        name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_hybrid_connection_keys(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_hybrid_connection_keys(resource_group_name=self.resource_group,
                                                                                      name=self.name,
                                                                                      namespace_name=self.namespace_name,
                                                                                      relay_name=self.relay_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_web_apps_by_hybrid_connection(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_web_apps_by_hybrid_connection(resource_group_name=self.resource_group,
                                                                                             name=self.name,
                                                                                             namespace_name=self.namespace_name,
                                                                                             relay_name=self.relay_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_metrics(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_metrics(resource_group_name=self.resource_group,
                                                                       name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_usages(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_usages(resource_group_name=self.resource_group,
                                                                      name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_routes_for_vnet(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_routes_for_vnet(resource_group_name=self.resource_group,
                                                                               name=self.name,
                                                                               vnet_name=self.vnet_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def get(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.get(resource_group_name=self.resource_group,
                                                              name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_capabilities(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_capabilities(resource_group_name=self.resource_group,
                                                                            name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_hybrid_connections(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_hybrid_connections(resource_group_name=self.resource_group,
                                                                                  name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_metric_defintions(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_metric_defintions(resource_group_name=self.resource_group,
                                                                                 name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_vnets(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_vnets(resource_group_name=self.resource_group,
                                                                     name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified App Service Plan.

        :return: deserialized App Service Planinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMAppServicePlansFacts()
if __name__ == '__main__':
    main()
