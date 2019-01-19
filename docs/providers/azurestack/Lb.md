# Terraform::AzureStack::Lb

Manages a Load Balancer Resource.

## Properties

`Name` - (Required) Specifies the name of the frontend ip configuration.

`ResourceGroupName` - (Required) The name of the resource group in which to create the LoadBalancer.

`Location` - (Required) Specifies the supported Azure location where the resource exists.

`FrontendIpConfiguration` - (Optional) A frontend ip configuration block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`SubnetId` - (Optional) Reference to subnet associated with the IP Configuration.

`PrivateIpAddress` - (Optional) Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

`PrivateIpAddressAllocation` - (Optional) Defines how a private IP address is assigned. Options are Static or Dynamic.

`PublicIpAddressId` - (Optional) Reference to Public IP address to be associated with the Load Balancer.


## Return Values

### Fn::GetAtt

`Id` - The LoadBalancer ID.

`PrivateIpAddress` - The first private IP address assigned to the load balancer in `FrontendIpConfiguration` blocks, if any.

`PrivateIpAddresses` - The list of private IP address assigned to the load balancer in `FrontendIpConfiguration` blocks, if any.

## See Also

* [azurestack_lb](https://www.terraform.io/docs/providers/azurestack/r/lb.html) in the _Terraform Provider Documentation_