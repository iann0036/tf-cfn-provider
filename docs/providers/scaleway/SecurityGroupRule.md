# Terraform::Scaleway::SecurityGroupRule

Provides security group rules. This allows security group rules to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#security-groups-manage-rules).

## Properties

`SecurityGroup` - (Required) the security group which should be associated with this rule.

`Action` - (Required) action of rule (`accept`, `drop`).

`Direction` - (Required) direction of rule (`inbound`, `outbound`).

`IpRange` - (Required) ip_range of rule.

`Protocol` - (Required) protocol of rule (`ICMP`, `TCP`, `UDP`).

`Port` - (Optional) port of the rule.


## Return Values

### Fn::GetAtt

`Id` - id of the new resource.

## See Also

* [scaleway_security_group_rule](https://www.terraform.io/docs/providers/scaleway/r/security_group_rule.html) in the _Terraform Provider Documentation_