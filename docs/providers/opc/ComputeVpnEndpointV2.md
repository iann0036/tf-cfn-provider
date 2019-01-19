# Terraform::OPC::ComputeVpnEndpointV2

The ``Terraform::OPC::ComputeVpnEndpointV2`` resource creates and manages an VPN Endpoint V2 in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The name of the VPN Endpoint V2.

`CustomerVpnGateway` - (Required) The ip address of the VPN gateway in your data center through which you want to connect to the Oracle Cloud VPN gateway.

`IpNetwork` - (Required) The name of the IP network on which the cloud gateway is created by VPNaaS.

`PreSharedKey` - (Required) The pre-shared VPN key.

`ReachableRoutes` - (Required) A list of routes (CIDR prefixes) that are reachable through this VPN tunnel.

`VnicSets` - (Required) A list of vnic sets that traffics is allowed to and from.

`Description` - (Optional) A description of the VPN Endpoint V2.

`Enabled` - (Optional) Enables or disables the VPN Endpoint V2. Set to true by default.

`IkeIdentifier` - (Optional) The Internet Key Exchange (IKE) ID. If you don't specify a value, the default value is the public IP address of the cloud gateway.

`RequirePerfectForwardSecrecy` - (Optional) Boolean specifying whether Perfect Forward Secrecy is enabled. Set to true by default.

`PhaseOneSettings` - (Optional) Settings for the phase one protocol (IKE). Phase One Settings are detailed below.

`PhaseTwoSettings` - (Optional) Settings for the phase two protocol (IPSEC). Phase Two Settings are detailed below.

`Tags` - (Optional) List of tags that may be applied to the VPN Endpoint V2.

`Encryption` - (Required) IKE Encryption. `aes128`, `aes192` or `aes256`.

`Hash` - (Required) IKE Hash. `sha1`, `sha2_256` or `md5`.

`DhGroup` - (Required) Diffie-Hellman group for both IKE and ESP. `group2`, `group5`, `group14`, `group22`, `group23`, or `group24`.

`Lifetime` - (Optional) IKE Lifetime in seconds.

`Encryption` - (Required) ESP Encryption.  `aes128`, `aes192` or `aes256`.

`Hash` - (Required) ESP Hash. `sha1`, `sha2_256` or `md5`.

`Lifetime` - (Optional) IPSEC Lifetime in seconds.

`LocalGatewayIpAddress` - Public IP Address of the Local Gateway.

`LocalGatewayPrivateIpAddress` - Private IP Address of the Local Gateway.

`Uri` - The Uniform Resource Identifier for the VPN Endpoint V2.


## See Also

* [opc_compute_vpn_endpoint_v2](https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2.html) in the _Terraform Provider Documentation_