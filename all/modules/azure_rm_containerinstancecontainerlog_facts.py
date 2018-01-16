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
module: azure_rm_containerinstancecontainerlog_facts
version_added: "2.5"
short_description: Get Container Log facts.
description:
    - Get facts of Container Log.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    container_group_name:
        description:
            - The name of the container group.
        required: True
    container_name:
        description:
            - The name of the container instance.
        required: True
    tail:
        description:
            - The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Container Log
    azure_rm_containerinstancecontainerlog_facts:
      resource_group: resource_group_name
      container_group_name: container_group_name
      container_name: container_name
      tail: tail
'''

RETURN = '''
container_logs:
    description: A list of dict results where the key is the name of the Container Log and the values are the facts for that Container Log.
    returned: always
    type: complex
    contains:
        containerlog_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.containerinstance import ContainerInstanceManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMContainerLogsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            container_group_name=dict(
                type='str',
                required=True
            ),
            container_name=dict(
                type='str',
                required=True
            ),
            tail=dict(
                type='int'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.container_group_name = None
        self.container_name = None
        self.tail = None
        super(AzureRMContainerLogsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(ContainerInstanceManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.container_group_name is not None and
                self.container_name is not None):
            self.results['container_logs'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Container Log.

        :return: deserialized Container Loginstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.container_logs.list(resource_group_name=self.resource_group,
                                                            container_group_name=self.container_group_name,
                                                            container_name=self.container_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ContainerLogs.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMContainerLogsFacts()
if __name__ == '__main__':
    main()
