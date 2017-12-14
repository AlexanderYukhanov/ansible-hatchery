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
module: azure_rm_webdomain_facts
version_added: "2.5"
short_description: Get Domains facts.
description:
    - Get facts of Domains.

options:
    keywords:
        description:
            - Keywords to be used for generating domain recommendations.
    max_domain_recommendations:
        description:
            - Maximum number of recommendations.
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
    domain_name:
        description:
            - Name of the domain.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Domains
    azure_rm_webdomain_facts:
      keywords: keywords
      max_domain_recommendations: max_domain_recommendations

  - name: Get instance of Domains
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
      domain_name: domain_name

  - name: List instances of Domains
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
      domain_name: domain_name

  - name: List instances of Domains
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
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


class AzureRMDomainsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            keywords=dict(
                type='str',
                required=False
            ),
            max_domain_recommendations=dict(
                type='int',
                required=False
            ),
            resource_group=dict(
                type='str',
                required=False
            ),
            domain_name=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.keywords = None
        self.max_domain_recommendations = None
        self.resource_group = None
        self.domain_name = None
        super(AzureRMDomainsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

            self.results['ansible_facts']['list_recommendations'] = self.list_recommendations()
        elif (self.resource_group_name is not None and
              self.domain_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.domain_name is not None):
            self.results['ansible_facts']['list_ownership_identifiers'] = self.list_ownership_identifiers()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def list_recommendations(self):
        '''
        Gets facts of the specified Domains.

        :return: deserialized Domainsinstance state dictionary
        '''
        self.log("Checking if the Domains instance {0} is present".format(self.domain_name))
        found = False
        try:
            response = self.mgmt_client.domains.list_recommendations()
            found = True
            self.log("Response : {0}".format(response))
            self.log("Domains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Domains instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified Domains.

        :return: deserialized Domainsinstance state dictionary
        '''
        self.log("Checking if the Domains instance {0} is present".format(self.domain_name))
        found = False
        try:
            response = self.mgmt_client.domains.get(self.resource_group,
                                                    self.domain_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Domains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Domains instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_ownership_identifiers(self):
        '''
        Gets facts of the specified Domains.

        :return: deserialized Domainsinstance state dictionary
        '''
        self.log("Checking if the Domains instance {0} is present".format(self.domain_name))
        found = False
        try:
            response = self.mgmt_client.domains.list_ownership_identifiers(self.resource_group,
                                                                           self.domain_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Domains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Domains instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Domains.

        :return: deserialized Domainsinstance state dictionary
        '''
        self.log("Checking if the Domains instance {0} is present".format(self.domain_name))
        found = False
        try:
            response = self.mgmt_client.domains.list_by_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Domains instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Domains instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMDomainsFacts()
if __name__ == '__main__':
    main()