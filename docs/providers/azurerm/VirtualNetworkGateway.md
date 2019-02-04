# Terraform::AzureRM::VirtualNetworkGateway

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

-> **Note:** Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)

## Properties

`Name` - (Required) The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

`Location` - (Required) The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

`Type` - (Required) The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

`VpnType` - (Optional) The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

`EnableBgp` - (Optional) If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

`ActiveActive` - (Optional) If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

`DefaultLocalNetworkGatewayId` -  (Optional) The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.

`Sku` - (Required) Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2` and `VpnGw3`
and depend on the `Type` and `VpnType` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### IpConfiguration Properties

`Name` - (Optional) A user-defined name of the IP configuration. Defaults to
`vnetGatewayConfig`.

`PrivateIpAddressAllocation` - (Optional) Defines how the private IP address
of the gateways virtual interface is assigned. Valid options are `Static` or
`Dynamic`. Defaults to `Dynamic`.

`SubnetId` - (Required) The ID of the gateway subnet of a virtual network in
which the virtual network gateway will be created. It is mandatory that
the associated subnet is named `GatewaySubnet`. Therefore, each virtual
network can contain at most a single Virtual Network Gateway.

`PublicIpAddressId` - (Optional) The ID of the public ip address to associate
with the Virtual Network Gateway.

### VpnClientConfiguration Properties

`AddressSpace` - (Required) The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.

`RootCertificate` - (Optional) One or more `RootCertificate` blocks which are
defined below. These root certificates are used to sign the client certificate
used by the VPN clients to connect to the gateway.
This setting is incompatible with the use of `RadiusServerAddress` and `RadiusServerSecret`.

`RevokedCertificate` - (Optional) One or more `RevokedCertificate` blocks which
are defined below.
This setting is incompatible with the use of `RadiusServerAddress` and `RadiusServerSecret`.

`RadiusServerAddress` - (Optional) The address of the Radius server.
This setting is incompatible with the use of `RootCertificate` and `RevokedCertificate`.

`RadiusServerSecret` - (Optional) The secret used by the Radius server.
This setting is incompatible with the use of `RootCertificate` and `RevokedCertificate`.

`VpnClientProtocols` - (Optional) List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.

`Asn` - (Optional) The Autonomous System Number (ASN) to use as part of the BGP.

`PeeringAddress` - (Optional) The BGP peer IP address of the virtual network
gateway. This address is needed to configure the created gateway as a BGP Peer
on the on-premises VPN devices. The IP address must be part of the subnet of
the Virtual Network Gateway. Changing this forces a new resource to be created.

`PeerWeight` - (Optional) The weight added to routes which have been learned
through BGP peering. Valid values can be between `0` and `100`.

### RootCertificate Properties

`Name` - (Required) A user-defined name of the root certificate.

`PublicCertData` - (Required) The public certificate of the root certificate
authority. The certificate must be provided in Base-64 encoded X.509 format
(PEM). In particular, this argument *must not* include the
`-----BEGIN CERTIFICATE-----` or `-----END CERTIFICATE-----` markers.

`Name` - (Required) A user-defined name of the revoked certificate.

`PublicCertData` - (Required) The SHA1 thumbprint of the certificate to be
revoked.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Network Gateway.

## See Also

* [azurerm_virtual_network_gateway](https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway.html) in the _Terraform Provider Documentation_