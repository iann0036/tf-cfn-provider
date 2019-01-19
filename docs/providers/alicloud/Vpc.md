# Terraform::Alicloud::Vpc

Provides a VPC resource.

~> **NOTE:** Terraform will auto build a router and a route table while it uses `alicloud_vpc` to build a vpc resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPC.

`CidrBlock` - The CIDR block for the VPC.

`Name` - The name of the VPC.

`Description` - The description of the VPC.

`RouterId` - The ID of the router created by default on VPC creation.

`RouteTableId` - The route table ID of the router created by default on VPC creation.

## See Also

* [alicloud_vpc](https://www.terraform.io/docs/providers/alicloud/r/vpc.html) in the _Terraform Provider Documentation_