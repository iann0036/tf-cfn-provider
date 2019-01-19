# Terraform::Alicloud::Vpc

Provides a VPC resource.

~> **NOTE:** Terraform will auto build a router and a route table while it uses `alicloud_vpc` to build a vpc resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC.

`CidrBlock` - The CIDR block for the VPC.

`Name` - The name of the VPC.

`Description` - The description of the VPC.

`RouterId` - The ID of the router created by default on VPC creation.

`RouteTableId` - The route table ID of the router created by default on VPC creation.

## See Also

* [alicloud_vpc](https://www.terraform.io/docs/providers/alicloud/r/vpc.html) in the _Terraform Provider Documentation_