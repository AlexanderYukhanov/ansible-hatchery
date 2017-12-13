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
module: azure_rm_webcertificate
version_added: "2.5"
short_description: Manage Certificates instance
description:
    - Create, update and delete instance of Certificates

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of the certificate.
        required: True
    kind:
        description:
            - Kind of resource.
    location:
        description:
            - Resource Location.
    host_names:
        description:
            - Host names the certificate applies to.
    pfx_blob:
        description:
            - Pfx blob.
    password:
        description:
            - Certificate password.
    key_vault_id:
        description:
            - Key Vault Csm resource Id.
    key_vault_secret_name:
        description:
            - Key Vault secret name.
    server_farm_id:
        description:
            - "Resource ID of the associated App Service plan, formatted as: '/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.
               Web/serverfarms/{appServicePlanName}'."

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Certificates
    azure_rm_webcertificate:
      resource_group: resource_group_name
      name: name
      kind: kind
      location: location
      host_names:
        - XXXX - list of values -- not implemented str
      pfx_blob: pfx_blob
      password: password
      key_vault_id: key_vault_id
      key_vault_secret_name: key_vault_secret_name
      server_farm_id: server_farm_id
'''

RETURN = '''
id:
    description:
        - Resource Id.
    returned: always
    type: str
    sample: id
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


class AzureRMCertificates(AzureRMModuleBase):
    """Configuration class for an Azure RM Certificates resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='str',
                required=False
            ),
            location=dict(
                type='str',
                required=False
            ),
            host_names=dict(
                type='list',
                required=False
            ),
            pfx_blob=dict(
                type='str',
                required=False
            ),
            password=dict(
                type='str',
                no_log=True,
                required=False
            ),
            key_vault_id=dict(
                type='str',
                required=False
            ),
            key_vault_secret_name=dict(
                type='str',
                required=False
            ),
            server_farm_id=dict(
                type='str',
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
        self.name = None
        self.certificate_envelope = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCertificates, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "kind":
                    self.certificate_envelope.update({"kind": kwargs[key]})
                elif key == "location":
                    self.certificate_envelope.update({"location": kwargs[key]})
                elif key == "host_names":
                    self.certificate_envelope.update({"host_names": kwargs[key]})
                elif key == "pfx_blob":
                    self.certificate_envelope.update({"pfx_blob": kwargs[key]})
                elif key == "password":
                    self.certificate_envelope.update({"password": kwargs[key]})
                elif key == "key_vault_id":
                    self.certificate_envelope.update({"key_vault_id": kwargs[key]})
                elif key == "key_vault_secret_name":
                    self.certificate_envelope.update({"key_vault_secret_name": kwargs[key]})
                elif key == "server_farm_id":
                    self.certificate_envelope.update({"server_farm_id": kwargs[key]})

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_certificates()

        if not old_response:
            self.log("Certificates instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Certificates instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Certificates instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Certificates instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_certificates()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Certificates instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_certificates()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_certificates():
                time.sleep(20)
        else:
            self.log("Certificates instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_certificates(self):
        '''
        Creates or updates Certificates with the specified configuration.

        :return: deserialized Certificates instance state dictionary
        '''
        self.log("Creating / Updating the Certificates instance {0}".format(self.name))

        try:
            response = self.mgmt_client.certificates.create_or_update(self.resource_group,
                                                                      self.name,
                                                                      self.certificate_envelope)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Certificates instance.')
            self.fail("Error creating the Certificates instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_certificates(self):
        '''
        Deletes specified Certificates instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Certificates instance {0}".format(self.name))
        try:
            response = self.mgmt_client.certificates.delete(self.resource_group,
                                                            self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Certificates instance.')
            self.fail("Error deleting the Certificates instance: {0}".format(str(e)))

        return True

    def get_certificates(self):
        '''
        Gets the properties of the specified Certificates.

        :return: deserialized Certificates instance state dictionary
        '''
        self.log("Checking if the Certificates instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.certificates.get(self.resource_group,
                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Certificates instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Certificates instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMCertificates()

if __name__ == '__main__':
    main()
