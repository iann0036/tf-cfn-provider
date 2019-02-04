# Terraform::CloudStack::NetworkAclRule

Creates network ACL rules for a given network ACL.

## Properties

`AclId` - (Required) The network ACL ID for which to create the rules.
Changing this forces a new resource to be created.

`Managed` - (Optional) USE WITH CAUTION! If enabled all the firewall rules for
this network ACL will be managed by this resource. This means it will delete
all firewall rules that are not in your config! (defaults false).

`Rule` - (Optional) Can be specified multiple times. Each rule block supports
fields documented below. If `managed = false` at least one rule is required!.

`Project` - (Optional) The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

### Rule Properties

`Action` - (Optional) The action for the rule. Valid options are: `allow` and
`deny` (defaults allow).

`CidrList` - (Required) A CIDR list to allow access to the given ports.

`Protocol` - (Required) The name of the protocol to allow. Valid options are:
`tcp`, `udp`, `icmp`, `all` or a valid protocol number.

`IcmpType` - (Optional) The ICMP type to allow, or `-1` to allow `any`. This
can only be specified if the protocol is ICMP. (defaults 0).

`IcmpCode` - (Optional) The ICMP code to allow, or `-1` to allow `any`. This
can only be specified if the protocol is ICMP. (defaults 0).

`Ports` - (Optional) List of ports and/or port ranges to allow. This can only
be specified if the protocol is TCP, UDP, ALL or a valid protocol number.

`TrafficType` - (Optional) The traffic type for the rule. Valid options are:
`ingress` or `egress` (defaults ingress).


## Return Values

### Fn::GetAtt

`Id` - The ACL ID for which the rules are created.

## See Also

* [cloudstack_network_acl_rule](https://www.terraform.io/docs/providers/cloudstack/r/network_acl_rule.html) in the _Terraform Provider Documentation_