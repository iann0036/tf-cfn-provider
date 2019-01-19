# Terraform::HuaweiCloud::NatSnatRuleV2

Manages a V2 snat rule resource within HuaweiCloud Nat

## Properties

`Region` - (Optional) The region in which to obtain the V2 nat client. If omitted, the `Region` argument of the provider is used. Changing this creates a new snat rule.

`NatGatewayId` - (Required) ID of the nat gateway this snat rule belongs to. Changing this creates a new snat rule.

`NetworkId` - (Required) ID of the network this snat rule connects to. Changing this creates a new snat rule.

`FloatingIpId` - (Required) ID of the floating ip this snat rule connets to. Changing this creates a new snat rule.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`NatGatewayId` - See Properties above.

`NetworkId` - See Properties above.

`FloatingIpId` - See Properties above.

## See Also

* [huaweicloud_nat_snat_rule_v2](https://www.terraform.io/docs/providers/huaweicloud/r/nat_snat_rule_v2.html) in the _Terraform Provider Documentation_