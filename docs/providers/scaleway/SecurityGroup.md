# Terraform::Scaleway::SecurityGroup

Provides security groups. This allows security groups to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#security-groups).

## Properties

`Name` - (Required) name of security group.

`Description` - (Required) description of security group.

`EnableDefaultSecurity` - (Optional) default: true. Add default security group rules.

`Stateful` - (Optional) default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers.

`InboundDefaultPolicy` - (Optional) default policy for inbound traffic. Can be one of accept or drop.

`OutboundDefaultPolicy` - (Optional) default policy for outbound traffic. Can be one of accept or drop.


## Return Values

### Fn::GetAtt

`Id` - id of the new resource.

## See Also

* [scaleway_security_group](https://www.terraform.io/docs/providers/scaleway/r/security_group.html) in the _Terraform Provider Documentation_