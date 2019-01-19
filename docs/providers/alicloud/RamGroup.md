# Terraform::Alicloud::RamGroup

Provides a RAM Group resource.

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `Force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

`Name` - (Required) Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.

`Comments` - (Optional) Comment of the RAM group. This parameter can have a string of 1 to 128 characters.

`Force` - (Optional) This parameter is used for resource destroy. Default value is `false`.


## Return Values

### Fn::GetAtt

`Id` - The group ID.

`Name` - The group name.

`Comments` - The group comments.

## See Also

* [alicloud_ram_group](https://www.terraform.io/docs/providers/alicloud/r/ram_group.html) in the _Terraform Provider Documentation_