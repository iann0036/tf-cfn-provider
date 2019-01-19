# Terraform::AzureStack::LbNatRule

Manages a LoadBalancer NAT Rule.

~> **NOTE** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the LoadBalancer to which the resource is attached.

## See Also

* [azurestack_lb_nat_rule](https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule.html) in the _Terraform Provider Documentation_