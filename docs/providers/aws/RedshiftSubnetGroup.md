# Terraform::AWS::RedshiftSubnetGroup

Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.

## Properties

`Name` - (Required) The name of the Redshift Subnet group.

`Description` - (Optional) The description of the Redshift Subnet group. Defaults to "Managed by Terraform".

`SubnetIds` - (Required) An array of VPC subnet IDs.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Redshift Subnet group ID.

## See Also

* [aws_redshift_subnet_group](https://www.terraform.io/docs/providers/aws/r/redshift_subnet_group.html) in the _Terraform Provider Documentation_