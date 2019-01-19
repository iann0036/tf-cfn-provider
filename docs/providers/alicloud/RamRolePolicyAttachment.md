# Terraform::Alicloud::RamRolePolicyAttachment

Provides a RAM Role attachment resource.

## Properties

`RoleName` - (Required, Forces new resource) Name of the RAM Role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-", "_", and must not begin with a hyphen.

`PolicyName` - (Required, Forces new resource) Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.

`PolicyType` - (Required, Forces new resource) Type of the RAM policy. It must be `Custom` or `System`.


## Return Values

### Fn::GetAtt

`Id` - The attachment ID.

`RoleName` - The role name.

`PolicyName` - The policy name.

`PolicyType` - The policy type.

## See Also

* [alicloud_ram_role_policy_attachment](https://www.terraform.io/docs/providers/alicloud/r/ram_role_policy_attachment.html) in the _Terraform Provider Documentation_