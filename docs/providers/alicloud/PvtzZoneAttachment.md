# Terraform::Alicloud::PvtzZoneAttachment

Provides vpcs bound to Alicloud Private Zone resource.

~> **NOTE:** Terraform will auto bind vpc to a Private Zone while it uses `Terraform::Alicloud::PvtzZoneAttachment` to build a Private Zone and VPC binding resource.

## Properties

`ZoneId` - (Required, Forces new resource) The name of the Private Zone Record.

`VpcIds` - (Required) The id List of the VPC, for example:["vpc-1","vpc-2"].


## Return Values

### Fn::GetAtt

`Id` - The ID of the Private Zone VPC Attachment.

## See Also

* [alicloud_pvtz_zone_attachment](https://www.terraform.io/docs/providers/alicloud/r/pvtz_zone_attachment.html) in the _Terraform Provider Documentation_