# Terraform::HuaweiCloud::IdentityGroupV3

Manages a User Group resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Properties

`Name` - (Required) The name of the group.The length is less than or equal
to 64 bytes.

`Description` - (Optional) A description of the group.

`DomainId` - (Optional) The domain this group belongs to.

`Region` - (Optional) The region in which to obtain the V3 Keystone client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new User Group.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

## See Also

* [huaweicloud_identity_group_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_group_v3.html) in the _Terraform Provider Documentation_