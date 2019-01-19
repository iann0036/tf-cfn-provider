# Terraform::Alicloud::RamPolicy

Provides a RAM Policy resource. 

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The policy ID.

`Name` - The policy name.

`Type` - The policy type.

`Description` - The policy description.

`Statement` - List of statement of the policy document.

`Document` - The policy document.

`Version` - The policy document version.

`AttachmentCount` - The policy attachment count.

## See Also

* [alicloud_ram_policy](https://www.terraform.io/docs/providers/alicloud/r/ram_policy.html) in the _Terraform Provider Documentation_