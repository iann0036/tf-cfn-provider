# Terraform::HuaweiCloud::VpcV1

Manages a VPC resource within HuaweiCloud.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` -  ID of the VPC.

`Name` -  See Argument Reference above.

`Cidr` - See Argument Reference above.

`Status` - The current status of the desired VPC. Can be either CREATING, OK, DOWN, PENDING_UPDATE, PENDING_DELETE, or ERROR.

`Shared` - Specifies whether the cross-tenant sharing is supported.

`Region` - See Argument Reference above.

## See Also

* [huaweicloud_vpc_v1](https://www.terraform.io/docs/providers/huaweicloud/r/vpc_v1.html) in the _Terraform Provider Documentation_