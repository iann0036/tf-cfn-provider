# Terraform::AWS::LoadBalancerPolicy

Provides a load balancer policy, which can be attached to an ELB listener or backend server.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the policy.

`PolicyName` - The name of the stickiness policy.

`PolicyTypeName` - The policy type of the policy.

`LoadBalancerName` - The load balancer on which the policy is defined.

## See Also

* [aws_load_balancer_policy](https://www.terraform.io/docs/providers/aws/r/load_balancer_policy.html) in the _Terraform Provider Documentation_