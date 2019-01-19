# Terraform::AWS::Lb

Provides a Load Balancer resource.

~> **Note:** `aws_alb` is known as `aws_lb`. The functionality is identical.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ARN of the load balancer (matches `arn`).

`Arn` - The ARN of the load balancer (matches `id`).

`ArnSuffix` - The ARN suffix for use with CloudWatch Metrics.

`DnsName` - The DNS name of the load balancer.

`ZoneId` - The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).

## See Also

* [aws_lb](https://www.terraform.io/docs/providers/aws/r/lb.html) in the _Terraform Provider Documentation_