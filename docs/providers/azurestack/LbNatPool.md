# Terraform::AzureStack::LbNatPool

Manages a Load Balancer NAT pool.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurestack_lb_nat_pool](https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool.html) in the _Terraform Provider Documentation_