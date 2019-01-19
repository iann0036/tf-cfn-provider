# Terraform::AWS::Route53QueryLog

Provides a Route53 query logging configuration resource.

~> **NOTE:** There are restrictions on the configuration of query logging. Notably,
the CloudWatch log group must be in the `us-east-1` region,
a permissive CloudWatch log resource policy must be in place, and
the Route53 hosted zone must be public.
See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.

## Properties

`CloudwatchLogGroupArn` - (Required) CloudWatch log group ARN to send query logs.

`ZoneId` - (Required) Route53 hosted zone ID to enable query logs.


## Return Values

### Fn::GetAtt

`Id` - The query logging configuration ID.

## See Also

* [aws_route53_query_log](https://www.terraform.io/docs/providers/aws/r/route53_query_log.html) in the _Terraform Provider Documentation_