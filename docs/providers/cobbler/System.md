# Terraform::Cobbler::System

Manages a System within Cobbler.

## Properties

`BootFiles` - (Optional) TFTP boot files copied into tftpboot.

`Comment` - (Optional) Free form text description.

`EnableGpxe` - (Optional) Use gPXE instead of PXELINUX.

`FetchableFiles` - (Optional) Templates for tftp or wget.

`Gateway` - (Optional) Network gateway.

`Hostname` - (Optional) Hostname of the system.

`Image` - (Optional) Parent image (if no profile is used).

`Interface` - (Optional).

`Ipv6DefaultDevice` - (Optional) IPv6 default device.

`KernelOptions` - (Optional) Kernel options. ex: selinux=permissive.

`KernelOptionsPost` - (Optional) Kernel options (post install).

`Kickstart` - (Optional) Path to kickstart template.

`KsMeta` - (Optional) Kickstart metadata.

`LdapEnabled` - (Optional) Configure LDAP at next config update.

`LdapType` - (Optional) LDAP management type.

`MgmtClasses` - (Optional) Management classes for external config management.

`MgmtParameters` - (Optional) Parameters which will be handed to your management application. Must be a valid YAML dictionary.

`MonitEnabled` - (Optional) Configure monit on this machine at next config update.

`NameServersSearch` - (Optional) Name servers search path.

`NameServers` - (Optional) Name servers.

`Name` - (Required) The name of the system.

`NetbootEnabled` - (Optional) (re)Install this machine at next boot.

`Owners` - (Optional) Owners list for authz_ownership.

`PowerAddress` - (Optional) Power management address.

`PowerId` - (Optional) Usually a plug number or blade name if power type requires it.

`PowerPass` - (Optional) Power management password.

`PowerType` - (Optional) Power management type.

`PowerUser` - (Optional) Power management user.

`Profile` - (Required) Parent profile.

`Proxy` - (Optional) Proxy URL.

`RedhatManagementKey` - (Optional) Red Hat management key.

`RedhatManagementServer` - (Optional) Red Hat management server.

`Status` - (Optional) System status (development, testing, acceptance, production).

`TemplateFiles` - (Optional) File mappings for built-in configuration management.

`TemplateRemoteKickstarts` - (Optional) template remote kickstarts.

`VirtAutoBoot` - (Optional) Auto boot the VM.

`VirtCpus` - (Optional) Number of virtual CPUs in the VM.

`VirtDiskDriver` - (Optional) The on-disk format for the virtualization disk.

`VirtFileSize` - (Optional) Virt file size.

`VirtPath` - (Optional) Path to the VM.

`VirtPxeBoot` - (Optional) Use PXE to build this VM?.

`VirtRam` - (Optional) The amount of RAM for the VM.

`VirtType` - (Optional) Virtualization technology to use: xenpv, xenfv, qemu, kvm, vmware, openvz.

### Interface Properties

`Name` - (Required) The device name of the interface. ex: eth0.

`Cnames` - (Optional) Canonical name records.

`DhcpTag` - (Optional) DHCP tag.

`DnsName` - (Optional) DNS name.

`BondingOpts` - (Optional) Options for bonded interfaces.

`BridgeOpts` - (Optional) Options for bridge interfaces.

`Gateway` - (Optional) Per-interface gateway.

`InterfaceType` - (Optional) The type of interface: na, master, slave, bond, bond_slave, bridge, bridge_slave, bonded_bridge_slave.

`InterfaceMaster` - (Optional) The master interface when slave.

`IpAddress` - (Optional) The IP address of the interface.

`Ipv6Address` - (Optional) The IPv6 address of the interface.

`Ipv6Mtu` - (Optional) The MTU of the IPv6 address.

`Ipv6StaticRoutes` - (Optional) Static routes for the IPv6 interface.

`Ipv6DefaultGateway` - (Optional) The default gateawy for the IPv6 address / interface.

`MacAddress` - (Optional) The MAC address of the interface.

`Management` - (Optional) Whether this interface is a management interface.

`Netmask` - (Optional) The IPv4 netmask of the interface.

`Static` - (Optional) Whether the interface should be static or DHCP.

`StaticRoutes` - (Optional) Static routes for the interface.

`VirtBridge` - (Optional) The virtual bridge to attach to.


## See Also

* [cobbler_system](https://www.terraform.io/docs/providers/cobbler/r/system.html) in the _Terraform Provider Documentation_