# Terraform::OVH::VrackCloudproject

Attach an existing public cloud project to an existing VRack.

## Properties

`VrackId` - (Required) The id of the vrack. If omitted, the `OVH_VRACK_ID` environment variable is used.

`ProjectId` - (Required) The id of the public cloud project. If omitted, the `OVH_PROJECT_ID` environment variable is used.


## Return Values

### Fn::GetAtt

`VrackId` - See Properties above.

`ProjectId` - See Properties above.

## See Also

* [ovh_vrack_cloudproject](https://www.terraform.io/docs/providers/ovh/r/vrack_cloudproject.html) in the _Terraform Provider Documentation_