# Terraform::AWS::LoadBalancerListenerPolicy

Attaches a load balancer policy to an ELB Listener.

## Properties

`LoadBalancerName` - (Required) The load balancer to attach the policy to.

`LoadBalancerPort` - (Required) The load balancer listener port to apply the policy to.

`PolicyNames` - (Required) List of Policy Names to apply to the backend server.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`LoadBalancerName` - The load balancer on which the policy is defined.

`LoadBalancerPort` - The load balancer listener port the policies are applied to.

## See Also

* [aws_load_balancer_listener_policy](https://www.terraform.io/docs/providers/aws/r/load_balancer_listener_policy.html) in the _Terraform Provider Documentation_