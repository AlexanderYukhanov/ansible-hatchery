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
short_description: Get AppServicePlans facts.
description:
    - Get facts of AppServicePlans.

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
            - Supported filter: $filter=state eq running. Returns only web apps that are currently running
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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      skip_token: skip_token
      filter: filter
      top: top

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      details: details
      filter: filter

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name
      vnet_name: vnet_name

  - name: Get instance of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServicePlans
    azure_rm_webappserviceplan_facts:
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


class AzureRMAppServicePlansFacts(AzureRMModuleBase):
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
            skip_token=dict(
                type='str',
                required=False
            ),
            filter=dict(
                type='str',
                required=False
            ),
            top=dict(
                type='str',
                required=False
            ),
            namespace_name=dict(
                type='str',
                required=False
            ),
            relay_name=dict(
                type='str',
                required=False
            ),
            details=dict(
                type='str',
                required=False
            ),
            vnet_name=dict(
                type='str',
                required=False
            ),
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_web_apps(self.resource_group,
                                                                        self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_hybrid_connection_keys(self.resource_group,
                                                                                      self.name,
                                                                                      self.namespace_name,
                                                                                      self.relay_name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_web_apps_by_hybrid_connection(self.resource_group,
                                                                                             self.name,
                                                                                             self.namespace_name,
                                                                                             self.relay_name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_metrics(self.resource_group,
                                                                       self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_usages(self.resource_group,
                                                                      self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_routes_for_vnet(self.resource_group,
                                                                               self.name,
                                                                               self.vnet_name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.get(self.resource_group,
                                                              self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServicePlans.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_capabilities(self):
        '''
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_capabilities(self.resource_group,
                                                                            self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_hybrid_connections(self.resource_group,
                                                                                  self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_metric_defintions(self.resource_group,
                                                                                 self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_vnets(self.resource_group,
                                                                     self.name)
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
        Gets facts of the specified AppServicePlans.

        :return: deserialized AppServicePlansinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.app_service_plans.list_by_resource_group(self.resource_group)
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
