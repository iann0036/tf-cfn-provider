# Terraform::AWS::Route53HealthCheck

Provides a Route53 health check.

## Properties

`ReferenceName` - (Optional) This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others).

`Fqdn` - (Optional) The fully qualified domain name of the endpoint to be checked.

`IpAddress` - (Optional) The IP address of the endpoint to be checked.

`Port` - (Optional) The port of the endpoint to be checked.

`Type` - (Required) The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.

`FailureThreshold` - (Required) The number of consecutive health checks that an endpoint must pass or fail.

`RequestInterval` - (Required) The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.

`ResourcePath` - (Optional) The path that you want Amazon Route 53 to request when performing health checks.

`SearchString` - (Optional) String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.

`MeasureLatency` - (Optional) A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.

`InvertHealthcheck` - (Optional) A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.

`EnableSni` - (Optional) A boolean value that indicates whether Route53 should send the `Fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `Type` is "HTTPS" `EnableSni` defaults to `true`, when `Type` is anything else `EnableSni` defaults to `false`.

`ChildHealthchecks` - (Optional) For a specified parent health check, a list of HealthCheckId values for the associated child health checks.

`ChildHealthThreshold` - (Optional) The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive.

`CloudwatchAlarmName` - (Optional) The name of the CloudWatch alarm.

`CloudwatchAlarmRegion` - (Optional) The CloudWatchRegion that the CloudWatch alarm was created in.

`InsufficientDataHealthStatus` - (Optional) The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.

`Regions` - (Optional) A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.

`Tags` - (Optional) A mapping of tags to assign to the health check.


## See Also

* [aws_route53_health_check](https://www.terraform.io/docs/providers/aws/r/route53_health_check.html) in the _Terraform Provider Documentation_