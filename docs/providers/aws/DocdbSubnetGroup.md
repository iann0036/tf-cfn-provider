# Terraform::AWS::DocdbSubnetGroup

Provides an DocumentDB subnet group resource.

## Properties

`Name` - (Optional, Forces new resource) The name of the docDB subnet group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - (Optional) The description of the docDB subnet group. Defaults to "Managed by Terraform".

`SubnetIds` - (Required) A list of VPC subnet IDs.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The docDB subnet group name.

`Arn` - The ARN of the docDB subnet group.

## See Also

* [aws_docdb_subnet_group](https://www.terraform.io/docs/providers/aws/r/docdb_subnet_group.html) in the _Terraform Provider Documentation_