# Terraform::BIGIP::LtmVirtualServer

`Terraform::BIGIP::LtmVirtualServer` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the virtual server.

`Port` - (Required) Listen port for the virtual server.

`Destination` - (Required) Destination IP.

`Pool` - (Optional) Default pool name.

`Mask` - (Optional) Mask can either be in CIDR notation or decimal, i.e.: 24 or 255.255.255.0. A CIDR mask of 0 is the same as 0.0.0.0.

`SourceAddressTranslation` - (Optional) Can be either omitted for none or the values automap or snat.

`TranslateAddress` - Enables or disables address translation for the virtual server. Turn address translation off for a virtual server if you want to use the virtual server to load balance connections to any address. This option is useful when the system is load balancing devices that have the same IP address.

`TranslatePort` - Enables or disables port translation. Turn port translation off for a virtual server if you want to use the virtual server to load balance connections to any service.

`IpProtocol` - (Optional) Specify the IP protocol to use with the the virtual server (all, tcp, or udp are valid).

`Profiles` - (Optional) List of profiles associated both client and server contexts on the virtual server. This includes protocol, ssl, http, etc.

`ClientProfiles` - (Optional) List of client context profiles associated on the virtual server. Not mutually exclusive with profiles and server_profiles.

`ServerProfiles` - (Optional) List of server context profiles associated on the virtual server. Not mutually exclusive with profiles and client_profiles.

`Source` -  (Optional) Specifies an IP address or network from which the virtual server will accept traffic.

`Rules` - (Optional) The iRules you want run on this virtual server. iRules help automate the intercepting, processing, and routing of application traffic.

`Snatpool` - (Optional) Specifies the name of an existing SNAT pool that you want the virtual server to use to implement selective and intelligent SNATs. DEPRECATED - see Virtual Server Property Groups source-address-translation.

`Vlans` - (Optional) The virtual server is enabled/disabled on this set of VLANs. See vlans-disabled and vlans-enabled.

`VlansEnabled` - (Optional Bool) Enables the virtual server on the VLANs specified by the VLANs option.

`VlansDisabled` - (Optional Bool) Disables the virtual server on the VLANs specified by the VLANs option.

`PersistenceProfiles` - (Optional) List of persistence profiles associated with the Virtual Server.

`FallbackPersistenceProfile` - (Optional) Specifies a fallback persistence profile for the Virtual Server to use when the default persistence profile is not available.


## See Also

* [bigip_ltm_virtual_server](https://www.terraform.io/docs/providers/bigip/r/ltm_virtual_server.html) in the _Terraform Provider Documentation_