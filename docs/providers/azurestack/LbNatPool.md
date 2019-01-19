# Terraform::AzureStack::LbNatPool

Manages a Load Balancer NAT pool.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the NAT pool.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the Load Balancer in which to create the NAT pool.

`FrontendIpConfigurationName` - (Required) The name of the frontend IP configuration exposing this rule.

`Protocol` - (Required) The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

`FrontendPortStart` - (Required) The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

`FrontendPortEnd` - (Required) The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

`BackendPort` - (Required) The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurestack_lb_nat_pool](https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool.html) in the _Terraform Provider Documentation_