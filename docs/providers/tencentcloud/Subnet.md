# Terraform::TencentCloud::Subnet

Provides an VPC subnet resource.

## Properties

`Name` - (Required) The name for the Subnet.

`CidrBlock` - (Required, Forces new resource) The CIDR block for the Subnet.

`AvailabilityZone` - (Required, Forces new resource) The AZ for the subnet.

`VpcId` - (Required, Forces new resource) The VPC ID.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Subnet.

`Name` - The name for the Subnet.

`CidrBlock` - The CIDR block of the Subnet.

`AvailabilityZone` - The AZ for the subnet.

`VpcId` - The VPC ID.

`RouteTableId` - The Route Table ID.

## See Also

* [tencentcloud_subnet](https://www.terraform.io/docs/providers/tencentcloud/r/subnet.html) in the _Terraform Provider Documentation_