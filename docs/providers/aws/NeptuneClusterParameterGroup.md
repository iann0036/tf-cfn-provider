# Terraform::AWS::NeptuneClusterParameterGroup

Manages a Neptune Cluster Parameter Group

## Properties

`Name` - (Required) The name of the neptune parameter.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Family` - (Required) The family of the neptune cluster parameter group.

`Description` - (Optional) The description of the neptune cluster parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of neptune parameters to apply.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Value` - (Required) The value of the neptune parameter.

`ApplyMethod` - (Optional) Valid values are `immediate` and `pending-reboot`. Defaults to `pending-reboot`.


## Return Values

### Fn::GetAtt

`Id` - The neptune cluster parameter group name.

`Arn` - The ARN of the neptune cluster parameter group.

## See Also

* [aws_neptune_cluster_parameter_group](https://www.terraform.io/docs/providers/aws/r/neptune_cluster_parameter_group.html) in the _Terraform Provider Documentation_