# Terraform::OpenStack::SharedfilesystemShareAccessV2

Use this resource to control the share access lists.

## Properties

`ShareId` - (Required) The UUID of the share to which you are granted access.

`AccessType` - (Required) The access rule type. Can either be an ip, user or cert.

`AccessTo` - (Required) The value that defines the access. Can either be an IP address or a username verified by configured Security Service of the Share Network.

`AccessLevel` - (Required) The access level to the share. Can either be rw or ro.


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the Share Access.

`ShareId` - See Properties above.

`AccessType` - See Properties above.

`AccessTo` - See Properties above.

`AccessLevel` - See Properties above.

## See Also

* [openstack_sharedfilesystem_share_access_v2](https://www.terraform.io/docs/providers/openstack/r/sharedfilesystem_share_access_v2.html) in the _Terraform Provider Documentation_