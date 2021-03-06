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
short_description: Get Top Level Domain facts.
description:
    - Get facts of Top Level Domain.

options:
    name:
        description:
            - Name of the top-level domain.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Top Level Domain
    azure_rm_webtopleveldomain_facts:
      name: name
'''

RETURN = '''
top_level_domains:
    description: A list of dict results where the key is the name of the Top Level Domain and the values are the facts for that Top Level Domain.
    returned: always
    type: complex
    contains:
        topleveldomain_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: /subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/providers/Microsoft.DomainRegistration/topLevelDomains/com
                name:
                    description:
                        - Resource Name.
                    returned: always
                    type: str
                    sample: com
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.DomainRegistration/topLevelDomains
                privacy:
                    description:
                        - If <code>true</code>, then the top level domain supports domain privacy; otherwise, <code>false</code>.
                    returned: always
                    type: str
                    sample: True
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
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.name = None
        super(AzureRMTopLevelDomainsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.name is not None):
            self.results['top_level_domains'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Top Level Domain.

        :return: deserialized Top Level Domaininstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.top_level_domains.get(name=self.name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for TopLevelDomains.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMTopLevelDomainsFacts()
if __name__ == '__main__':
    main()
