# Terraform::AzureRM::Firewall

Manages an Azure Firewall.

## Properties

`Name` - (Required) Specifies the name of the IP Configuration.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`IpConfiguration` - (Required) A `IpConfiguration` block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`SubnetId` - (Required) Reference to the subnet associated with the IP Configuration.

`PublicIpAddressId` - (Required) The Resource ID of the Public IP Address associated with the firewall.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the Azure Firewall.

`IpConfiguration` - A `IpConfiguration` block as defined below.

`PrivateIpAddress` - The private IP address of the Azure Firewall.

## See Also

* [azurerm_firewall](https://www.terraform.io/docs/providers/azurerm/r/firewall.html) in the _Terraform Provider Documentation_