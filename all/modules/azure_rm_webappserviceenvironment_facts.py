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
    start_time:
        description:
            - Beginning time of the metrics query.
    end_time:
        description:
            - End time of the metrics query.
    time_grain:
        description:
            - Time granularity of the metrics query.
    details:
        description:
            - Specify <code>true</code> to include instance details. The default is <code>false</code>.
    filter:
        description:
            - "Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq C(Metric1) or name.value
              eq C(Metric2)) and startTime eq C(2014-01-01T00:00:00Z) and endTime eq C(2014-12-31T23:59:59Z) and timeGrain eq durationC([Hour|Minute|Day])."
    worker_pool_name:
        description:
            - Name of the worker pool.
    instance:
        description:
            - Name of the instance in the worker pool.
    properties_to_include:
        description:
            - Comma separated list of app properties to include.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      start_time: start_time
      end_time: end_time
      time_grain: time_grain
      details: details
      filter: filter

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      instance: instance
      details: details
      filter: filter

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      details: details
      filter: filter

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      details: details
      filter: filter

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      instance: instance
      details: details

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      instance: instance

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      instance: instance

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      properties_to_include: properties_to_include

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: Get instance of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of App Service Environment
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
                        - "Current status of the App Service Environment. Possible values include: C(Preparing), C(Ready), C(Scaling), C(Deleting)"
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
            ),
            start_time=dict(
                type='str'
            ),
            end_time=dict(
                type='str'
            ),
            time_grain=dict(
                type='str'
            ),
            details=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            worker_pool_name=dict(
                type='str'
            ),
            instance=dict(
                type='str'
            ),
            properties_to_include=dict(
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
        self.start_time = None
        self.end_time = None
        self.time_grain = None
        self.details = None
        self.filter = None
        self.worker_pool_name = None
        self.instance = None
        self.properties_to_include = None
        super(AzureRMAppServiceEnvironmentsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.name is not None):
            self.results['app_service_environments'] = self.list_multi_role_metrics()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None and
              self.instance is not None):
            self.results['app_service_environments'] = self.list_worker_pool_instance_metrics()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['app_service_environments'] = self.list_web_worker_metrics()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_metrics()
        elif (self.resource_group is not None and
              self.name is not None and
              self.instance is not None):
            self.results['app_service_environments'] = self.list_multi_role_pool_instance_metrics()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None and
              self.instance is not None):
            self.results['app_service_environments'] = self.list_worker_pool_instance_metric_definitions()
        elif (self.resource_group is not None and
              self.name is not None and
              self.instance is not None):
            self.results['app_service_environments'] = self.list_multi_role_pool_instance_metric_definitions()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_web_apps()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_usages()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['app_service_environments'] = self.list_web_worker_metric_definitions()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['app_service_environments'] = self.list_worker_pool_skus()
        elif (self.resource_group is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['app_service_environments'] = self.list_web_worker_usages()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.get()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_capacities()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_vips()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_diagnostics()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_multi_role_pools()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_multi_role_metric_definitions()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_multi_role_pool_skus()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_multi_role_usages()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_operations()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_app_service_plans()
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['app_service_environments'] = self.list_worker_pools()
        elif (self.resource_group is not None):
            self.results['app_service_environments'] = self.list_by_resource_group()
        return self.results

    def list_multi_role_metrics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_metrics(resource_group_name=self.resource_group,
                                                                                         name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_worker_pool_instance_metrics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_instance_metrics(resource_group_name=self.resource_group,
                                                                                                   name=self.name,
                                                                                                   worker_pool_name=self.worker_pool_name,
                                                                                                   instance=self.instance)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_web_worker_metrics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_metrics(resource_group_name=self.resource_group,
                                                                                         name=self.name,
                                                                                         worker_pool_name=self.worker_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_metrics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_metrics(resource_group_name=self.resource_group,
                                                                              name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_pool_instance_metrics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_instance_metrics(resource_group_name=self.resource_group,
                                                                                                       name=self.name,
                                                                                                       instance=self.instance)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_worker_pool_instance_metric_definitions(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_instance_metric_definitions(resource_group_name=self.resource_group,
                                                                                                              name=self.name,
                                                                                                              worker_pool_name=self.worker_pool_name,
                                                                                                              instance=self.instance)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_pool_instance_metric_definitions(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_instance_metric_definitions(resource_group_name=self.resource_group,
                                                                                                                  name=self.name,
                                                                                                                  instance=self.instance)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_web_apps(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_web_apps(resource_group_name=self.resource_group,
                                                                               name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_usages(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_usages(resource_group_name=self.resource_group,
                                                                             name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_web_worker_metric_definitions(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_metric_definitions(resource_group_name=self.resource_group,
                                                                                                    name=self.name,
                                                                                                    worker_pool_name=self.worker_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_worker_pool_skus(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_skus(resource_group_name=self.resource_group,
                                                                                       name=self.name,
                                                                                       worker_pool_name=self.worker_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_web_worker_usages(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_usages(resource_group_name=self.resource_group,
                                                                                        name=self.name,
                                                                                        worker_pool_name=self.worker_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

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

    def list_capacities(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_capacities(resource_group_name=self.resource_group,
                                                                                 name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_vips(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_vips(resource_group_name=self.resource_group,
                                                                           name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_diagnostics(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_diagnostics(resource_group_name=self.resource_group,
                                                                                  name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_pools(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pools(resource_group_name=self.resource_group,
                                                                                       name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_metric_definitions(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_metric_definitions(resource_group_name=self.resource_group,
                                                                                                    name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_pool_skus(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_skus(resource_group_name=self.resource_group,
                                                                                           name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_multi_role_usages(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_usages(resource_group_name=self.resource_group,
                                                                                        name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_operations(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_operations(resource_group_name=self.resource_group,
                                                                                 name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_app_service_plans(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_app_service_plans(resource_group_name=self.resource_group,
                                                                                        name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_worker_pools(self):
        '''
        Gets facts of the specified App Service Environment.

        :return: deserialized App Service Environmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pools(resource_group_name=self.resource_group,
                                                                                   name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceEnvironments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

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
