# Terraform::Alicloud::SlbRule

A forwarding rule is configured in `HTTP`/`HTTPS` listener and it used to listen a list of backend servers which in one specified virtual backend server group.
You can add forwarding rules to a listener to forward requests based on the domain names or the URL in the request.

~> **NOTE:** One virtual backend server group can be attached in multiple forwarding rules.

~> **NOTE:** At least one "Domain" or "Url" must be specified when creating a new rule.

~> **NOTE:** Having the same 'Domain' and 'Url' rule can not be created repeatedly in the one listener.

~> **NOTE:** Rule only be created in the `HTTP` or `HTTPS` listener.

~> **NOTE:** Only rule's virtual server group can be modified.

## Properties

`LoadBalancerId` - (Required, ForceNew) The Load Balancer ID which is used to launch the new forwarding rule.

`Name` - (Optional, ForceNew) Name of the forwarding rule. Our plugin provides a default name: "tf-slb-rule".

`FrontendPort` - (Required, ForceNew) The listener frontend port which is used to launch the new forwarding rule. Valid range: [1-65535].

`Domain` - (Optional, ForceNew) Domain name of the forwarding rule. It can contain letters a-z, numbers 0-9, hyphens (-), and periods (.),
and wildcard characters. The following two domain name formats are supported:
- Standard domain name: www.test.com
- Wildcard domain name: *.test.com. wildcard (*) must be the first character in the format of (*.).

`Url` - (Optional, ForceNew) Domain of the forwarding rule. It must be 2-80 characters in length. Only letters a-z, numbers 0-9,
and characters '-' '/' '?' '%' '#' and '&' are allowed. URLs must be started with the character '/', but cannot be '/' alone.

`ServerGroupId` - (Required) ID of a virtual server group that will be forwarded.


## Return Values

### Fn::GetAtt

`Id` - The ID of the forwarding rule.

`LoadBalancerId` - The Load Balancer ID in which forwarding rule belongs.

`Name` - The name of the forwarding rule.

`ForntendPort` - The listener port in which forwarding rule belongs.

`Domain` - The domain name of the forwarding rule.

`Url` - The url of the forwarding rule.

`ServerGroupId` - The Id of the virtual server group.

## See Also

* [alicloud_slb_rule](https://www.terraform.io/docs/providers/alicloud/r/slb_rule.html) in the _Terraform Provider Documentation_