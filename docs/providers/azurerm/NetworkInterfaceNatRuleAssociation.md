# Terraform::AzureRM::NetworkInterfaceNatRuleAssociation

Manages the association between a Network Interface and a Load Balancer's NAT Rule.

## Properties

`NetworkInterfaceId` - (Required) The ID of the Network Interface. Changing this forces a new resource to be created.

`IpConfigurationName` - (Required) The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.

`NatRuleId` - (Required) The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The (Terraform specific) ID of the Association between the Network Interface and the Load Balancers NAT Rule.

## See Also

* [azurerm_network_interface_nat_rule_association](https://www.terraform.io/docs/providers/azurerm/r/network_interface_nat_rule_association.html) in the _Terraform Provider Documentation_