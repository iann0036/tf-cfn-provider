# Terraform::AWS::ElasticacheSecurityGroup

Provides an ElastiCache Security Group to control access to one or more cache
clusters.

~> **NOTE:** ElastiCache Security Groups are for use only when working with an
ElastiCache cluster **outside** of a VPC. If you are using a VPC, see the
[ElastiCache Subnet Group resource](elasticache_subnet_group.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_elasticache_security_group](https://www.terraform.io/docs/providers/aws/r/elasticache_security_group.html) in the _Terraform Provider Documentation_