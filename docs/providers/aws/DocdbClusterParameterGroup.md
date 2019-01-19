# Terraform::AWS::DocdbClusterParameterGroup

Manages a DocumentDB Cluster Parameter Group

## Properties

`Name` - (Optional, Forces new resource) The name of the documentDB cluster parameter group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Family` - (Required, Forces new resource) The family of the documentDB cluster parameter group.

`Description` - (Optional, Forces new resource) The description of the documentDB cluster parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of documentDB parameters to apply.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Name` - (Required) The name of the documentDB parameter.

`Value` - (Required) The value of the documentDB parameter.

`ApplyMethod` - (Optional) Valid values are `immediate` and `pending-reboot`. Defaults to `pending-reboot`.


## Return Values

### Fn::GetAtt

`Id` - The documentDB cluster parameter group name.

`Arn` - The ARN of the documentDB cluster parameter group.

## See Also

* [aws_docdb_cluster_parameter_group](https://www.terraform.io/docs/providers/aws/r/docdb_cluster_parameter_group.html) in the _Terraform Provider Documentation_