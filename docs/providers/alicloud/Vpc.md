# Terraform::Alicloud::Vpc

Provides a VPC resource.

~> **NOTE:** Terraform will auto build a router and a route table while it uses `Terraform::Alicloud::Vpc` to build a vpc resource.

## Properties

`CidrBlock` - (Required, Forces new resource) The CIDR block for the VPC.

`Name` - (Optional) The name of the VPC. Defaults to null.

`Description` - (Optional) The VPC description. Defaults to null.


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