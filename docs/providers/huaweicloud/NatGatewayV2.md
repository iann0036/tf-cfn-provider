# Terraform::HuaweiCloud::NatGatewayV2

Manages a V2 nat gateway resource within HuaweiCloud Nat

## Properties

`Region` - (Optional) The region in which to obtain the V2 nat client. If omitted, the `Region` argument of the provider is used. Changing this creates a new nat gateway.

`Name` - (Required) The name of the nat gateway.

`Description` - (Optional) The description of the nat gateway.

`Spec` - (Required) The specification of the nat gateway, valid values are "1", "2", "3", "4".

`TenantId` - (Optional) The target tenant ID in which to allocate the nat gateway. Changing this creates a new nat gateway.

`RouterId` - (Required) ID of the router this nat gateway belongs to. Changing this creates a new nat gateway.

`InternalNetworkId` - (Optional) ID of the network this nat gateway connects to. Changing this creates a new nat gateway.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Spec` - See Properties above.

`TenantId` - See Properties above.

`RouterId` - See Properties above.

`InternalNetworkId` - See Properties above.

## See Also

* [huaweicloud_nat_gateway_v2](https://www.terraform.io/docs/providers/huaweicloud/r/nat_gateway_v2.html) in the _Terraform Provider Documentation_