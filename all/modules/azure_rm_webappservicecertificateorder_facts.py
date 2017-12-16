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
short_description: Get AppServiceCertificateOrders facts.
description:
    - Get facts of AppServiceCertificateOrders.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of AppServiceCertificateOrders
    azure_rm_webappservicecertificateorder_facts:
      resource_group: resource_group_name
      certificate_order_name: certificate_order_name

  - name: List instances of AppServiceCertificateOrders
    azure_rm_webappservicecertificateorder_facts:
      resource_group: resource_group_name
      certificate_order_name: certificate_order_name

  - name: List instances of AppServiceCertificateOrders
    azure_rm_webappservicecertificateorder_facts:
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


class AzureRMAppServiceCertificateOrdersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            certificate_order_name=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.resource_group = None
        self.certificate_order_name = None
        super(AzureRMAppServiceCertificateOrdersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.certificate_order_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.certificate_order_name is not None):
            self.results['ansible_facts']['list_certificates'] = self.list_certificates()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified AppServiceCertificateOrders.

        :return: deserialized AppServiceCertificateOrdersinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.app_service_certificate_orders.get(self.resource_group,
                                                                           self.certificate_order_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceCertificateOrders instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceCertificateOrders instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_certificates(self):
        '''
        Gets facts of the specified AppServiceCertificateOrders.

        :return: deserialized AppServiceCertificateOrdersinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.app_service_certificate_orders.list_certificates(self.resource_group,
                                                                                         self.certificate_order_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceCertificateOrders instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceCertificateOrders instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_resource_group(self):
        '''
        Gets facts of the specified AppServiceCertificateOrders.

        :return: deserialized AppServiceCertificateOrdersinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.app_service_certificate_orders.list_by_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceCertificateOrders instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceCertificateOrders instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMAppServiceCertificateOrdersFacts()
if __name__ == '__main__':
    main()
