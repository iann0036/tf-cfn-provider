# Terraform::AWS::NeptuneSubnetGroup

Provides an Neptune subnet group resource.

## Properties

`Name` - (Optional, Forces new resource) The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - (Optional) The description of the neptune subnet group. Defaults to "Managed by Terraform".

`SubnetIds` - (Required) A list of VPC subnet IDs.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The neptune subnet group name.

`Arn` - The ARN of the neptune subnet group.

## See Also

* [aws_neptune_subnet_group](https://www.terraform.io/docs/providers/aws/r/neptune_subnet_group.html) in the _Terraform Provider Documentation_