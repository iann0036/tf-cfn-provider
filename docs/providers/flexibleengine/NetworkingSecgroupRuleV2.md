# Terraform::FlexibleEngine::NetworkingSecgroupRuleV2

Manages a V2 neutron security group rule resource within FlexibleEngine.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Direction` - See Argument Reference above.

`Ethertype` - See Argument Reference above.

`Protocol` - See Argument Reference above.

`PortRangeMin` - See Argument Reference above.

`PortRangeMax` - See Argument Reference above.

`RemoteIpPrefix` - See Argument Reference above.

`RemoteGroupId` - See Argument Reference above.

`SecurityGroupId` - See Argument Reference above.

`TenantId` - See Argument Reference above.

## See Also

* [flexibleengine_networking_secgroup_rule_v2](https://www.terraform.io/docs/providers/flexibleengine/r/networking_secgroup_rule_v2.html) in the _Terraform Provider Documentation_