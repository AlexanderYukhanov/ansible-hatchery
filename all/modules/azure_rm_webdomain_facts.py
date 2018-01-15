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
short_description: Get Domain facts.
description:
    - Get facts of Domain.

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

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Domain
    azure_rm_webdomain_facts:
      keywords: keywords
      max_domain_recommendations: max_domain_recommendations

  - name: Get instance of Domain
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
      domain_name: domain_name

  - name: List instances of Domain
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
      domain_name: domain_name

  - name: List instances of Domain
    azure_rm_webdomain_facts:
      resource_group: resource_group_name
'''

RETURN = '''
domains:
    description: A list of dict results where the key is the name of the Domain and the values are the facts for that Domain.
    returned: always
    type: complex
    contains:
        domain_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: id
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
                type='str'
            ),
            max_domain_recommendations=dict(
                type='int'
            ),
            resource_group=dict(
                type='str'
            ),
            domain_name=dict(
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.keywords = None
        self.max_domain_recommendations = None
        self.resource_group = None
        self.domain_name = None
        super(AzureRMDomainsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results['domains'] = self.list_recommendations()
        elif (self.resource_group is not None and
              self.domain_name is not None):
            self.results['domains'] = self.get()
        elif (self.resource_group is not None and
              self.domain_name is not None):
            self.results['domains'] = self.list_ownership_identifiers()
        elif (self.resource_group is not None):
            self.results['domains'] = self.list_by_resource_group()
        return self.results

    def list_recommendations(self):
        '''
        Gets facts of the specified Domain.

        :return: deserialized Domaininstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.domains.list_recommendations()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Domains.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def get(self):
        '''
        Gets facts of the specified Domain.

        :return: deserialized Domaininstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.domains.get(resource_group_name=self.resource_group,
                                                    domain_name=self.domain_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Domains.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_ownership_identifiers(self):
        '''
        Gets facts of the specified Domain.

        :return: deserialized Domaininstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.domains.list_ownership_identifiers(resource_group_name=self.resource_group,
                                                                           domain_name=self.domain_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Domains.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified Domain.

        :return: deserialized Domaininstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.domains.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Domains.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMDomainsFacts()
if __name__ == '__main__':
    main()
