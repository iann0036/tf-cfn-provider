# Terraform::AWS::LbSslNegotiationPolicy

Provides a load balancer SSL negotiation policy, which allows an ELB to control the ciphers and protocols that are supported during SSL negotiations between a client and a load balancer.

## Properties

`Name` - (Required) The name of the SSL negotiation policy.

`LoadBalancer` - (Required) The load balancer to which the policy
should be attached.

`LbPort` - (Required) The load balancer port to which the policy
should be applied. This must be an active listener on the load
balancer.

`Attribute` - (Optional) An SSL Negotiation policy attribute. Each has two properties:.

`Name` - The name of the attribute.

`Value` - The value of the attribute.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`Name` - The name of the stickiness policy.

`LoadBalancer` - The load balancer to which the policy is attached.

`LbPort` - The load balancer port to which the policy is applied.

`Attribute` - The SSL Negotiation policy attributes.

## See Also

* [aws_lb_ssl_negotiation_policy](https://www.terraform.io/docs/providers/aws/r/lb_ssl_negotiation_policy.html) in the _Terraform Provider Documentation_