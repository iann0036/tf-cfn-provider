# Terraform::OpenStack::VpnaasSiteConnectionV2

Manages a V2 Neutron IPSec site connection resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an IPSec site connection. If omitted, the `Region` argument of the provider is used. Changing this creates a new site connection.

`Name` - (Optional) The name of the connection. Changing this updates the name of the existing connection.

`TenantId` - (Optional) The owner of the connection. Required if admin wants to create a connection for another project. Changing this creates a new connection.

`Description` - (Optional) The human-readable description for the connection. Changing this updates the description of the existing connection.

`AdminStateUp` - (Optional) The administrative state of the resource. Can either be up(true) or down(false). Changing this updates the administrative state of the existing connection.

`IkepolicyId` - (Required) The ID of the IKE policy. Changing this creates a new connection.

`VpnserviceId` - (Required) The ID of the VPN service. Changing this creates a new connection.

`LocalEpGroupId` - (Optional) The ID for the endpoint group that contains private subnets for the local side of the connection. You must specify this parameter with the peer_ep_group_id parameter unless in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service. Changing this updates the existing connection.

`IpsecpolicyId` - (Required) The ID of the IPsec policy. Changing this creates a new connection.

`PeerId` - (Required) The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN. Typically, this value matches the peer_address value. Changing this updates the existing policy.

`PeerEpGroupId` - (Optional) The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection. You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.

`LocalId` - (Optional) An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic. Most often, local ID would be domain name, email address, etc. If this is not configured then the external IP address will be used as the ID.

`PeerAddress` - (Required) The peer gateway public IPv4 or IPv6 address or FQDN.

`Psk` - (Required) The pre-shared key. A valid value is any string.

`Initiator` - (Optional) A valid value is response-only or bi-directional. Default is bi-directional.

`PeerCidrs` - (Optional) Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

`Dpd` - (Optional) A dictionary with dead peer detection (DPD) protocol controls. - `Action` - (Optional) The dead peer detection (DPD) action. A valid value is clear, hold, restart, disabled, or restart-by-peer. Default value is hold.

`Action` - (Optional) The dead peer detection (DPD) action. A valid value is clear, hold, restart, disabled, or restart-by-peer. Default value is hold.

`Timeout` - (Optional) The dead peer detection (DPD) timeout in seconds. A valid value is a positive integer that is greater than the DPD interval value. Default is 120.

`Interval` - (Optional) The dead peer detection (DPD) interval, in seconds. A valid value is a positive integer. Default is 30.

`Mtu` -  (Optional) The maximum transmission unit (MTU) value to address fragmentation. Minimum value is 68 for IPv4, and 1280 for IPv6.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`TenantId` - See Properties above.

`AdminStateUp` - See Properties above.

`Description` - See Properties above.

`Dpd` - See Properties above.

`Psk` - See Properties above.

`Initiator` - See Properties above.

`PeerAddress` - See Properties above.

`PeerId` - See Properties above.

`PeerCidrs` - See Properties above.

`Mtu` - See Properties above.

`LocalId` - See Properties above.

`PeerEpGroupId` - See Properties above.

`IpsecpolicyId` - See Properties above.

`VpnserviceId` - See Properties above.

`IkepolicyId` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [openstack_vpnaas_site_connection_v2](https://www.terraform.io/docs/providers/openstack/r/vpnaas_site_connection_v2.html) in the _Terraform Provider Documentation_