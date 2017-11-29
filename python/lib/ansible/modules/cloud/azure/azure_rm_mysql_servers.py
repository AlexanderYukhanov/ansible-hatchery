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
module: azure_rm_mysql_servers
version_added: "2.5"
short_description: Manage Servers instance
description:
    - Create, update and delete instance of Servers

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    name:
        description:
            - The name of the server.
        required: True
    sku:
        description:
            - The SKU (pricing tier) of the server.
        suboptions:
            name:
                description:
                    - The name of the sku, typically, a letter + Number code, e.g. P3.
            tier:
                description:
                    - "The tier of the particular SKU, e.g. Basic. Possible values include: 'Basic', 'Standard'"
            capacity:
                description:
                    - "The scale up/out capacity, representing server's compute units."
            size:
                description:
                    - The size code, to be interpreted by resource as appropriate.
            family:
                description:
                    - The family of hardware.
    properties:
        description:
            - Properties of the server.
        required: True
        suboptions:
            storage_mb:
                description:
                    - The maximum storage allowed for a server.
            version:
                description:
                    - "Server version. Possible values include: '5.6', '5.7'"
            ssl_enforcement:
                description:
                    - "Enable ssl enforcement or not when connect to server. Possible values include: 'Enabled', 'Disabled'"
            create_mode:
                description:
                    - Constant filled by server.
                required: True
            admin_username:
                description:
                    - "The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation)."
                required: True
            admin_password:
                description:
                    - The password of the administrator login.
                required: True
    location:
        description:
            - The location the resource resides in.
        required: True
    tags:
        description:
            - Application-specific metadata in the form of key-value pairs.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Servers
    azure_rm_mysql_servers:
      resource_group: {{ resource_group }}
      name: test-mysql-server
      sku:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: "{{ capacity }}"
        size: "{{ size }}"
        family: "{{ family }}"
      properties:
        storage_mb: "{{ storage_mb }}"
        version: 5.6
        ssl_enforcement: "{{ ssl_enforcement }}"
        create_mode: Default
        admin_username: zimxyz
        admin_password: Testpasswordxyz12!
      location: westus
      tags: "{{ tags }}"
'''

RETURN = '''
state:
    description: Current state of Servers
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID
            returned: always
            type: str
            sample: id
        name:
            description:
                - Resource name.
            returned: always
            type: str
            sample: name
        type:
            description:
                - Resource type.
            returned: always
            type: str
            sample: type
        location:
            description:
                - The location the resource resides in.
            returned: always
            type: str
            sample: location
        tags:
            description:
                - Application-specific metadata in the form of key-value pairs.
            returned: always
            type: complex
            sample: tags
        sku:
            description:
                - The SKU (pricing tier) of the server.
            returned: always
            type: complex
            sample: sku
            suboptions:
                name:
                    description:
                        - The name of the sku, typically, a letter + Number code, e.g. P3.
                    returned: always
                    type: str
                    sample: name
                tier:
                    description:
                        - "The tier of the particular SKU, e.g. Basic. Possible values include: 'Basic', 'Standard'"
                    returned: always
                    type: str
                    sample: tier
                capacity:
                    description:
                        - "The scale up/out capacity, representing server's compute units."
                    returned: always
                    type: int
                    sample: capacity
                size:
                    description:
                        - The size code, to be interpreted by resource as appropriate.
                    returned: always
                    type: str
                    sample: size
                family:
                    description:
                        - The family of hardware.
                    returned: always
                    type: str
                    sample: family
        administrator_login:
            description:
                - "The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation)."
            returned: always
            type: str
            sample: administrator_login
        storage_mb:
            description:
                - The maximum storage allowed for a server.
            returned: always
            type: long
            sample: storage_mb
        version:
            description:
                - "Server version. Possible values include: '5.6', '5.7'"
            returned: always
            type: str
            sample: version
        ssl_enforcement:
            description:
                - "Enable ssl enforcement or not when connect to server. Possible values include: 'Enabled', 'Disabled'"
            returned: always
            type: str
            sample: ssl_enforcement
        user_visible_state:
            description:
                - "A state of a server that is visible to user. Possible values include: 'Ready', 'Dropping', 'Disabled'"
            returned: always
            type: str
            sample: user_visible_state
        fully_qualified_domain_name:
            description:
                - The fully qualified domain name of a server.
            returned: always
            type: str
            sample: fully_qualified_domain_name
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.rdbms.mysql import MySQLManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServers(AzureRMModuleBase):
    """Configuration class for an Azure RM Servers resource"""

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
            sku=dict(
                type='dict',
                required=False
            ),
            properties=dict(
                type='dict',
                required=True
            ),
            location=dict(
                type='str',
                required=True
            ),
            tags=dict(
                type='dict',
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
        self.parameters = dict()

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None

        super(AzureRMServers, self).__init__(derived_arg_spec=self.module_arg_spec,
                                             supports_check_mode=True,
                                             supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif key == "sku":
                self.parameters["sku"] = kwargs[key]
            elif key == "properties":
                self.parameters["properties"] = kwargs[key]
            elif key == "location":
                self.parameters["location"] = kwargs[key]
            elif key == "tags":
                self.parameters["tags"] = kwargs[key]

        self.adjust_parameters()

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_servers()

        if not old_response:
            self.log("Servers instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
        else:
            self.log("Servers instance already exists")
            if self.state == 'absent':
                self.delete_servers()
                self.results['changed'] = True
                self.log("Servers instance deleted")
            elif self.state == 'present':
                self.log("Need to check if Servers instance has to be deleted or may be updated")

        if self.state == 'present':

            self.log("Need to Create / Update the Servers instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_servers()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = (cmp(old_response, self.results['state']) != 0)

            self.log("Creation / Update done")

        return self.results

    def adjust_parameters(self):
        if self.parameters.has_key('properties'):
          rename_key(self.parameters['properties'], administrator_login, admin_username)
          rename_key(self.parameters['properties'], administrator_login_password, admin_password)

    def rename_key(d, old_name, new_name):
        old_value = dict.get(old_name, None)
        if old_value is not None:
            dict.pop(old_name, None)
            dict[new_name] = old_value;

    def create_update_servers(self):
        '''
        Creates or updates Servers with the specified configuration.

        :return: deserialized Servers instance state dictionary
        '''
        self.log("Creating / Updating the Servers instance {0}".format(self.name))

        try:
            response = self.mgmt_client.servers.create_or_update(self.resource_group,
                                                                 self.name,
                                                                 self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Servers instance.')
            self.fail("Error creating the Servers instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_servers(self):
        '''
        Deletes specified Servers instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Servers instance {0}".format(self.name))
        try:
            response = self.mgmt_client.servers.delete(self.resource_group,
                                                       self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Servers instance.')
            self.fail("Error deleting the Servers instance: {0}".format(str(e)))

        return True

    def get_servers(self):
        '''
        Gets the properties of the specified Servers.

        :return: deserialized Servers instance state dictionary
        '''
        self.log("Checking if the Servers instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.servers.get(self.resource_group,
                                                    self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Servers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Servers instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMServers()

if __name__ == '__main__':
    main()
