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
module: azure_rm_applicationgatewaybgpservicecommunity_facts
version_added: "2.5"
short_description: Get Bgp Service Community facts.
description:
    - Get facts of Bgp Service Community.

options:

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Bgp Service Community
    azure_rm_applicationgatewaybgpservicecommunity_facts:
'''

RETURN = '''
bgp_service_communities:
    description: A list of dict results where the key is the name of the Bgp Service Community and the values are the facts for that Bgp Service Community.
    returned: always
    type: complex
    contains:
        bgpservicecommunity_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMBgpServiceCommunitiesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        super(AzureRMBgpServiceCommunitiesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results['bgp_service_communities'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Bgp Service Community.

        :return: deserialized Bgp Service Communityinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.bgp_service_communities.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for BgpServiceCommunities.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMBgpServiceCommunitiesFacts()
if __name__ == '__main__':
    main()
