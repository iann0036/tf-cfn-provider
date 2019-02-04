# Terraform::AWS::LbCookieStickinessPolicy

Provides a load balancer cookie stickiness policy, which allows an ELB to control the sticky session lifetime of the browser.

## Properties

`Name` - (Required) The name of the stickiness policy.

`LoadBalancer` - (Required) The load balancer to which the policy
should be attached.

`LbPort` - (Required) The load balancer port to which the policy
should be applied. This must be an active listener on the load
balancer.

`CookieExpirationPeriod` - (Optional) The time period after which
the session cookie should be considered stale, expressed in seconds.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`Name` - The name of the stickiness policy.

`LoadBalancer` - The load balancer to which the policy is attached.

`LbPort` - The load balancer port to which the policy is applied.

`CookieExpirationPeriod` - The time period after which the session cookie is considered stale, expressed in seconds.

## See Also

* [aws_lb_cookie_stickiness_policy](https://www.terraform.io/docs/providers/aws/r/lb_cookie_stickiness_policy.html) in the _Terraform Provider Documentation_