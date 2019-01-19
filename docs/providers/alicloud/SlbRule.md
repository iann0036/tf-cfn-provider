# Terraform::Alicloud::SlbRule

A forwarding rule is configured in `HTTP`/`HTTPS` listener and it used to listen a list of backend servers which in one specified virtual backend server group.
You can add forwarding rules to a listener to forward requests based on the domain names or the URL in the request.

~> **NOTE:** One virtual backend server group can be attached in multiple forwarding rules.

~> **NOTE:** At least one "Domain" or "Url" must be specified when creating a new rule.

~> **NOTE:** Having the same 'Domain' and 'Url' rule can not be created repeatedly in the one listener.

~> **NOTE:** Rule only be created in the `HTTP` or `HTTPS` listener.

~> **NOTE:** Only rule's virtual server group can be modified.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the forwarding rule.

`LoadBalancerId` - The Load Balancer ID in which forwarding rule belongs.

`Name` - The name of the forwarding rule.

`ForntendPort` - The listener port in which forwarding rule belongs.

`Domain` - The domain name of the forwarding rule.

`Url` - The url of the forwarding rule.

`ServerGroupId` - The Id of the virtual server group.

## See Also

* [alicloud_slb_rule](https://www.terraform.io/docs/providers/alicloud/r/slb_rule.html) in the _Terraform Provider Documentation_