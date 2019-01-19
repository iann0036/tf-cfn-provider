# Terraform::OVH::VrackPubliccloudAttachment

__DEPRECATED__ use `Terraform::OVH::VrackCloudproject` instead.
Attach an existing PublicCloud project to an existing VRack.

## Properties

`VrackId` - (Required) The id of the vrack. If omitted, the `OVH_VRACK_ID` environment variable is used.

`ProjectId` - (Required) The id of the public cloud project. If omitted, the `OVH_PROJECT_ID` environment variable is used.


## Return Values

### Fn::GetAtt

`VrackId` - See Properties above.

`ProjectId` - See Properties above.

## See Also

* [ovh_vrack_publiccloud_attachment](https://www.terraform.io/docs/providers/ovh/r/vrack_publiccloud_attachment.html) in the _Terraform Provider Documentation_