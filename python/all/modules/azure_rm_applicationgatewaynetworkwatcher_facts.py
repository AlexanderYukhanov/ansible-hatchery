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
module: azure_rm_applicationgatewaynetworkwatcher_facts
version_added: "2.5"
short_description: Get NetworkWatchers facts.
description:
    - Get facts of NetworkWatchers.

options:
    resource_group:
        description:
            - The name of the network watcher resource group.
    network_watcher_name:
        description:
            - The name of the network watcher resource.
    parameters:
        description:
            - Parameters that scope the list of available providers.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of NetworkWatchers
    azure_rm_applicationgatewaynetworkwatcher_facts:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name
      parameters: parameters

  - name: Get instance of NetworkWatchers
    azure_rm_applicationgatewaynetworkwatcher_facts:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name

  - name: List instances of NetworkWatchers
    azure_rm_applicationgatewaynetworkwatcher_facts:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNetworkWatchersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=False
            ),
            network_watcher_name=dict(
                type='str',
                required=False
            ),
            parameters=dict(
                type='dict',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.network_watcher_name = None
        self.parameters = None
        super(AzureRMNetworkWatchersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.network_watcher_name is not None and
                self.parameters is not None):
            self.results['ansible_facts']['list_available_providers'] = self.list_available_providers()
        elif (self.resource_group_name is not None and
              self.network_watcher_name is not None):
            self.results['ansible_facts']['get'] = self.get()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def list_available_providers(self):
        '''
        Gets facts of the specified NetworkWatchers.

        :return: deserialized NetworkWatchersinstance state dictionary
        '''
        self.log("Checking if the NetworkWatchers instance {0} is present".format(self.network_watcher_name))
        found = False
        try:
            response = self.mgmt_client.network_watchers.list_available_providers(self.resource_group,
                                                                                  self.network_watcher_name,
                                                                                  self.parameters)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkWatchers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkWatchers instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified NetworkWatchers.

        :return: deserialized NetworkWatchersinstance state dictionary
        '''
        self.log("Checking if the NetworkWatchers instance {0} is present".format(self.network_watcher_name))
        found = False
        try:
            response = self.mgmt_client.network_watchers.get(self.resource_group,
                                                             self.network_watcher_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkWatchers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkWatchers instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_all(self):
        '''
        Gets facts of the specified NetworkWatchers.

        :return: deserialized NetworkWatchersinstance state dictionary
        '''
        self.log("Checking if the NetworkWatchers instance {0} is present".format(self.network_watcher_name))
        found = False
        try:
            response = self.mgmt_client.network_watchers.list_all()
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkWatchers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkWatchers instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMNetworkWatchersFacts()
if __name__ == '__main__':
    main()
