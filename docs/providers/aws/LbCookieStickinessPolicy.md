# Terraform::AWS::LbCookieStickinessPolicy

Provides a load balancer cookie stickiness policy, which allows an ELB to control the sticky session lifetime of the browser.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the policy.

`Name` - The name of the stickiness policy.

`LoadBalancer` - The load balancer to which the policy is attached.

`LbPort` - The load balancer port to which the policy is applied.

`CookieExpirationPeriod` - The time period after which the session cookie is considered stale, expressed in seconds.

## See Also

* [aws_lb_cookie_stickiness_policy](https://www.terraform.io/docs/providers/aws/r/lb_cookie_stickiness_policy.html) in the _Terraform Provider Documentation_