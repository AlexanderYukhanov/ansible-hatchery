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
module: azure_rm_sqlelasticpool_facts
version_added: "2.5"
short_description: Get ElasticPools facts.
description:
    - Get facts of ElasticPools.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    elastic_pool_name:
        description:
            - The name of the elastic pool.
    filter:
        description:
            - An OData filter expression that describes a subset of metrics to return.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of ElasticPools
    azure_rm_sqlelasticpool_facts:
      resource_group: resource_group_name
      server_name: server_name
      elastic_pool_name: elastic_pool_name
      filter: filter

  - name: List instances of ElasticPools
    azure_rm_sqlelasticpool_facts:
      resource_group: resource_group_name
      server_name: server_name
      elastic_pool_name: elastic_pool_name

  - name: Get instance of ElasticPools
    azure_rm_sqlelasticpool_facts:
      resource_group: resource_group_name
      server_name: server_name
      elastic_pool_name: elastic_pool_name

  - name: List instances of ElasticPools
    azure_rm_sqlelasticpool_facts:
      resource_group: resource_group_name
      server_name: server_name
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMElasticPoolsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            elastic_pool_name=dict(
                type='str',
                required=False
            ),
            filter=dict(
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
        self.server_name = None
        self.elastic_pool_name = None
        self.filter = None
        super(AzureRMElasticPoolsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.elastic_pool_name is not None and
                self.filter is not None):
            self.results['ansible_facts']['list_metrics'] = self.list_metrics()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.elastic_pool_name is not None):
            self.results['ansible_facts']['list_metric_definitions'] = self.list_metric_definitions()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.elastic_pool_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None):
            self.results['ansible_facts']['list_by_server'] = self.list_by_server()
        return self.results

    def list_metrics(self):
        '''
        Gets facts of the specified ElasticPools.

        :return: deserialized ElasticPoolsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.elastic_pools.list_metrics(self.resource_group,
                                                                   self.server_name,
                                                                   self.elastic_pool_name,
                                                                   self.filter)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ElasticPools.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_metric_definitions(self):
        '''
        Gets facts of the specified ElasticPools.

        :return: deserialized ElasticPoolsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.elastic_pools.list_metric_definitions(self.resource_group,
                                                                              self.server_name,
                                                                              self.elastic_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ElasticPools.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def get(self):
        '''
        Gets facts of the specified ElasticPools.

        :return: deserialized ElasticPoolsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.elastic_pools.get(self.resource_group,
                                                          self.server_name,
                                                          self.elastic_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ElasticPools.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_by_server(self):
        '''
        Gets facts of the specified ElasticPools.

        :return: deserialized ElasticPoolsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.elastic_pools.list_by_server(self.resource_group,
                                                                     self.server_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ElasticPools.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMElasticPoolsFacts()
if __name__ == '__main__':
    main()
