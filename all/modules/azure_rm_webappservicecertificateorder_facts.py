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
module: azure_rm_webappservicecertificateorder_facts
version_added: "2.5"
short_description: Get App Service Certificate Order facts.
description:
    - Get facts of App Service Certificate Order.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    certificate_order_name:
        description:
            - Name of the certificate order..

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of App Service Certificate Order
    azure_rm_webappservicecertificateorder_facts:
      resource_group: resource_group_name
      certificate_order_name: certificate_order_name

  - name: List instances of App Service Certificate Order
    azure_rm_webappservicecertificateorder_facts:
      resource_group: resource_group_name
'''

RETURN = '''
app_service_certificate_orders:
    description: A list of dict results where the key is the name of the App Service Certificate Order and the values are the facts for that App Service Certificate Order.
    returned: always
    type: complex
    contains:
        appservicecertificateorder_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource Id.
                    returned: always
                    type: str
                    sample: id
                status:
                    description:
                        - "Current order status. Possible values include: C(Pendingissuance), C(Issued), C(Revoked), C(Canceled), C(Denied), C(Pendingrevocat
                          ion), C(PendingRekey), C(Unused), C(Expired), C(NotSubmitted)"
                    returned: always
                    type: str
                    sample: status
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


class AzureRMAppServiceCertificateOrdersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            certificate_order_name=dict(
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
        self.certificate_order_name = None
        super(AzureRMAppServiceCertificateOrdersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.certificate_order_name is not None):
            self.results['app_service_certificate_orders'] = self.get()
        elif (self.resource_group is not None):
            self.results['app_service_certificate_orders'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified App Service Certificate Order.

        :return: deserialized App Service Certificate Orderinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_certificate_orders.get(resource_group_name=self.resource_group,
                                                                           certificate_order_name=self.certificate_order_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceCertificateOrders.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_resource_group(self):
        '''
        Gets facts of the specified App Service Certificate Order.

        :return: deserialized App Service Certificate Orderinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.app_service_certificate_orders.list_by_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for AppServiceCertificateOrders.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMAppServiceCertificateOrdersFacts()
if __name__ == '__main__':
    main()
