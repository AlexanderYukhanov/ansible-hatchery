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
short_description: Get AppServiceEnvironments facts.
description:
    - Get facts of AppServiceEnvironments.

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
            - "Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value e
               q 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'."
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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      start_time: start_time
      end_time: end_time
      time_grain: time_grain
      details: details
      filter: filter

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      instance: instance
      details: details
      filter: filter

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      details: details
      filter: filter

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      details: details
      filter: filter

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      instance: instance
      details: details

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name
      instance: instance

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      instance: instance

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      properties_to_include: properties_to_include

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name
      worker_pool_name: worker_pool_name

  - name: Get instance of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of AppServiceEnvironments
    azure_rm_webappserviceenvironment_facts:
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


class AzureRMAppServiceEnvironmentsFacts(AzureRMModuleBase):
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
            start_time=dict(
                type='str',
                required=False
            ),
            end_time=dict(
                type='str',
                required=False
            ),
            time_grain=dict(
                type='str',
                required=False
            ),
            details=dict(
                type='str',
                required=False
            ),
            filter=dict(
                type='str',
                required=False
            ),
            worker_pool_name=dict(
                type='str',
                required=False
            ),
            instance=dict(
                type='str',
                required=False
            ),
            properties_to_include=dict(
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

        if (self.resource_group_name is not None and
                self.name is not None):
            self.results['ansible_facts']['list_multi_role_metrics'] = self.list_multi_role_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None and
              self.instance is not None):
            self.results['ansible_facts']['list_worker_pool_instance_metrics'] = self.list_worker_pool_instance_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['ansible_facts']['list_web_worker_metrics'] = self.list_web_worker_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metrics'] = self.list_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.instance is not None):
            self.results['ansible_facts']['list_multi_role_pool_instance_metrics'] = self.list_multi_role_pool_instance_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None and
              self.instance is not None):
            self.results['ansible_facts']['list_worker_pool_instance_metric_definitions'] = self.list_worker_pool_instance_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.instance is not None):
            self.results['ansible_facts']['list_multi_role_pool_instance_metric_definitions'] = self.list_multi_role_pool_instance_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_web_apps'] = self.list_web_apps()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_usages'] = self.list_usages()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['ansible_facts']['list_web_worker_metric_definitions'] = self.list_web_worker_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['ansible_facts']['list_worker_pool_skus'] = self.list_worker_pool_skus()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.worker_pool_name is not None):
            self.results['ansible_facts']['list_web_worker_usages'] = self.list_web_worker_usages()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_capacities'] = self.list_capacities()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_vips'] = self.list_vips()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_diagnostics'] = self.list_diagnostics()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metric_definitions'] = self.list_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_multi_role_pools'] = self.list_multi_role_pools()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_multi_role_metric_definitions'] = self.list_multi_role_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_multi_role_pool_skus'] = self.list_multi_role_pool_skus()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_multi_role_usages'] = self.list_multi_role_usages()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_operations'] = self.list_operations()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_app_service_plans'] = self.list_app_service_plans()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_worker_pools'] = self.list_worker_pools()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def list_multi_role_metrics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_metrics(self.resource_group,
                                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_worker_pool_instance_metrics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_instance_metrics(self.resource_group,
                                                                                                   self.name,
                                                                                                   self.worker_pool_name,
                                                                                                   self.instance)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_worker_metrics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_metrics(self.resource_group,
                                                                                         self.name,
                                                                                         self.worker_pool_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metrics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_metrics(self.resource_group,
                                                                              self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_pool_instance_metrics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_instance_metrics(self.resource_group,
                                                                                                       self.name,
                                                                                                       self.instance)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_worker_pool_instance_metric_definitions(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_instance_metric_definitions(self.resource_group,
                                                                                                              self.name,
                                                                                                              self.worker_pool_name,
                                                                                                              self.instance)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_pool_instance_metric_definitions(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_instance_metric_definitions(self.resource_group,
                                                                                                                  self.name,
                                                                                                                  self.instance)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_apps(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_web_apps(self.resource_group,
                                                                               self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_usages(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_usages(self.resource_group,
                                                                             self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_worker_metric_definitions(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_metric_definitions(self.resource_group,
                                                                                                    self.name,
                                                                                                    self.worker_pool_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_worker_pool_skus(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pool_skus(self.resource_group,
                                                                                       self.name,
                                                                                       self.worker_pool_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_worker_usages(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_web_worker_usages(self.resource_group,
                                                                                        self.name,
                                                                                        self.worker_pool_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.get(self.resource_group,
                                                                     self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_capacities(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_capacities(self.resource_group,
                                                                                 self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_vips(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_vips(self.resource_group,
                                                                           self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_diagnostics(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_diagnostics(self.resource_group,
                                                                                  self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metric_definitions(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_metric_definitions(self.resource_group,
                                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_pools(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pools(self.resource_group,
                                                                                       self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_metric_definitions(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_metric_definitions(self.resource_group,
                                                                                                    self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_pool_skus(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_pool_skus(self.resource_group,
                                                                                           self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_multi_role_usages(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_multi_role_usages(self.resource_group,
                                                                                        self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_operations(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_operations(self.resource_group,
                                                                                 self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_app_service_plans(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_app_service_plans(self.resource_group,
                                                                                        self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_worker_pools(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_worker_pools(self.resource_group,
                                                                                   self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_resource_group(self):
        '''
        Gets facts of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironmentsinstance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.list_by_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMAppServiceEnvironmentsFacts()
if __name__ == '__main__':
    main()
