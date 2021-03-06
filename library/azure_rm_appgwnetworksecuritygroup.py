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
module: azure_rm_appgwnetworksecuritygroup
version_added: "2.5"
short_description: Manage Network Security Group instance.
description:
    - Create, update and delete instance of Network Security Group.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_security_group_name:
        description:
            - The name of the network security group.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    security_rules:
        description:
            - A collection of security rules of the network security group.
        type: list
        suboptions:
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
                    - "C(*)TheC(*) C(*)destinationC(*) C(*)portC(*) C(*)orC(*) C(*)rangeC(*). C(*)IntegerC(*) C(*)orC(*) C(*)rangeC(*) C(*)betweenC(*)
                       C(*)0C(*) C(*)andC(*) C(*)65535C(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*)
                       C(*)allC(*) C(*)portsC(*)."
            source_address_prefix:
                description:
                    - "C(*)TheC(*) C(*)CIDRC(*) C(*)orC(*) C(*)sourceC(*) C(*)IPC(*) C(*)rangeC(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*)
                       C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*) C(*)IPsC(*). C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*)
                       'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*) 'C(*)InternetC(*)' C(*)canC(*) C(*)alsoC(*) C(*)beC(*)
                       C(*)usedC(*). C(*)IfC(*) C(*)thisC(*) C(*)isC(*) C(*)anC(*) C(*)ingressC(*) C(*)ruleC(*), C(*)specifiesC(*) C(*)whereC(*)
                       C(*)networkC(*) C(*)trafficC(*) C(*)originatesC(*) C(*)fromC(*). "
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
                       C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*)
                       C(*)IPsC(*). C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*) 'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*)
                       'C(*)InternetC(*)' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*)."
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
                       C(*)eachC(*) C(*)ruleC(*) C(*)inC(*) C(*)theC(*) C(*)collectionC(*). C(*)TheC(*) C(*)lowerC(*) C(*)theC(*) C(*)priorityC(*)
                       C(*)numberC(*), C(*)theC(*) C(*)higherC(*) C(*)theC(*) C(*)priorityC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*)."
            direction:
                description:
                    - "C(*)TheC(*) C(*)directionC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*). C(*)TheC(*) C(*)directionC(*) C(*)specifiesC(*) C(*)ifC(*)
                       C(*)ruleC(*) C(*)willC(*) C(*)beC(*) C(*)evaluatedC(*) C(*)onC(*) C(*)incomingC(*) C(*)orC(*) C(*)outcomingC(*) C(*)trafficC(*).
                       C(*)PossibleC(*) C(*)valuesC(*) C(*)areC(*): 'C(*)InboundC(*)' C(*)andC(*) 'C(*)OutboundC(*)'."
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
                    - "C(*)AC(*) C(*)uniqueC(*) C(*)readC(*)-C(*)onlyC(*) C(*)stringC(*) C(*)thatC(*) C(*)changesC(*) C(*)wheneverC(*) C(*)theC(*)
                       C(*)resourceC(*) C(*)isC(*) C(*)updatedC(*)."
    default_security_rules:
        description:
            - The default security rules of network security group.
        type: list
        suboptions:
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
                    - "C(*)TheC(*) C(*)destinationC(*) C(*)portC(*) C(*)orC(*) C(*)rangeC(*). C(*)IntegerC(*) C(*)orC(*) C(*)rangeC(*) C(*)betweenC(*)
                       C(*)0C(*) C(*)andC(*) C(*)65535C(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*)
                       C(*)allC(*) C(*)portsC(*)."
            source_address_prefix:
                description:
                    - "C(*)TheC(*) C(*)CIDRC(*) C(*)orC(*) C(*)sourceC(*) C(*)IPC(*) C(*)rangeC(*). C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*)
                       C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*) C(*)IPsC(*). C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*)
                       'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*) 'C(*)InternetC(*)' C(*)canC(*) C(*)alsoC(*) C(*)beC(*)
                       C(*)usedC(*). C(*)IfC(*) C(*)thisC(*) C(*)isC(*) C(*)anC(*) C(*)ingressC(*) C(*)ruleC(*), C(*)specifiesC(*) C(*)whereC(*)
                       C(*)networkC(*) C(*)trafficC(*) C(*)originatesC(*) C(*)fromC(*). "
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
                       C(*)AsterixC(*) '*' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*) C(*)toC(*) C(*)matchC(*) C(*)allC(*) C(*)sourceC(*)
                       C(*)IPsC(*). C(*)DefaultC(*) C(*)tagsC(*) C(*)suchC(*) C(*)asC(*) 'C(*)VirtualNetworkC(*)', 'C(*)AzureLoadBalancerC(*)' C(*)andC(*)
                       'C(*)InternetC(*)' C(*)canC(*) C(*)alsoC(*) C(*)beC(*) C(*)usedC(*)."
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
                       C(*)eachC(*) C(*)ruleC(*) C(*)inC(*) C(*)theC(*) C(*)collectionC(*). C(*)TheC(*) C(*)lowerC(*) C(*)theC(*) C(*)priorityC(*)
                       C(*)numberC(*), C(*)theC(*) C(*)higherC(*) C(*)theC(*) C(*)priorityC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*)."
            direction:
                description:
                    - "C(*)TheC(*) C(*)directionC(*) C(*)ofC(*) C(*)theC(*) C(*)ruleC(*). C(*)TheC(*) C(*)directionC(*) C(*)specifiesC(*) C(*)ifC(*)
                       C(*)ruleC(*) C(*)willC(*) C(*)beC(*) C(*)evaluatedC(*) C(*)onC(*) C(*)incomingC(*) C(*)orC(*) C(*)outcomingC(*) C(*)trafficC(*).
                       C(*)PossibleC(*) C(*)valuesC(*) C(*)areC(*): 'C(*)InboundC(*)' C(*)andC(*) 'C(*)OutboundC(*)'."
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
                    - "C(*)AC(*) C(*)uniqueC(*) C(*)readC(*)-C(*)onlyC(*) C(*)stringC(*) C(*)thatC(*) C(*)changesC(*) C(*)wheneverC(*) C(*)theC(*)
                       C(*)resourceC(*) C(*)isC(*) C(*)updatedC(*)."
    resource_guid:
        description:
            - The resource GUID property of the network security group resource.
    provisioning_state:
        description:
            - "The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
    etag:
        description:
            - A unique read-only string that changes whenever the resource is updated.
    state:
      description:
        - Assert the state of the Network Security Group.
        - Use 'present' to create or update an Network Security Group and 'absent' to delete it.
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
  - name: Create (or update) Network Security Group
    azure_rm_appgwnetworksecuritygroup:
      resource_group: rg1
      network_security_group_name: testnsg
      location: eastus
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg
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


class AzureRMNetworkSecurityGroups(AzureRMModuleBase):
    """Configuration class for an Azure RM Network Security Group resource"""

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
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            security_rules=dict(
                type='list'
            ),
            default_security_rules=dict(
                type='list'
            ),
            resource_guid=dict(
                type='str'
            ),
            provisioning_state=dict(
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
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetworkSecurityGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "security_rules":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                        elif ev['protocol'] == 'udp':
                            ev['protocol'] = 'Udp'
                    if 'access' in ev:
                        if ev['access'] == 'allow':
                            ev['access'] = 'Allow'
                        elif ev['access'] == 'deny':
                            ev['access'] = 'Deny'
                    if 'direction' in ev:
                        if ev['direction'] == 'inbound':
                            ev['direction'] = 'Inbound'
                        elif ev['direction'] == 'outbound':
                            ev['direction'] = 'Outbound'
                    self.parameters["security_rules"] = ev
                elif key == "default_security_rules":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                        elif ev['protocol'] == 'udp':
                            ev['protocol'] = 'Udp'
                    if 'access' in ev:
                        if ev['access'] == 'allow':
                            ev['access'] = 'Allow'
                        elif ev['access'] == 'deny':
                            ev['access'] = 'Deny'
                    if 'direction' in ev:
                        if ev['direction'] == 'inbound':
                            ev['direction'] = 'Inbound'
                        elif ev['direction'] == 'outbound':
                            ev['direction'] = 'Outbound'
                    self.parameters["default_security_rules"] = ev
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_networksecuritygroup()

        if not old_response:
            self.log("Network Security Group instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Network Security Group instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Network Security Group instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Network Security Group instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_networksecuritygroup()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Network Security Group instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_networksecuritygroup()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_networksecuritygroup():
                time.sleep(20)
        else:
            self.log("Network Security Group instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_networksecuritygroup(self):
        '''
        Creates or updates Network Security Group with the specified configuration.

        :return: deserialized Network Security Group instance state dictionary
        '''
        self.log("Creating / Updating the Network Security Group instance {0}".format(self.network_security_group_name))

        try:
            response = self.mgmt_client.network_security_groups.create_or_update(resource_group_name=self.resource_group,
                                                                                 network_security_group_name=self.network_security_group_name,
                                                                                 parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Network Security Group instance.')
            self.fail("Error creating the Network Security Group instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_networksecuritygroup(self):
        '''
        Deletes specified Network Security Group instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Network Security Group instance {0}".format(self.network_security_group_name))
        try:
            response = self.mgmt_client.network_security_groups.delete(resource_group_name=self.resource_group,
                                                                       network_security_group_name=self.network_security_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Network Security Group instance.')
            self.fail("Error deleting the Network Security Group instance: {0}".format(str(e)))

        return True

    def get_networksecuritygroup(self):
        '''
        Gets the properties of the specified Network Security Group.

        :return: deserialized Network Security Group instance state dictionary
        '''
        self.log("Checking if the Network Security Group instance {0} is present".format(self.network_security_group_name))
        found = False
        try:
            response = self.mgmt_client.network_security_groups.get(resource_group_name=self.resource_group,
                                                                    network_security_group_name=self.network_security_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Network Security Group instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Network Security Group instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMNetworkSecurityGroups()

if __name__ == '__main__':
    main()
