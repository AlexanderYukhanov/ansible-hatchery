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
module: azure_rm_applicationgatewaypacketcapture_facts
version_added: "2.5"
short_description: Get PacketCaptures facts.
description:
    - Get facts of PacketCaptures.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_watcher_name:
        description:
            - The name of the network watcher.
        required: True
    packet_capture_name:
        description:
            - The name of the packet capture session.
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of PacketCaptures
    azure_rm_applicationgatewaypacketcapture_facts:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name
      packet_capture_name: packet_capture_name
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


class AzureRMPacketCapturesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_watcher_name=dict(
                type='str',
                required=True
            ),
            packet_capture_name=dict(
                type='str',
                required=True
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.resource_group = None
        self.network_watcher_name = None
        self.packet_capture_name = None
        super(AzureRMPacketCapturesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.network_watcher_name is not None and
                self.packet_capture_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified PacketCaptures.

        :return: deserialized PacketCapturesinstance state dictionary
        '''
        self.log("Checking if the PacketCaptures instance {0} is present".format(self.packet_capture_name))
        found = False
        try:
            response = self.mgmt_client.packet_captures.get(self.resource_group,
                                                            self.network_watcher_name,
                                                            self.packet_capture_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("PacketCaptures instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the PacketCaptures instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMPacketCapturesFacts()
if __name__ == '__main__':
    main()
