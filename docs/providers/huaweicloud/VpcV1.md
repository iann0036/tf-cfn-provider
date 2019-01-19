# Terraform::HuaweiCloud::VpcV1

Manages a VPC resource within HuaweiCloud.

## Properties

`Cidr` - (Required) The range of available subnets in the VPC. The value ranges from 10.0.0.0/8 to 10.255.255.0/24, 172.16.0.0/12 to 172.31.255.0/24, or 192.168.0.0/16 to 192.168.255.0/24.

`Region` - (Optional) The region in which to obtain the V1 VPC client. A VPC client is needed to create a VPC. If omitted, the region argument of the provider is used. Changing this creates a new VPC.

`Name` - (Required) The name of the VPC. The name must be unique for a tenant. The value is a string of no more than 64 characters and can contain digits, letters, underscores (_), and hyphens (-). Changing this updates the name of the existing VPC.


## Return Values

### Fn::GetAtt

`Id` -  ID of the VPC.

`Name` -  See Properties above.

`Cidr` - See Properties above.

`Status` - The current status of the desired VPC. Can be either CREATING, OK, DOWN, PENDING_UPDATE, PENDING_DELETE, or ERROR.

`Shared` - Specifies whether the cross-tenant sharing is supported.

`Region` - See Properties above.

## See Also

* [huaweicloud_vpc_v1](https://www.terraform.io/docs/providers/huaweicloud/r/vpc_v1.html) in the _Terraform Provider Documentation_