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
module: azure_rm_sqlelasticpool
version_added: "2.5"
short_description: Manage ElasticPool instance
description:
    - Create, update and delete instance of ElasticPool

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    name:
        description:
            - The name of the elastic pool to be operated on (updated or created).
        required: True
    location:
        description:
            - Resource location.
    edition:
        description:
            - "The edition of the elastic pool. Possible values include: 'Basic', 'Standard', 'Premium'"
    dtu:
        description:
            - The total shared DTU for the database elastic pool.
    database_dtu_max:
        description:
            - The maximum DTU any one database can consume.
    database_dtu_min:
        description:
            - The minimum DTU all databases are guaranteed.
    storage_mb:
        description:
            - Gets storage limit for the database elastic pool in MB.
    zone_redundant:
        description:
            - "Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availabi
               lity zones."

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) ElasticPool
    azure_rm_sqlelasticpool:
      resource_group: resource_group_name
      server_name: server_name
      name: elastic_pool_name
      location: location
      edition: edition
      dtu: dtu
      database_dtu_max: database_dtu_max
      database_dtu_min: database_dtu_min
      storage_mb: storage_mb
      zone_redundant: zone_redundant
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
state:
    description:
        - "The state of the elastic pool. Possible values include: 'Creating', 'Ready', 'Disabled'"
    returned: always
    type: str
    sample: state
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMElasticPools(AzureRMModuleBase):
    """Configuration class for an Azure RM ElasticPool resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                required=False
            ),
            edition=dict(
                type='str',
                required=False
            ),
            dtu=dict(
                type='int',
                required=False
            ),
            database_dtu_max=dict(
                type='int',
                required=False
            ),
            database_dtu_min=dict(
                type='int',
                required=False
            ),
            storage_mb=dict(
                type='int',
                required=False
            ),
            zone_redundant=dict(
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
        self.server_name = None
        self.name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMElasticPools, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif key == "location" and kwargs[key] is not None:
                self.parameters.update({"location": kwargs[key]})
            elif key == "edition" and kwargs[key] is not None:
                self.parameters.update({"edition": kwargs[key]})
            elif key == "dtu" and kwargs[key] is not None:
                self.parameters.update({"dtu": kwargs[key]})
            elif key == "database_dtu_max" and kwargs[key] is not None:
                self.parameters.update({"database_dtu_max": kwargs[key]})
            elif key == "database_dtu_min" and kwargs[key] is not None:
                self.parameters.update({"database_dtu_min": kwargs[key]})
            elif key == "storage_mb" and kwargs[key] is not None:
                self.parameters.update({"storage_mb": kwargs[key]})
            elif key == "zone_redundant" and kwargs[key] is not None:
                self.parameters.update({"zone_redundant": kwargs[key]})

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_elasticpool()

        if not old_response:
            self.log("ElasticPool instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ElasticPool instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ElasticPool instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ElasticPool instance")

            if self.check_mode:
                return self.results

            response = self.create_update_elasticpool()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)

            # remove unnecessary fields from return state
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ElasticPool instance deleted")
            self.delete_elasticpool()
            self.results['changed'] = True
        else:
            self.log("ElasticPool instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_elasticpool(self):
        '''
        Creates or updates ElasticPool with the specified configuration.

        :return: deserialized ElasticPool instance state dictionary
        '''
        self.log("Creating / Updating the ElasticPool instance {0}".format(self.name))

        try:
            response = self.mgmt_client.elastic_pools.create_or_update(self.resource_group,
                                                                       self.server_name,
                                                                       self.name,
                                                                       self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ElasticPool instance.')
            self.fail("Error creating the ElasticPool instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_elasticpool(self):
        '''
        Deletes specified ElasticPool instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ElasticPool instance {0}".format(self.name))
        try:
            response = self.mgmt_client.elastic_pools.delete(self.resource_group,
                                                             self.server_name,
                                                             self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ElasticPool instance.')
            self.fail("Error deleting the ElasticPool instance: {0}".format(str(e)))

        return True

    def get_elasticpool(self):
        '''
        Gets the properties of the specified ElasticPool.

        :return: deserialized ElasticPool instance state dictionary
        '''
        self.log("Checking if the ElasticPool instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.elastic_pools.get(self.resource_group,
                                                          self.server_name,
                                                          self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ElasticPool instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ElasticPool instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMElasticPools()

if __name__ == '__main__':
    main()
