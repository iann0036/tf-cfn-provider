# Terraform::Alicloud::HavipAttachment

Provides an Alicloud HaVip Attachment resource for associating HaVip to ECS Instance.

~> **NOTE:** Terraform will auto build havip attachment while it uses `Terraform::Alicloud::HavipAttachment` to build a havip attachment resource.

## Properties

`HavipId` - (Required, ForceNew) The havip_id of the havip attachment, the field can't be changed.

`InstanceId` - (Required, ForceNew) The instance_id of the havip attachment, the field can't be changed.


## Return Values

### Fn::GetAtt

`Id` - The ID of the havip attachment id and formates as `<havip_id>:<instance_id>`.

## See Also

* [alicloud_havip_attachment](https://www.terraform.io/docs/providers/alicloud/r/havip_attachment.html) in the _Terraform Provider Documentation_