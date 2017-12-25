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
module: azure_rm_webdiagnostic_facts
version_added: "2.5"
short_description: Get Diagnostics facts.
description:
    - Get facts of Diagnostics.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    site_name:
        description:
            - Site Name
        required: True
    diagnostic_category:
        description:
            - Diagnostic Category
    slot:
        description:
            - Slot Name

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
      diagnostic_category: diagnostic_category
      slot: slot

  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
      diagnostic_category: diagnostic_category
      slot: slot

  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
      diagnostic_category: diagnostic_category

  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
      diagnostic_category: diagnostic_category

  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
      slot: slot

  - name: List instances of Diagnostics
    azure_rm_webdiagnostic_facts:
      resource_group: resource_group_name
      site_name: site_name
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


class AzureRMDiagnosticsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            site_name=dict(
                type='str',
                required=True
            ),
            diagnostic_category=dict(
                type='str'
            ),
            slot=dict(
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
        self.site_name = None
        self.diagnostic_category = None
        self.slot = None
        super(AzureRMDiagnosticsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.site_name is not None and
                self.diagnostic_category is not None and
                self.slot is not None):
            self.results['ansible_facts']['list_site_analyses_slot'] = self.list_site_analyses_slot()
        elif (self.resource_group is not None and
              self.site_name is not None and
              self.diagnostic_category is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_site_detectors_slot'] = self.list_site_detectors_slot()
        elif (self.resource_group is not None and
              self.site_name is not None and
              self.diagnostic_category is not None):
            self.results['ansible_facts']['list_site_analyses'] = self.list_site_analyses()
        elif (self.resource_group is not None and
              self.site_name is not None and
              self.diagnostic_category is not None):
            self.results['ansible_facts']['list_site_detectors'] = self.list_site_detectors()
        elif (self.resource_group is not None and
              self.site_name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_site_diagnostic_categories_slot'] = self.list_site_diagnostic_categories_slot()
        elif (self.resource_group is not None and
              self.site_name is not None):
            self.results['ansible_facts']['list_site_diagnostic_categories'] = self.list_site_diagnostic_categories()
        return self.results

    def list_site_analyses_slot(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_analyses_slot(resource_group_name=self.resource_group,
                                                                            site_name=self.site_name,
                                                                            diagnostic_category=self.diagnostic_category,
                                                                            slot=self.slot)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_site_detectors_slot(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_detectors_slot(resource_group_name=self.resource_group,
                                                                             site_name=self.site_name,
                                                                             diagnostic_category=self.diagnostic_category,
                                                                             slot=self.slot)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_site_analyses(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_analyses(resource_group_name=self.resource_group,
                                                                       site_name=self.site_name,
                                                                       diagnostic_category=self.diagnostic_category)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_site_detectors(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_detectors(resource_group_name=self.resource_group,
                                                                        site_name=self.site_name,
                                                                        diagnostic_category=self.diagnostic_category)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_site_diagnostic_categories_slot(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_diagnostic_categories_slot(resource_group_name=self.resource_group,
                                                                                         site_name=self.site_name,
                                                                                         slot=self.slot)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_site_diagnostic_categories(self):
        '''
        Gets facts of the specified Diagnostics.

        :return: deserialized Diagnosticsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.diagnostics.list_site_diagnostic_categories(resource_group_name=self.resource_group,
                                                                                    site_name=self.site_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Diagnostics.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMDiagnosticsFacts()
if __name__ == '__main__':
    main()
