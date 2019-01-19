# Terraform::RightScale::SecurityGroupRule

Use this resource to create, update or destroy RightScale [security group rules](http://reference.rightscale.com/api1.5/resources/ResourceSecurityGroupRules.html).

## Properties

`SourceType` - (Required) Source type. May be a CIDR block or another Security Group. Options are 'cidr_ips' or 'group'.

`Protocol` - (Required) Protocol to filter on.  Options are 'tcp', 'udp', 'icmp' and 'all'.

`SecurityGroupHref` - (Required) Href of parent security group.

`ProtocolDetails` - (Required) Block options include:.

### ProtocolDetails Properties

`CidrIps` - (Contextual) An IP address range in CIDR notation. Required if source_type is 'cidr'. Conflicts with 'group_name' and 'group_owner'.

`GroupName` - (Contextual) Name of source Security Group. Required if source_type is 'group'.  Conflicts with 'cidr_ips'.

`GroupOwner` - (Contexual) Owner of source Security Group. Required if source_type is 'group'. Conflicts with 'cidr_ips'.

`Direction` - (Optional) Direction of traffic to apply rule against.  Options are 'ingress' or 'egress'.

`Priority` - (Optional) Lower takes precedence. Supported by security group rules created in Microsoft Azure only.


## Return Values

### Fn::GetAtt

`Href` - Href of the security group rule.

`ResourceUid` - Cloud resource_uid.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_security_group_rule](https://www.terraform.io/docs/providers/rightscale/r/security_group_rule.html) in the _Terraform Provider Documentation_