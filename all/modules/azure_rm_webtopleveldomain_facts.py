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
module: azure_rm_webtopleveldomain_facts
version_added: "2.5"
short_description: Get TopLevelDomains facts.
description:
    - Get facts of TopLevelDomains.

options:
    name:
        description:
            - Name of the top-level domain.
        required: True
    include_privacy:
        description:
            - If <code>true</code>, then the list of agreements will include agreements for domain privacy as well; otherwise, <code>false</code>.
    for_transfer:
        description:
            - If <code>true</code>, then the list of agreements will include agreements for domain transfer as well; otherwise, <code>false</code>.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of TopLevelDomains
    azure_rm_webtopleveldomain_facts:
      name: name
      include_privacy: include_privacy
      for_transfer: for_transfer

  - name: Get instance of TopLevelDomains
    azure_rm_webtopleveldomain_facts:
      name: name
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


class AzureRMTopLevelDomainsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                required=True
            ),
            include_privacy=dict(
                type='str',
                required=False
            ),
            for_transfer=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.name = None
        self.include_privacy = None
        self.for_transfer = None
        super(AzureRMTopLevelDomainsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.name is not None):
            self.results['ansible_facts']['list_agreements'] = self.list_agreements()
        elif (self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def list_agreements(self):
        '''
        Gets facts of the specified TopLevelDomains.

        :return: deserialized TopLevelDomainsinstance state dictionary
        '''
        self.log("Checking if the TopLevelDomains instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.top_level_domains.list_agreements(self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("TopLevelDomains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the TopLevelDomains instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified TopLevelDomains.

        :return: deserialized TopLevelDomainsinstance state dictionary
        '''
        self.log("Checking if the TopLevelDomains instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.top_level_domains.get(self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("TopLevelDomains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the TopLevelDomains instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMTopLevelDomainsFacts()
if __name__ == '__main__':
    main()