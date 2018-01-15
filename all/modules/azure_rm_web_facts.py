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
module: azure_rm_web_facts
version_added: "2.5"
short_description: Get  facts.
description:
    - Get facts of .

options:
    sku:
        description:
            - Name of SKU used to filter the regions.
    linux_workers_enabled:
        description:
            - Specify <code>true</code> if you want to filter to only regions that support Linux workers.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of
    azure_rm_web_facts:
      sku: sku
      linux_workers_enabled: linux_workers_enabled

  - name: List instances of
    azure_rm_web_facts:

  - name: List instances of
    azure_rm_web_facts:

  - name: List instances of
    azure_rm_web_facts:
'''

RETURN = '''
:
    description: A list of dict results where the key is the name of the  and the values are the facts for that .
    returned: always
    type: complex
    contains:
        _name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            sku=dict(
                type='str'
            ),
            linux_workers_enabled=dict(
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.sku = None
        self.linux_workers_enabled = None
        super(AzureRMFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results[''] = self.list_geo_regions()
            self.results[''] = self.list_premier_add_on_offers()
            self.results[''] = self.list_skus()
            self.results[''] = self.list_source_controls()
        return self.results

    def list_geo_regions(self):
        '''
        Gets facts of the specified .

        :return: deserialized instance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client..list_geo_regions()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for .')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_premier_add_on_offers(self):
        '''
        Gets facts of the specified .

        :return: deserialized instance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client..list_premier_add_on_offers()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for .')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_skus(self):
        '''
        Gets facts of the specified .

        :return: deserialized instance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client..list_skus()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for .')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_source_controls(self):
        '''
        Gets facts of the specified .

        :return: deserialized instance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client..list_source_controls()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for .')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMFacts()
if __name__ == '__main__':
    main()
