# Terraform::AWS::ElasticacheParameterGroup

Provides an ElastiCache parameter group resource.

~> **NOTE:** Attempting to remove the `reserved-memory` parameter when `Family` is set to `redis2.6` or `redis2.8` may show a perpetual difference in Terraform due to an Elasticache API limitation. Leave that parameter configured with any value to workaround the issue.

## Properties

`Name` - (Required) The name of the ElastiCache parameter.

`Family` - (Required) The family of the ElastiCache parameter group.

`Description` - (Optional) The description of the ElastiCache parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of ElastiCache parameters to apply.

`Value` - (Required) The value of the ElastiCache parameter.


## Return Values

### Fn::GetAtt

`Id` - The ElastiCache parameter group name.

## See Also

* [aws_elasticache_parameter_group](https://www.terraform.io/docs/providers/aws/r/elasticache_parameter_group.html) in the _Terraform Provider Documentation_