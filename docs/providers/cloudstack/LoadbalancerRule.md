# Terraform::CloudStack::LoadbalancerRule

Creates a loadbalancer rule.

## Properties

`Name` - (Required) Name of the loadbalancer rule.
Changing this forces a new resource to be created.

`Description` - (Optional) The description of the load balancer rule.

`IpAddressId` - (Required) Public IP address ID from where the network
traffic will be load balanced from. Changing this forces a new resource
to be created.

`NetworkId` - (Optional) The network ID this rule will be created for.
Required when public IP address is not associated with any network yet
(VPC case).

`Algorithm` - (Required) Load balancer rule algorithm (source, roundrobin,
leastconn). Changing this forces a new resource to be created.

`PrivatePort` - (Required) The private port of the private IP address
(virtual machine) where the network traffic will be load balanced to.
Changing this forces a new resource to be created.

`PublicPort` - (Required) The public port from where the network traffic
will be load balanced from. Changing this forces a new resource to be
created.

`Protocol` - (Optional) Load balancer protocol (tcp, udp, tcp-proxy).
Changing this forces a new resource to be created.

`MemberIds` - (Required) List of instance IDs to assign to the load balancer
rule. Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The load balancer rule ID.

`Description` - The description of the load balancer rule.

## See Also

* [cloudstack_loadbalancer_rule](https://www.terraform.io/docs/providers/cloudstack/r/loadbalancer_rule.html) in the _Terraform Provider Documentation_