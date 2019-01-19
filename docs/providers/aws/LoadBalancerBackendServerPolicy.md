# Terraform::AWS::LoadBalancerBackendServerPolicy

Attaches a load balancer policy to an ELB backend server.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the policy.

`LoadBalancerName` - The load balancer on which the policy is defined.

`InstancePort` - The backend port the policies are applied to.

## See Also

* [aws_load_balancer_backend_server_policy](https://www.terraform.io/docs/providers/aws/r/load_balancer_backend_server_policy.html) in the _Terraform Provider Documentation_