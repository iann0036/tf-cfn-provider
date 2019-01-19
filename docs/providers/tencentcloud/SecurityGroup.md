# Terraform::TencentCloud::SecurityGroup

Provides a security group resource.

## Properties

`Name` - (Required) The name of the security group. Name should be unique in each project, and no more than 60 characters.

`Description` - (Optional) The security group's description, maximum length is 100 characters.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group.

`Name` - The name of the security group.

`Description` - The description of the security group.

## See Also

* [tencentcloud_security_group](https://www.terraform.io/docs/providers/tencentcloud/r/security_group.html) in the _Terraform Provider Documentation_