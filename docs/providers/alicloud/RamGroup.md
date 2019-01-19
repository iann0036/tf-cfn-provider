# Terraform::Alicloud::RamGroup

Provides a RAM Group resource.

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The group ID.

`Name` - The group name.

`Comments` - The group comments.

## See Also

* [alicloud_ram_group](https://www.terraform.io/docs/providers/alicloud/r/ram_group.html) in the _Terraform Provider Documentation_