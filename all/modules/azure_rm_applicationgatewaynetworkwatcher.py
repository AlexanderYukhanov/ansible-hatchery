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
module: azure_rm_applicationgatewaynetworkwatcher
version_added: "2.5"
short_description: Manage NetworkWatchers instance
description:
    - Create, update and delete instance of NetworkWatchers

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_watcher_name:
        description:
            - The name of the network watcher.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    etag:
        description:
            - A unique read-only string that changes whenever the resource is updated.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) NetworkWatchers
    azure_rm_applicationgatewaynetworkwatcher:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name
      id: id
      location: location
      etag: etag
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNetworkWatchers(AzureRMModuleBase):
    """Configuration class for an Azure RM NetworkWatchers resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_watcher_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            location=dict(
                type='str',
                required=False
            ),
            etag=dict(
                type='str',
                required=False
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.network_watcher_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetworkWatchers, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_networkwatchers()

        if not old_response:
            self.log("NetworkWatchers instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("NetworkWatchers instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if NetworkWatchers instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the NetworkWatchers instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_networkwatchers()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("NetworkWatchers instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_networkwatchers()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_networkwatchers():
                time.sleep(20)
        else:
            self.log("NetworkWatchers instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_networkwatchers(self):
        '''
        Creates or updates NetworkWatchers with the specified configuration.

        :return: deserialized NetworkWatchers instance state dictionary
        '''
        self.log("Creating / Updating the NetworkWatchers instance {0}".format(self.network_watcher_name))

        try:
            response = self.mgmt_client.network_watchers.create_or_update(self.resource_group,
                                                                          self.network_watcher_name,
                                                                          self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the NetworkWatchers instance.')
            self.fail("Error creating the NetworkWatchers instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_networkwatchers(self):
        '''
        Deletes specified NetworkWatchers instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the NetworkWatchers instance {0}".format(self.network_watcher_name))
        try:
            response = self.mgmt_client.network_watchers.delete(self.resource_group,
                                                                self.network_watcher_name)
        except CloudError as e:
            self.log('Error attempting to delete the NetworkWatchers instance.')
            self.fail("Error deleting the NetworkWatchers instance: {0}".format(str(e)))

        return True

    def get_networkwatchers(self):
        '''
        Gets the properties of the specified NetworkWatchers.

        :return: deserialized NetworkWatchers instance state dictionary
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


def main():
    """Main execution"""
    AzureRMNetworkWatchers()

if __name__ == '__main__':
    main()
