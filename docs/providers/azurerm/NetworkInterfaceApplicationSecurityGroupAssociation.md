# Terraform::AzureRM::NetworkInterfaceApplicationSecurityGroupAssociation

Manages the association between a Network Interface and a Application Security Group.

## Properties

`NetworkInterfaceId` - (Required) The ID of the Network Interface. Changing this forces a new resource to be created.

`IpConfigurationName` - (Required) The Name of the IP Configuration within the Network Interface which should be connected to the Application Security Group. Changing this forces a new resource to be created.

`ApplicationSecurityGroupId` - (Required) The ID of the Application Security Group which this Network Interface which should be connected to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The (Terraform specific) ID of the Association between the Network Interface and the Application Security Group.

## See Also

* [azurerm_network_interface_application_security_group_association](https://www.terraform.io/docs/providers/azurerm/r/network_interface_application_security_group_association.html) in the _Terraform Provider Documentation_