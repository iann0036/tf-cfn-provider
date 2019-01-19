# Terraform::AWS::RedshiftSecurityGroup

Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters

## Properties

`Name` - (Required) The name of the Redshift security group.

`Description` - (Optional) The description of the Redshift security group. Defaults to "Managed by Terraform".

`Ingress` - (Optional) A list of ingress rules.

`Cidr` - The CIDR block to accept.

`SecurityGroupName` - The name of the security group to authorize.

`SecurityGroupOwnerId` - The owner Id of the security group provided by `SecurityGroupName`.


## Return Values

### Fn::GetAtt

`Id` - The Redshift security group ID.

## See Also

* [aws_redshift_security_group](https://www.terraform.io/docs/providers/aws/r/redshift_security_group.html) in the _Terraform Provider Documentation_