# Terraform::Alicloud::RamRole

Provides a RAM Role resource.

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The role ID.

`Name` - The role name.

`Arn` - The role arn.

`Description` - The role description.

`Version` - The role policy document version.

`Document` - Authorization strategy of the role.

`RamUsers` - List of services which can assume the RAM role.

`Services` - List of services which can assume the RAM role.

## See Also

* [alicloud_ram_role](https://www.terraform.io/docs/providers/alicloud/r/ram_role.html) in the _Terraform Provider Documentation_