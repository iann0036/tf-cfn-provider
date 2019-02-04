# Terraform::OpenStack::LbListenerV2

Manages a V2 listener resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`Region` argument of the provider is used. Changing this creates a new
Listener.

`Protocol` - (Required) The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

`ProtocolPort` - (Required) The port on which to listen for client traffic.
Changing this creates a new Listener.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

`LoadbalancerId` - (Required) The load balancer on which to provision this
Listener. Changing this creates a new Listener.

`Name` - (Optional) Human-readable name for the Listener. Does not have
to be unique.

`DefaultPoolId` - (Optional) The ID of the default pool with which the
Listener is associated.

`Description` - (Optional) Human-readable description for the Listener.

`ConnectionLimit` - (Optional) The maximum number of connections allowed
for the Listener.

`DefaultTlsContainerRef` - (Optional) A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

`SniContainerRefs` - (Optional) A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

`AdminStateUp` - (Optional) The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the Listener.

`Protocol` - See Properties above.

`ProtocolPort` - See Properties above.

`TenantId` - See Properties above.

`Name` - See Properties above.

`DefaultPortId` - See Properties above.

`Description` - See Properties above.

`ConnectionLimit` - See Properties above.

`DefaultTlsContainerRef` - See Properties above.

`SniContainerRefs` - See Properties above.

`AdminStateUp` - See Properties above.

## See Also

* [openstack_lb_listener_v2](https://www.terraform.io/docs/providers/openstack/r/lb_listener_v2.html) in the _Terraform Provider Documentation_