# Terraform::AWS::RedshiftParameterGroup

Provides a Redshift Cluster parameter group resource.

## Properties

`Name` - (Required) The name of the Redshift parameter.

`Family` - (Required) The family of the Redshift parameter group.

`Description` - (Optional) The description of the Redshift parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of Redshift parameters to apply.

`Value` - (Required) The value of the Redshift parameter.


## Return Values

### Fn::GetAtt

`Id` - The Redshift parameter group name.

## See Also

* [aws_redshift_parameter_group](https://www.terraform.io/docs/providers/aws/r/redshift_parameter_group.html) in the _Terraform Provider Documentation_