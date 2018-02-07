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
module: azure_rm_batchaicluster_facts
version_added: "2.5"
short_description: Get Cluster facts.
description:
    - Get facts of Cluster.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    cluster_name:
        description:
            - "The name of the cluster within the specified resource group. Cluster names can only contain a combination of alphanumeric characters along
               with dash (-) and underscore (_). The name must be from 1 through 64 characters long."
    clusters_list_by_resource_group_options:
        description:
            - Additional parameters for the operation

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Cluster
    azure_rm_batchaicluster_facts:
      resource_group: resource_group_name
      cluster_name: cluster_name

  - name: List instances of Cluster
    azure_rm_batchaicluster_facts:
      resource_group: resource_group_name
      clusters_list_by_resource_group_options: clusters_list_by_resource_group_options
'''

RETURN = '''
clusters:
    description: A list of dict results where the key is the name of the Cluster and the values are the facts for that Cluster.
    returned: always
    type: complex
    contains:
        cluster_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - The ID of the resource
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/demo_resource_group/providers/Microsoft.BatchAI/clusters/demo
                            _cluster"
                name:
                    description:
                        - The name of the resource
                    returned: always
                    type: str
                    sample: demo_cluster
                type:
                    description:
                        - The type of the resource
                    returned: always
                    type: str
                    sample: Microsoft.BatchAI/Clusters
                location:
                    description:
                        - The location of the resource
                    returned: always
                    type: str
                    sample: eastus
                subnet:
                    description:
                        -
                    returned: always
                    type: complex
                    sample: subnet
                    contains:
                        id:
                            description:
                                - The ID of the resource
                            returned: always
                            type: str
                            sample: "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/demo_resource_group/providers/Microsoft.Network/virtu
                                    alNetworks/7feb1976-8c31-4f1f-bea2-86cb1839a7bavnet/subnets/Subnet-1"
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batchai import BatchAIManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMClustersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str'
            ),
            clusters_list_by_resource_group_options=dict(
                type='dict'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.cluster_name = None
        self.clusters_list_by_resource_group_options = None
        super(AzureRMClustersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(BatchAIManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.cluster_name is not None):
            self.results['clusters'] = self.get()
        elif (self.resource_group is not None):
            self.results['clusters'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Cluster.

        :return: deserialized Clusterinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.clusters.get(resource_group_name=self.resource_group,
                                                     cluster_name=self.cluster_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Clusters.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Cluster.

        :return: deserialized Clusterinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.clusters.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Clusters.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMClustersFacts()
if __name__ == '__main__':
    main()
