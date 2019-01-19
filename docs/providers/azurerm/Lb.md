# Terraform::AzureRM::Lb

Manage a Load Balancer Resource.

## Properties

`ResourceGroupName` - (Required) The name of the Resource Group in which to create the Load Balancer.

`Location` - (Required) Specifies the supported Azure Region where the Load Balancer should be created.

`FrontendIpConfiguration` - (Optional) A `FrontendIpConfiguration` block as documented below.

`Sku` - (Optional) The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### FrontendIpConfiguration Properties

`Name` - (Required) Specifies the name of the frontend ip configuration.

`SubnetId` - The ID of the Subnet which should be associated with the IP Configuration.

`PrivateIpAddress` - (Optional) Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

`PrivateIpAddressAllocation` - (Optional) The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.

`PublicIpAddressId` - (Optional) Th ID of a Public IP Address which should be associated with the Load Balancer.

`Zones` - (Optional) A list of Availability Zones which the Load Balancer's IP Addresses should be created in.


## Return Values

### Fn::GetAtt

`Id` - The Load Balancer ID.

`PrivateIpAddress` - The first private IP address assigned to the load balancer in `FrontendIpConfiguration` blocks, if any.

`PrivateIpAddresses` - The list of private IP address assigned to the load balancer in `FrontendIpConfiguration` blocks, if any.

## See Also

* [azurerm_lb](https://www.terraform.io/docs/providers/azurerm/r/lb.html) in the _Terraform Provider Documentation_