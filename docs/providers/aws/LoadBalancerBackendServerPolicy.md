# Terraform::AWS::LoadBalancerBackendServerPolicy

Attaches a load balancer policy to an ELB backend server.

## Properties

`LoadBalancerName` - (Required) The load balancer to attach the policy to.

`PolicyNames` - (Required) List of Policy Names to apply to the backend server.

`InstancePort` - (Required) The instance port to apply the policy to.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`LoadBalancerName` - The load balancer on which the policy is defined.

`InstancePort` - The backend port the policies are applied to.

## See Also

* [aws_load_balancer_backend_server_policy](https://www.terraform.io/docs/providers/aws/r/load_balancer_backend_server_policy.html) in the _Terraform Provider Documentation_