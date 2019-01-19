# Terraform::Alicloud::HavipAttachment

Provides an Alicloud HaVip Attachment resource for associating HaVip to ECS Instance.

~> **NOTE:** Terraform will auto build havip attachment while it uses `alicloud_havip_attachment` to build a havip attachment resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the havip attachment id and formates as `<havip_id>:<instance_id>`.

## See Also

* [alicloud_havip_attachment](https://www.terraform.io/docs/providers/alicloud/r/havip_attachment.html) in the _Terraform Provider Documentation_