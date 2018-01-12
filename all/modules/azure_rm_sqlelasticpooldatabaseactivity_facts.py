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
module: azure_rm_sqlelasticpooldatabaseactivity_facts
version_added: "2.5"
short_description: Get Elastic Pool Database Activity facts.
description:
    - Get facts of Elastic Pool Database Activity.

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
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Elastic Pool Database Activity
    azure_rm_sqlelasticpooldatabaseactivity_facts:
      resource_group: resource_group_name
      server_name: server_name
      elastic_pool_name: elastic_pool_name
'''

RETURN = '''
elastic_pool_database_activities:
    description: A list of dict results where the key is the name of the Elastic Pool Database Activity and the values are the facts for that Elastic Pool Database Activity.
    returned: always
    type: complex
    contains:
        elasticpooldatabaseactivity_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMElasticPoolDatabaseActivitiesFacts(AzureRMModuleBase):
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
        self.server_name = None
        self.elastic_pool_name = None
        super(AzureRMElasticPoolDatabaseActivitiesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.elastic_pool_name is not None):
            self.results['elastic_pool_database_activities'] = self.list_by_elastic_pool()
        return self.results

    def list_by_elastic_pool(self):
        '''
        Gets facts of the specified Elastic Pool Database Activity.

        :return: deserialized Elastic Pool Database Activityinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.elastic_pool_database_activities.list_by_elastic_pool(resource_group_name=self.resource_group,
                                                                                              server_name=self.server_name,
                                                                                              elastic_pool_name=self.elastic_pool_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ElasticPoolDatabaseActivities.')

        if response is not None:
            results = {}
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMElasticPoolDatabaseActivitiesFacts()
if __name__ == '__main__':
    main()
