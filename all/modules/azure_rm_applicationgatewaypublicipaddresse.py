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
module: azure_rm_applicationgatewaypublicipaddresse
version_added: "2.5"
short_description: Manage PublicIPAddresses instance
description:
    - Create, update and delete instance of PublicIPAddresses

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    public_ip_address_name:
        description:
            - The name of the public IP address.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    sku:
        description:
            - The public IP address SKU.
        suboptions:
            name:
                description:
                    - "Name of a public IP address SKU. Possible values include: 'Basic', 'Standard'"
    public_ip_allocation_method:
        description:
            - "The public IP allocation method. Possible values are: 'Static' and 'Dynamic'. Possible values include: 'Static', 'Dynamic'"
    public_ip_address_version:
        description:
            - "The public IP address version. Possible values are: 'IPv4' and 'IPv6'. Possible values include: 'IPv4', 'IPv6'"
    dns_settings:
        description:
            - The FQDN of the DNS record associated with the public IP address.
        suboptions:
            domain_name_label:
                description:
                    - "Gets or sets the Domain name label.The concatenation of the domain name label and the regionalized DNS zone make up the fully qualifie
                       d domain name associated with the public IP address. If a domain name label is specified, an A DNS record is created for the public IP
                        in the Microsoft Azure DNS system."
            fqdn:
                description:
                    - "Gets the FQDN, Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainN
                       ameLabel and the regionalized DNS zone."
            reverse_fqdn:
                description:
                    - "Gets or Sets the Reverse FQDN. A user-visible, fully qualified domain name that resolves to this public IP address. If the reverseFqdn
                        is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN. "
    ip_address:
        description:
            - The IP address associated with the public IP address resource.
    idle_timeout_in_minutes:
        description:
            - The idle timeout of the public IP address.
    resource_guid:
        description:
            - The resource GUID property of the public IP resource.
    provisioning_state:
        description:
            - "The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
    etag:
        description:
            - A unique read-only string that changes whenever the resource is updated.
    zones:
        description:
            - A list of availability zones denoting the IP allocated for the resource needs to come from.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) PublicIPAddresses
    azure_rm_applicationgatewaypublicipaddresse:
      resource_group: resource_group_name
      public_ip_address_name: public_ip_address_name
      id: id
      location: location
      sku:
        name: name
      public_ip_allocation_method: public_ip_allocation_method
      public_ip_address_version: public_ip_address_version
      dns_settings:
        domain_name_label: domain_name_label
        fqdn: fqdn
        reverse_fqdn: reverse_fqdn
      ip_address: ip_address
      idle_timeout_in_minutes: idle_timeout_in_minutes
      resource_guid: resource_guid
      provisioning_state: provisioning_state
      etag: etag
      zones:
        - XXXX - list of values -- not implemented str
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPublicIPAddresses(AzureRMModuleBase):
    """Configuration class for an Azure RM PublicIPAddresses resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            public_ip_address_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            location=dict(
                type='str',
                required=False
            ),
            sku=dict(
                type='dict',
                required=False
            ),
            public_ip_allocation_method=dict(
                type='str',
                required=False
            ),
            public_ip_address_version=dict(
                type='str',
                required=False
            ),
            dns_settings=dict(
                type='dict',
                required=False
            ),
            ip_address=dict(
                type='str',
                required=False
            ),
            idle_timeout_in_minutes=dict(
                type='int',
                required=False
            ),
            resource_guid=dict(
                type='str',
                required=False
            ),
            provisioning_state=dict(
                type='str',
                required=False
            ),
            etag=dict(
                type='str',
                required=False
            ),
            zones=dict(
                type='list',
                required=False
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.public_ip_address_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPublicIPAddresses, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                       supports_check_mode=True,
                                                       supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "sku":
                    self.parameters["sku"] = kwargs[key]
                elif key == "public_ip_allocation_method":
                    self.parameters["public_ip_allocation_method"] = kwargs[key]
                elif key == "public_ip_address_version":
                    self.parameters["public_ip_address_version"] = kwargs[key]
                elif key == "dns_settings":
                    self.parameters["dns_settings"] = kwargs[key]
                elif key == "ip_address":
                    self.parameters["ip_address"] = kwargs[key]
                elif key == "idle_timeout_in_minutes":
                    self.parameters["idle_timeout_in_minutes"] = kwargs[key]
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]
                elif key == "zones":
                    self.parameters["zones"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_publicipaddresses()

        if not old_response:
            self.log("PublicIPAddresses instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("PublicIPAddresses instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if PublicIPAddresses instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the PublicIPAddresses instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_publicipaddresses()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("PublicIPAddresses instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_publicipaddresses()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_publicipaddresses():
                time.sleep(20)
        else:
            self.log("PublicIPAddresses instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_publicipaddresses(self):
        '''
        Creates or updates PublicIPAddresses with the specified configuration.

        :return: deserialized PublicIPAddresses instance state dictionary
        '''
        self.log("Creating / Updating the PublicIPAddresses instance {0}".format(self.public_ip_address_name))

        try:
            response = self.mgmt_client.public_ip_addresses.create_or_update(self.resource_group,
                                                                             self.public_ip_address_name,
                                                                             self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the PublicIPAddresses instance.')
            self.fail("Error creating the PublicIPAddresses instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_publicipaddresses(self):
        '''
        Deletes specified PublicIPAddresses instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the PublicIPAddresses instance {0}".format(self.public_ip_address_name))
        try:
            response = self.mgmt_client.public_ip_addresses.delete(self.resource_group,
                                                                   self.public_ip_address_name)
        except CloudError as e:
            self.log('Error attempting to delete the PublicIPAddresses instance.')
            self.fail("Error deleting the PublicIPAddresses instance: {0}".format(str(e)))

        return True

    def get_publicipaddresses(self):
        '''
        Gets the properties of the specified PublicIPAddresses.

        :return: deserialized PublicIPAddresses instance state dictionary
        '''
        self.log("Checking if the PublicIPAddresses instance {0} is present".format(self.public_ip_address_name))
        found = False
        try:
            response = self.mgmt_client.public_ip_addresses.get(self.resource_group,
                                                                self.public_ip_address_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("PublicIPAddresses instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the PublicIPAddresses instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMPublicIPAddresses()

if __name__ == '__main__':
    main()