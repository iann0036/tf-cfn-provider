# Terraform::AWS::LoadBalancerPolicy

Provides a load balancer policy, which can be attached to an ELB listener or backend server.

## Properties

`LoadBalancerName` - (Required) The load balancer on which the policy is defined.

`PolicyName` - (Required) The name of the load balancer policy.

`PolicyTypeName` - (Required) The policy type.

`PolicyAttribute` - (Optional) Policy attribute to apply to the policy.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`PolicyName` - The name of the stickiness policy.

`PolicyTypeName` - The policy type of the policy.

`LoadBalancerName` - The load balancer on which the policy is defined.

## See Also

* [aws_load_balancer_policy](https://www.terraform.io/docs/providers/aws/r/load_balancer_policy.html) in the _Terraform Provider Documentation_