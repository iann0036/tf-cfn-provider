# Terraform::AWS::LbSslNegotiationPolicy

Provides a load balancer SSL negotiation policy, which allows an ELB to control the ciphers and protocols that are supported during SSL negotiations between a client and a load balancer.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the policy.

`Name` - The name of the stickiness policy.

`LoadBalancer` - The load balancer to which the policy is attached.

`LbPort` - The load balancer port to which the policy is applied.

`Attribute` - The SSL Negotiation policy attributes.

## See Also

* [aws_lb_ssl_negotiation_policy](https://www.terraform.io/docs/providers/aws/r/lb_ssl_negotiation_policy.html) in the _Terraform Provider Documentation_