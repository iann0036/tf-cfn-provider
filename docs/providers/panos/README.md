# Palo Alto Networks Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/panos**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Optional) This is the hostname / IP address of the firewall.
* `username` - (Optional) The username to authenticate to the firewall as.
* `password` - (Optional) The password for the given username. It must be
  provided, but can also be defined via the `PANOS_PASSWORD` environment
  variable.
* `api_key` - (Optional) The API key for the firewall.  If this is given, then
  the `username` and `password` settings are ignored.
* `protocol` - (Optional) The communication protocol.  This can be set to
  either `https` or `http`.  If left unspecified, this defaults to `https`.  
* `port` - (Optional) If the port number is non-standard for the desired
  protocol, then the port number to use.
* `timeout` - (Optional) The timeout for all communications with the
  firewall.  If left unspecified, this will be set to 10 seconds.
* `logging` - (Optional) List of logging options for the provider's connection
  to the API.  If this is unspecified, then it defaults to
  `["action", "uid"]`.
* `json_config_file` - (Optional) The path to a JSON configuration file that
  contains any number of the provider's parameters.  If specified, the params
  present act as a last resort for any other provider param that has not been
  specified yet.

The list of strings supported for `logging` are as follows:

* `quiet` - Disables logging.  This is ignored, however, if other logging
  flags are present.
* `action` - Log `set` / `edit` / `delete`.
* `query` - Log `get`.
* `op` - Log `op`.
* `uid` - Log user-id envocations.
* `xpath` - Log the XPATH associated with various actions.
* `send` - Log the raw request sent to the device.  This is probably
  only useful in development of the provider itself.
* `receive` - Log the raw response sent back from the device.  This is probably
  only useful in development of the provider itself.


## Supported Resources

* [Terraform::Panos::AddressGroup](AddressGroup.md)
* [Terraform::Panos::AddressObject](AddressObject.md)
* [Terraform::Panos::AdministrativeTag](AdministrativeTag.md)
* [Terraform::Panos::DagTags](DagTags.md)
* [Terraform::Panos::Edl](Edl.md)
* [Terraform::Panos::EthernetInterface](EthernetInterface.md)
* [Terraform::Panos::GeneralSettings](GeneralSettings.md)
* [Terraform::Panos::IkeCryptoProfile](IkeCryptoProfile.md)
* [Terraform::Panos::IkeGateway](IkeGateway.md)
* [Terraform::Panos::IpsecCryptoProfile](IpsecCryptoProfile.md)
* [Terraform::Panos::IpsecTunnelProxyIdIpv4](IpsecTunnelProxyIdIpv4.md)
* [Terraform::Panos::IpsecTunnel](IpsecTunnel.md)
* [Terraform::Panos::LicenseApiKey](LicenseApiKey.md)
* [Terraform::Panos::Licensing](Licensing.md)
* [Terraform::Panos::LoopbackInterface](LoopbackInterface.md)
* [Terraform::Panos::ManagementProfile](ManagementProfile.md)
* [Terraform::Panos::NatRule](NatRule.md)
* [Terraform::Panos::PanoramaAddressGroup](PanoramaAddressGroup.md)
* [Terraform::Panos::PanoramaAddressObject](PanoramaAddressObject.md)
* [Terraform::Panos::PanoramaAdministrativeTag](PanoramaAdministrativeTag.md)
* [Terraform::Panos::PanoramaDeviceGroupEntry](PanoramaDeviceGroupEntry.md)
* [Terraform::Panos::PanoramaDeviceGroup](PanoramaDeviceGroup.md)
* [Terraform::Panos::PanoramaEdl](PanoramaEdl.md)
* [Terraform::Panos::PanoramaEthernetInterface](PanoramaEthernetInterface.md)
* [Terraform::Panos::PanoramaIkeCryptoProfile](PanoramaIkeCryptoProfile.md)
* [Terraform::Panos::PanoramaIkeGateway](PanoramaIkeGateway.md)
* [Terraform::Panos::PanoramaIpsecCryptoProfile](PanoramaIpsecCryptoProfile.md)
* [Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4](PanoramaIpsecTunnelProxyIdIpv4.md)
* [Terraform::Panos::PanoramaIpsecTunnel](PanoramaIpsecTunnel.md)
* [Terraform::Panos::PanoramaLoopbackInterface](PanoramaLoopbackInterface.md)
* [Terraform::Panos::PanoramaManagementProfile](PanoramaManagementProfile.md)
* [Terraform::Panos::PanoramaNatRule](PanoramaNatRule.md)
* [Terraform::Panos::PanoramaSecurityPolicy](PanoramaSecurityPolicy.md)
* [Terraform::Panos::PanoramaSecurityRuleGroup](PanoramaSecurityRuleGroup.md)
* [Terraform::Panos::PanoramaServiceGroup](PanoramaServiceGroup.md)
* [Terraform::Panos::PanoramaServiceObject](PanoramaServiceObject.md)
* [Terraform::Panos::PanoramaStaticRouteIpv4](PanoramaStaticRouteIpv4.md)
* [Terraform::Panos::PanoramaTemplateEntry](PanoramaTemplateEntry.md)
* [Terraform::Panos::PanoramaTemplateStackEntry](PanoramaTemplateStackEntry.md)
* [Terraform::Panos::PanoramaTemplateStack](PanoramaTemplateStack.md)
* [Terraform::Panos::PanoramaTemplateVariable](PanoramaTemplateVariable.md)
* [Terraform::Panos::PanoramaTemplate](PanoramaTemplate.md)
* [Terraform::Panos::PanoramaTunnelInterface](PanoramaTunnelInterface.md)
* [Terraform::Panos::PanoramaVirtualRouterEntry](PanoramaVirtualRouterEntry.md)
* [Terraform::Panos::PanoramaVirtualRouter](PanoramaVirtualRouter.md)
* [Terraform::Panos::PanoramaVlanInterface](PanoramaVlanInterface.md)
* [Terraform::Panos::PanoramaZoneEntry](PanoramaZoneEntry.md)
* [Terraform::Panos::PanoramaZone](PanoramaZone.md)
* [Terraform::Panos::SecurityPolicy](SecurityPolicy.md)
* [Terraform::Panos::SecurityRuleGroup](SecurityRuleGroup.md)
* [Terraform::Panos::ServiceGroup](ServiceGroup.md)
* [Terraform::Panos::ServiceObject](ServiceObject.md)
* [Terraform::Panos::StaticRouteIpv4](StaticRouteIpv4.md)
* [Terraform::Panos::Telemetry](Telemetry.md)
* [Terraform::Panos::TunnelInterface](TunnelInterface.md)
* [Terraform::Panos::VirtualRouterEntry](VirtualRouterEntry.md)
* [Terraform::Panos::VirtualRouter](VirtualRouter.md)
* [Terraform::Panos::VlanInterface](VlanInterface.md)
* [Terraform::Panos::ZoneEntry](ZoneEntry.md)
* [Terraform::Panos::Zone](Zone.md)