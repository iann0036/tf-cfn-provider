# Terraform::AWS::ElasticacheParameterGroup

Provides an ElastiCache parameter group resource.

~> **NOTE:** Attempting to remove the `reserved-memory` parameter when `family` is set to `redis2.6` or `redis2.8` may show a perpetual difference in Terraform due to an Elasticache API limitation. Leave that parameter configured with any value to workaround the issue.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ElastiCache parameter group name.

## See Also

* [aws_elasticache_parameter_group](https://www.terraform.io/docs/providers/aws/r/elasticache_parameter_group.html) in the _Terraform Provider Documentation_