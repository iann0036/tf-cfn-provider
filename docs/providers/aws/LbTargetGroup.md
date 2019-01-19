# Terraform::AWS::LbTargetGroup

Provides a Target Group resource for use with Load Balancer resources.

~> **Note:** `Terraform::AWS::AlbTargetGroup` is known as `awsLbTargetGroup`. The functionality is identical.

## Properties

`Name` - (Optional, Forces new resource) The name of the target group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`. Cannot be longer than 6 characters.

`Port` - (Optional) The port on which targets receive traffic, unless overridden when registering a specific target. Required when `TargetType` is `instance` or `ip`. Does not apply when `TargetType` is `lambda`.

`Protocol` - (Optional) The protocol to use for routing traffic to the targets. Should be one of "TCP", "HTTP" or "HTTPS". Required when `TargetType` is `instance` or `ip`. Does not apply when `TargetType` is `lambda`.

`VpcId` - (Optional) The identifier of the VPC in which to create the target group. Required when `TargetType` is `instance` or `ip`. Does not apply when `TargetType` is `lambda`.

`DeregistrationDelay` - (Optional) The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.

`SlowStart` - (Optional) The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.

`ProxyProtocolV2` - (Optional) Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.

`Stickiness` - (Optional) A Stickiness block. Stickiness blocks are documented below. `Stickiness` is only valid if used with Load Balancers of type `Application`.

`HealthCheck` - (Optional) A Health Check block. Health Check blocks are documented below.

`TargetType` - (Optional) The type of target that you must specify when registering targets with this target group. The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn). The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses. If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Stickiness Properties

`Type` - (Required) The type of sticky sessions. The only current possible value is `lb_cookie`.

`CookieDuration` - (Optional) The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).

`Enabled` - (Optional) Boolean to enable / disable `Stickiness`. Default is `true`.

### HealthCheck Properties

`Interval` - (Optional) The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. Default 30 seconds.

`Path` - (Required for HTTP/HTTPS ALB) The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).

`Port` - (Optional) The port to use to connect with the target. Valid values are either ports 1-65536, or `traffic-port`. Defaults to `traffic-port`.

`Protocol` - (Optional) The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `TargetType` is `lambda`.

`Timeout` - (Optional) The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 60 seconds and the default is 5 seconds. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.

`HealthyThreshold` - (Optional) The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.

`UnhealthyThreshold` - (Optional) The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the `HealthyThreshold`. Defaults to 3.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the Target Group (matches `arn`).

`Arn` - The ARN of the Target Group (matches `id`).

`ArnSuffix` - The ARN suffix for use with CloudWatch Metrics.

`Name` - The name of the Target Group.

## See Also

* [aws_lb_target_group](https://www.terraform.io/docs/providers/aws/r/lb_target_group.html) in the _Terraform Provider Documentation_