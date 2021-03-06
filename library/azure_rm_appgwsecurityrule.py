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
module: azure_rm_appgwsecurityrule
version_added: "2.5"
short_description: Manage Security Rule instance.
description:
    - Create, update and delete instance of Security Rule.

options:
    resource_group:
        description:
            - C(*)TheC(*) C(*)nameC(*) C(*)ofC(*) C(*)theC(*) C(*)resourceC(*) C(*)groupC(*).
        required: True
    network_security_group_name:
        description:
            - C(*)TheC(*) C(*)nameC(*) C(*)ofC(*) C(*)theC(*) C(*)networkC(*) C(*)securityC(*) C(*)groupC(*).
        required: True
    security_rule_name:
        description:
            - C(*)TheC(*) C(*)nameC(*) C(*)ofC(*) C(*)theC(*) C(*)securityC(*) C(*)ruleC(*).
        required: True
    id:
        description:
            - C(*)ResourceC(*) C(*)IDC(*).
    description:
        description:
            - C(*)AC(*) C(*)descriptionC(*) C(*)forC(*) C(*)thisC(*) C(*)ruleC(*). C(*)RestrictedC(*) C(*)toC(*) C(*)140C(*) C(*)charsC(*).
    protocol:
        description:
            - "C(*)NetworkC(*) C(*)protocolC(*) C(*)thisC(*) C(*)ruleC(*) C(*)appliesC(*) C(*)toC(*). C(*)PossibleC(*) C(*)valuesC(*) C(*)areC(*)
               'C(*)CC(*)(C(*)tcpC(*))', 'C(*)CC(*)(C(*)udpC(*))', C(*)andC(*) '*'."
        required: True
        choices:
            - 'tcp'
            - 'udp'
            - '*'
    source_port_range:
        description:
            - "C(*)TheC(*) C(*)sourceC(*) C(*)portC(*) C(*)orC(*) C(*)rangeC(*). C(*)IntegerC(*) C(*)orC(*) C(*)rangeC(*) C(*)betweenC(*) C(*)0C(*)
               C(*)andC(*) C(*)65535C(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*)
               C(*)portsC(*)."
    destination_port_range:
        description:
            - "C(*)TheC(*) C(*)destinationC(*) C(*)portC(*) C(*)orC(*) C(*)rangeC(*). C(*)IntegerC(*) C(*)orC(*) C(*)rangeC(*) C(*)betweenC(*) C(*)0C(*)
               C(*)andC(*) C(*)65535C(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*)
               C(*)portsC(*)."
    source_address_prefix:
        description:
            - "C(*)TheC(*) C(*)CIDRC(*) C(*)orC(*) C(*)sourceC(*) C(*)IPC(*) C(*)rangeC(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*)
               C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*) C(*)IPsC(*). C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*)
               'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*) 'C(*)InternetC(*)' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*).
               C(*)IfC(*) C(*)thisC(*) C(*)isC(*) C(*)anC(*) C(*)ingressC(*) C(*)ruleC(*), C(*)specifiesC(*) C(*)whereC(*) C(*)networkC(*) C(*)trafficC(*)
               C(*)originatesC(*) C(*)fromC(*). "
    source_address_prefixes:
        description:
            - C(*)TheC(*) C(*)CIDRC(*) C(*)orC(*) C(*)sourceC(*) C(*)IPC(*) C(*)rangesC(*).
        type: list
    source_application_security_groups:
        description:
            - C(*)TheC(*) C(*)applicationC(*) C(*)securityC(*) C(*)groupC(*) C(*)specifiedC(*) C(*)asC(*) C(*)sourceC(*).
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            location:
                description:
                    - Resource location.
    destination_address_prefix:
        description:
            - "C(*)TheC(*) C(*)destinationC(*) C(*)addressC(*) C(*)prefixC(*). C(*)CIDRC(*) C(*)orC(*) C(*)destinationC(*) C(*)IPC(*) C(*)rangeC(*).
               C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*) C(*)IPsC(*).
               C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*) 'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*) 'C(*)InternetC(*)'
               C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*)."
    destination_address_prefixes:
        description:
            - C(*)TheC(*) C(*)destinationC(*) C(*)addressC(*) C(*)prefixesC(*). C(*)CIDRC(*) C(*)orC(*) C(*)destinationC(*) C(*)IPC(*) C(*)rangesC(*).
        type: list
    destination_application_security_groups:
        description:
            - C(*)TheC(*) C(*)applicationC(*) C(*)securityC(*) C(*)groupC(*) C(*)specifiedC(*) C(*)asC(*) C(*)destinationC(*).
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            location:
                description:
                    - Resource location.
    source_port_ranges:
        description:
            - C(*)TheC(*) C(*)sourceC(*) C(*)portC(*) C(*)rangesC(*).
        type: list
    destination_port_ranges:
        description:
            - C(*)TheC(*) C(*)destinationC(*) C(*)portC(*) C(*)rangesC(*).
        type: list
    access:
        description:
            - "C(*)TheC(*) C(*)networkC(*) C(*)trafficC(*) C(*)isC(*) C(*)allowedC(*) C(*)orC(*) C(*)deniedC(*). C(*)PossibleC(*) C(*)valuesC(*)
               C(*)areC(*): 'C(*)AllowC(*)' C(*)andC(*) 'C(*)DenyC(*)'."
        required: True
        choices:
            - 'allow'
            - 'deny'
    priority:
        description:
            - "C(*)TheC(*) C(*)priorityC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*). C(*)TheC(*) C(*)valueC(*) C(*)canC(*) C(*)beC(*) C(*)betweenC(*)
               C(*)100C(*) C(*)andC(*) C(*)4096C(*). C(*)TheC(*) C(*)priorityC(*) C(*)numberC(*) C(*)mustC(*) C(*)beC(*) C(*)uniqueC(*) C(*)forC(*)
               C(*)eachC(*) C(*)ruleC(*) C(*)inC(*) C(*)theC(*) C(*)collectionC(*). C(*)TheC(*) C(*)lowerC(*) C(*)theC(*) C(*)priorityC(*) C(*)numberC(*),
               C(*)theC(*) C(*)higherC(*) C(*)theC(*) C(*)priorityC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*)."
    direction:
        description:
            - "C(*)TheC(*) C(*)directionC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*). C(*)TheC(*) C(*)directionC(*) C(*)specifiesC(*) C(*)ifC(*) C(*)ruleC(*)
               C(*)willC(*) C(*)beC(*) C(*)evaluatedC(*) C(*)onC(*) C(*)incomingC(*) C(*)orC(*) C(*)outcomingC(*) C(*)trafficC(*). C(*)PossibleC(*)
               C(*)valuesC(*) C(*)areC(*): 'C(*)InboundC(*)' C(*)andC(*) 'C(*)OutboundC(*)'."
        required: True
        choices:
            - 'inbound'
            - 'outbound'
    provisioning_state:
        description:
            - "C(*)TheC(*) C(*)provisioningC(*) C(*)stateC(*) C(*)ofC(*) C(*)theC(*) C(*)publicC(*) C(*)IPC(*) C(*)resourceC(*). C(*)PossibleC(*)
               C(*)valuesC(*) C(*)areC(*): 'C(*)UpdatingC(*)', 'C(*)DeletingC(*)', C(*)andC(*) 'C(*)FailedC(*)'."
    name:
        description:
            - "C(*)TheC(*) C(*)nameC(*) C(*)ofC(*) C(*)theC(*) C(*)resourceC(*) C(*)thatC(*) C(*)isC(*) C(*)uniqueC(*) C(*)withinC(*) C(*)aC(*)
               C(*)resourceC(*) C(*)groupC(*). C(*)ThisC(*) C(*)nameC(*) C(*)canC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)IC(*)(C(*)accessC(*))
               C(*)theC(*) C(*)resourceC(*)."
    etag:
        description:
            - "C(*)AC(*) C(*)uniqueC(*) C(*)readC(*)-C(*)onlyC(*) C(*)stringC(*) C(*)thatC(*) C(*)changesC(*) C(*)wheneverC(*) C(*)theC(*) C(*)resourceC(*)
               C(*)isC(*) C(*)updatedC(*)."
    state:
      description:
        - Assert the state of the Security Rule.
        - Use 'present' to create or update an Security Rule and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Security Rule
    azure_rm_appgwsecurityrule:
      resource_group: rg1
      network_security_group_name: testnsg
      security_rule_name: rule1
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/securityRules/rule1
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSecurityRules(AzureRMModuleBase):
    """Configuration class for an Azure RM Security Rule resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_security_group_name=dict(
                type='str',
                required=True
            ),
            security_rule_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            description=dict(
                type='str'
            ),
            protocol=dict(
                type='str',
                choices=['tcp',
                         'udp',
                         '*'],
                required=True
            ),
            source_port_range=dict(
                type='str'
            ),
            destination_port_range=dict(
                type='str'
            ),
            source_address_prefix=dict(
                type='str'
            ),
            source_address_prefixes=dict(
                type='list'
            ),
            source_application_security_groups=dict(
                type='list'
            ),
            destination_address_prefix=dict(
                type='str'
            ),
            destination_address_prefixes=dict(
                type='list'
            ),
            destination_application_security_groups=dict(
                type='list'
            ),
            source_port_ranges=dict(
                type='list'
            ),
            destination_port_ranges=dict(
                type='list'
            ),
            access=dict(
                type='str',
                choices=['allow',
                         'deny'],
                required=True
            ),
            priority=dict(
                type='int'
            ),
            direction=dict(
                type='str',
                choices=['inbound',
                         'outbound'],
                required=True
            ),
            provisioning_state=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            etag=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.network_security_group_name = None
        self.security_rule_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSecurityRules, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "description":
                    self.parameters["description"] = kwargs[key]
                elif key == "protocol":
                    self.parameters["protocol"] = _snake_to_camel(kwargs[key], True)
                elif key == "source_port_range":
                    self.parameters["source_port_range"] = kwargs[key]
                elif key == "destination_port_range":
                    self.parameters["destination_port_range"] = kwargs[key]
                elif key == "source_address_prefix":
                    self.parameters["source_address_prefix"] = kwargs[key]
                elif key == "source_address_prefixes":
                    self.parameters["source_address_prefixes"] = kwargs[key]
                elif key == "source_application_security_groups":
                    self.parameters["source_application_security_groups"] = kwargs[key]
                elif key == "destination_address_prefix":
                    self.parameters["destination_address_prefix"] = kwargs[key]
                elif key == "destination_address_prefixes":
                    self.parameters["destination_address_prefixes"] = kwargs[key]
                elif key == "destination_application_security_groups":
                    self.parameters["destination_application_security_groups"] = kwargs[key]
                elif key == "source_port_ranges":
                    self.parameters["source_port_ranges"] = kwargs[key]
                elif key == "destination_port_ranges":
                    self.parameters["destination_port_ranges"] = kwargs[key]
                elif key == "access":
                    self.parameters["access"] = _snake_to_camel(kwargs[key], True)
                elif key == "priority":
                    self.parameters["priority"] = kwargs[key]
                elif key == "direction":
                    self.parameters["direction"] = _snake_to_camel(kwargs[key], True)
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "name":
                    self.parameters["name"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_securityrule()

        if not old_response:
            self.log("Security Rule instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Security Rule instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Security Rule instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Security Rule instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_securityrule()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Security Rule instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_securityrule()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_securityrule():
                time.sleep(20)
        else:
            self.log("Security Rule instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_securityrule(self):
        '''
        Creates or updates Security Rule with the specified configuration.

        :return: deserialized Security Rule instance state dictionary
        '''
        self.log("Creating / Updating the Security Rule instance {0}".format(self.security_rule_name))

        try:
            response = self.mgmt_client.security_rules.create_or_update(resource_group_name=self.resource_group,
                                                                        network_security_group_name=self.network_security_group_name,
                                                                        security_rule_name=self.security_rule_name,
                                                                        security_rule_parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Security Rule instance.')
            self.fail("Error creating the Security Rule instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_securityrule(self):
        '''
        Deletes specified Security Rule instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Security Rule instance {0}".format(self.security_rule_name))
        try:
            response = self.mgmt_client.security_rules.delete(resource_group_name=self.resource_group,
                                                              network_security_group_name=self.network_security_group_name,
                                                              security_rule_name=self.security_rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the Security Rule instance.')
            self.fail("Error deleting the Security Rule instance: {0}".format(str(e)))

        return True

    def get_securityrule(self):
        '''
        Gets the properties of the specified Security Rule.

        :return: deserialized Security Rule instance state dictionary
        '''
        self.log("Checking if the Security Rule instance {0} is present".format(self.security_rule_name))
        found = False
        try:
            response = self.mgmt_client.security_rules.get(resource_group_name=self.resource_group,
                                                           network_security_group_name=self.network_security_group_name,
                                                           security_rule_name=self.security_rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Security Rule instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Security Rule instance.')
        if found is True:
            return response.as_dict()

        return False


def _snake_to_camel(snake, capitalize_first=False):
    if capitalize_first:
        return ''.join(x.capitalize() or '_' for x in snake.split('_'))
    else:
        return snake.split('_')[0] + ''.join(x.capitalize() or '_' for x in snake.split('_')[1:])


def main():
    """Main execution"""
    AzureRMSecurityRules()

if __name__ == '__main__':
    main()
