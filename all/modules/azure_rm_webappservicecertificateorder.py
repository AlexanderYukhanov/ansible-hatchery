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
module: azure_rm_webappservicecertificateorder
version_added: "2.5"
short_description: Manage AppServiceCertificateOrders instance.
description:
    - Create, update and delete instance of AppServiceCertificateOrders.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    certificate_order_name:
        description:
            - Name of the certificate order.
        required: True
    kind:
        description:
            - Kind of resource.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    certificates:
        description:
            - State of the Key Vault secret.
    distinguished_name:
        description:
            - Certificate distinguished name.
    validity_in_years:
        description:
            - Duration in years (must be between 1 and 3).
    key_size:
        description:
            - Certificate key size.
    product_type:
        description:
            - Certificate product type. Possible values include: C(StandardDomainValidatedSsl), C(StandardDomainValidatedWildCardSsl)
        choices: ['StandardDomainValidatedSsl', 'StandardDomainValidatedWildCardSsl']
    auto_renew:
        description:
            - <code>true</code> if the certificate should be automatically renewed when it expires; otherwise, <code>false</code>.
    csr:
        description:
            - Last CSR that was created for this order.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) AppServiceCertificateOrders
    azure_rm_webappservicecertificateorder:
      resource_group: NOT FOUND
      certificate_order_name: NOT FOUND
      location: eastus
'''

RETURN = '''
id:
    description:
        - Resource Id.
    returned: always
    type: str
    sample: id
status:
    description:
        - "Current order status. Possible values include: C(Pendingissuance), C(Issued), C(Revoked), C(Canceled), C(Denied), C(Pendingrevocation), C(PendingR
           ekey), C(Unused), C(Expired), C(NotSubmitted)"
    returned: always
    type: str
    sample: status
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.web import WebSiteManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAppServiceCertificateOrders(AzureRMModuleBase):
    """Configuration class for an Azure RM AppServiceCertificateOrders resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            certificate_order_name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            certificates=dict(
                type='dict'
            ),
            distinguished_name=dict(
                type='str'
            ),
            validity_in_years=dict(
                type='int'
            ),
            key_size=dict(
                type='int'
            ),
            product_type=dict(
                type='str',
                choices=['StandardDomainValidatedSsl', 'StandardDomainValidatedWildCardSsl']
            ),
            auto_renew=dict(
                type='str'
            ),
            csr=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.certificate_order_name = None
        self.certificate_distinguished_name = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAppServiceCertificateOrders, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                 supports_check_mode=True,
                                                                 supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "kind":
                    self.certificate_distinguished_name["kind"] = kwargs[key]
                elif key == "location":
                    self.certificate_distinguished_name["location"] = kwargs[key]
                elif key == "certificates":
                    self.certificate_distinguished_name["certificates"] = kwargs[key]
                elif key == "distinguished_name":
                    self.certificate_distinguished_name["distinguished_name"] = kwargs[key]
                elif key == "validity_in_years":
                    self.certificate_distinguished_name["validity_in_years"] = kwargs[key]
                elif key == "key_size":
                    self.certificate_distinguished_name["key_size"] = kwargs[key]
                elif key == "product_type":
                    self.certificate_distinguished_name["product_type"] = kwargs[key]
                elif key == "auto_renew":
                    self.certificate_distinguished_name["auto_renew"] = kwargs[key]
                elif key == "csr":
                    self.certificate_distinguished_name["csr"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_appservicecertificateorders()

        if not old_response:
            self.log("AppServiceCertificateOrders instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("AppServiceCertificateOrders instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if AppServiceCertificateOrders instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the AppServiceCertificateOrders instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_appservicecertificateorders()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("AppServiceCertificateOrders instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_appservicecertificateorders()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_appservicecertificateorders():
                time.sleep(20)
        else:
            self.log("AppServiceCertificateOrders instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["status"] = response["status"]

        return self.results

    def create_update_appservicecertificateorders(self):
        '''
        Creates or updates AppServiceCertificateOrders with the specified configuration.

        :return: deserialized AppServiceCertificateOrders instance state dictionary
        '''
        self.log("Creating / Updating the AppServiceCertificateOrders instance {0}".format(self.certificate_order_name))

        try:
            response = self.mgmt_client.app_service_certificate_orders.create_or_update(resource_group_name=self.resource_group,
                                                                                        certificate_order_name=self.certificate_order_name,
                                                                                        certificate_distinguished_name=self.certificate_distinguished_name)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the AppServiceCertificateOrders instance.')
            self.fail("Error creating the AppServiceCertificateOrders instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_appservicecertificateorders(self):
        '''
        Deletes specified AppServiceCertificateOrders instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the AppServiceCertificateOrders instance {0}".format(self.certificate_order_name))
        try:
            response = self.mgmt_client.app_service_certificate_orders.delete(resource_group_name=self.resource_group,
                                                                              certificate_order_name=self.certificate_order_name)
        except CloudError as e:
            self.log('Error attempting to delete the AppServiceCertificateOrders instance.')
            self.fail("Error deleting the AppServiceCertificateOrders instance: {0}".format(str(e)))

        return True

    def get_appservicecertificateorders(self):
        '''
        Gets the properties of the specified AppServiceCertificateOrders.

        :return: deserialized AppServiceCertificateOrders instance state dictionary
        '''
        self.log("Checking if the AppServiceCertificateOrders instance {0} is present".format(self.certificate_order_name))
        found = False
        try:
            response = self.mgmt_client.app_service_certificate_orders.get(resource_group_name=self.resource_group,
                                                                           certificate_order_name=self.certificate_order_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceCertificateOrders instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceCertificateOrders instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMAppServiceCertificateOrders()

if __name__ == '__main__':
    main()
