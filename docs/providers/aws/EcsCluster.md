# Terraform::AWS::EcsCluster

Provides an ECS cluster.

## Properties

`Name` - (Required) The name of the cluster (up to 255 letters, numbers, hyphens, and underscores).

`Tags` - (Optional) Key-value mapping of resource tags.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) that identifies the cluster.

`Arn` - The Amazon Resource Name (ARN) that identifies the cluster.

## See Also

* [aws_ecs_cluster](https://www.terraform.io/docs/providers/aws/r/ecs_cluster.html) in the _Terraform Provider Documentation_