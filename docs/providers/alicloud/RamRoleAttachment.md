# Terraform::Alicloud::RamRoleAttachment

Provides a RAM role attachment resource to bind role for several ECS instances.

## Properties

`RoleName` - (Required, Forces new resource) The name of role used to bind. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-", "_", and must not begin with a hyphen.

`InstanceIds` - (Required, Forces new resource) The list of ECS instance's IDs.


## Return Values

### Fn::GetAtt

`RoleName` - The name of the role.

## See Also

* [alicloud_ram_role_attachment](https://www.terraform.io/docs/providers/alicloud/r/ram_role_attachment.html) in the _Terraform Provider Documentation_