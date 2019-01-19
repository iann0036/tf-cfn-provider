# Terraform::AzureStack::Lb

Manages a Load Balancer Resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The LoadBalancer ID.

`PrivateIpAddress` - The first private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

`PrivateIpAddresses` - The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

## See Also

* [azurestack_lb](https://www.terraform.io/docs/providers/azurestack/r/lb.html) in the _Terraform Provider Documentation_