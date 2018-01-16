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
short_description: Get Packet Capture facts.
description:
    - Get facts of Packet Capture.

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

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Packet Capture
    azure_rm_applicationgatewaypacketcapture_facts:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name
      packet_capture_name: packet_capture_name

  - name: List instances of Packet Capture
    azure_rm_applicationgatewaypacketcapture_facts:
      resource_group: resource_group_name
      network_watcher_name: network_watcher_name
'''

RETURN = '''
packet_captures:
    description: A list of dict results where the key is the name of the Packet Capture and the values are the facts for that Packet Capture.
    returned: always
    type: complex
    contains:
        packetcapture_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - ID of the packet capture operation.
                    returned: always
                    type: str
                    sample: id
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
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
        self.network_watcher_name = None
        self.packet_capture_name = None
        super(AzureRMPacketCapturesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.network_watcher_name is not None and
                self.packet_capture_name is not None):
            self.results['packet_captures'] = self.get()
        elif (self.resource_group is not None and
              self.network_watcher_name is not None):
            self.results['packet_captures'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Packet Capture.

        :return: deserialized Packet Captureinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.packet_captures.get(resource_group_name=self.resource_group,
                                                            network_watcher_name=self.network_watcher_name,
                                                            packet_capture_name=self.packet_capture_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PacketCaptures.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Packet Capture.

        :return: deserialized Packet Captureinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.packet_captures.list(resource_group_name=self.resource_group,
                                                             network_watcher_name=self.network_watcher_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PacketCaptures.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMPacketCapturesFacts()
if __name__ == '__main__':
    main()
