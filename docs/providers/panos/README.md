# Palo Alto Networks Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/panos**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Optional) This is the hostname / IP address of the firewall.  It
  must be provided, but can also be defined via the `PANOS_HOSTNAME`
  environment variable.
* `username` - (Optional) The username to authenticate to the firewall as.  It
  must be provided, but can also be defined via the `PANOS_USERNAME`
  environment variable.
* `password` - (Optional) The password for the given username. It must be
  provided, but can also be defined via the `PANOS_PASSWORD` environment
  variable.
* `api_key` - (Optional) The API key for the firewall.  If this is given, then
  the `username` and `password` settings are ignored.  This can also be defined
  via the `PANOS_API_KEY` environment variable.
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

* [Terraform::Panos::AddressGroup](docs/providers/panos/AddressGroup.md)
* [Terraform::Panos::AddressObject](docs/providers/panos/AddressObject.md)
* [Terraform::Panos::AdministrativeTag](docs/providers/panos/AdministrativeTag.md)
* [Terraform::Panos::DagTags](docs/providers/panos/DagTags.md)
* [Terraform::Panos::Edl](docs/providers/panos/Edl.md)
* [Terraform::Panos::EthernetInterface](docs/providers/panos/EthernetInterface.md)
* [Terraform::Panos::GeneralSettings](docs/providers/panos/GeneralSettings.md)
* [Terraform::Panos::IkeCryptoProfile](docs/providers/panos/IkeCryptoProfile.md)
* [Terraform::Panos::IkeGateway](docs/providers/panos/IkeGateway.md)
* [Terraform::Panos::IpsecCryptoProfile](docs/providers/panos/IpsecCryptoProfile.md)
* [Terraform::Panos::IpsecTunnelProxyIdIpv4](docs/providers/panos/IpsecTunnelProxyIdIpv4.md)
* [Terraform::Panos::IpsecTunnel](docs/providers/panos/IpsecTunnel.md)
* [Terraform::Panos::LicenseApiKey](docs/providers/panos/LicenseApiKey.md)
* [Terraform::Panos::Licensing](docs/providers/panos/Licensing.md)
* [Terraform::Panos::LoopbackInterface](docs/providers/panos/LoopbackInterface.md)
* [Terraform::Panos::ManagementProfile](docs/providers/panos/ManagementProfile.md)
* [Terraform::Panos::NatRule](docs/providers/panos/NatRule.md)
* [Terraform::Panos::PanoramaAddressGroup](docs/providers/panos/PanoramaAddressGroup.md)
* [Terraform::Panos::PanoramaAddressObject](docs/providers/panos/PanoramaAddressObject.md)
* [Terraform::Panos::PanoramaAdministrativeTag](docs/providers/panos/PanoramaAdministrativeTag.md)
* [Terraform::Panos::PanoramaDeviceGroupEntry](docs/providers/panos/PanoramaDeviceGroupEntry.md)
* [Terraform::Panos::PanoramaDeviceGroup](docs/providers/panos/PanoramaDeviceGroup.md)
* [Terraform::Panos::PanoramaEdl](docs/providers/panos/PanoramaEdl.md)
* [Terraform::Panos::PanoramaEthernetInterface](docs/providers/panos/PanoramaEthernetInterface.md)
* [Terraform::Panos::PanoramaIkeCryptoProfile](docs/providers/panos/PanoramaIkeCryptoProfile.md)
* [Terraform::Panos::PanoramaIkeGateway](docs/providers/panos/PanoramaIkeGateway.md)
* [Terraform::Panos::PanoramaIpsecCryptoProfile](docs/providers/panos/PanoramaIpsecCryptoProfile.md)
* [Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4](docs/providers/panos/PanoramaIpsecTunnelProxyIdIpv4.md)
* [Terraform::Panos::PanoramaIpsecTunnel](docs/providers/panos/PanoramaIpsecTunnel.md)
* [Terraform::Panos::PanoramaLoopbackInterface](docs/providers/panos/PanoramaLoopbackInterface.md)
* [Terraform::Panos::PanoramaManagementProfile](docs/providers/panos/PanoramaManagementProfile.md)
* [Terraform::Panos::PanoramaNatRule](docs/providers/panos/PanoramaNatRule.md)
* [Terraform::Panos::PanoramaSecurityPolicy](docs/providers/panos/PanoramaSecurityPolicy.md)
* [Terraform::Panos::PanoramaSecurityRuleGroup](docs/providers/panos/PanoramaSecurityRuleGroup.md)
* [Terraform::Panos::PanoramaServiceGroup](docs/providers/panos/PanoramaServiceGroup.md)
* [Terraform::Panos::PanoramaServiceObject](docs/providers/panos/PanoramaServiceObject.md)
* [Terraform::Panos::PanoramaStaticRouteIpv4](docs/providers/panos/PanoramaStaticRouteIpv4.md)
* [Terraform::Panos::PanoramaTemplateEntry](docs/providers/panos/PanoramaTemplateEntry.md)
* [Terraform::Panos::PanoramaTemplateStackEntry](docs/providers/panos/PanoramaTemplateStackEntry.md)
* [Terraform::Panos::PanoramaTemplateStack](docs/providers/panos/PanoramaTemplateStack.md)
* [Terraform::Panos::PanoramaTemplateVariable](docs/providers/panos/PanoramaTemplateVariable.md)
* [Terraform::Panos::PanoramaTemplate](docs/providers/panos/PanoramaTemplate.md)
* [Terraform::Panos::PanoramaTunnelInterface](docs/providers/panos/PanoramaTunnelInterface.md)
* [Terraform::Panos::PanoramaVirtualRouterEntry](docs/providers/panos/PanoramaVirtualRouterEntry.md)
* [Terraform::Panos::PanoramaVirtualRouter](docs/providers/panos/PanoramaVirtualRouter.md)
* [Terraform::Panos::PanoramaVlanInterface](docs/providers/panos/PanoramaVlanInterface.md)
* [Terraform::Panos::PanoramaZoneEntry](docs/providers/panos/PanoramaZoneEntry.md)
* [Terraform::Panos::PanoramaZone](docs/providers/panos/PanoramaZone.md)
* [Terraform::Panos::SecurityPolicy](docs/providers/panos/SecurityPolicy.md)
* [Terraform::Panos::SecurityRuleGroup](docs/providers/panos/SecurityRuleGroup.md)
* [Terraform::Panos::ServiceGroup](docs/providers/panos/ServiceGroup.md)
* [Terraform::Panos::ServiceObject](docs/providers/panos/ServiceObject.md)
* [Terraform::Panos::StaticRouteIpv4](docs/providers/panos/StaticRouteIpv4.md)
* [Terraform::Panos::Telemetry](docs/providers/panos/Telemetry.md)
* [Terraform::Panos::TunnelInterface](docs/providers/panos/TunnelInterface.md)
* [Terraform::Panos::VirtualRouterEntry](docs/providers/panos/VirtualRouterEntry.md)
* [Terraform::Panos::VirtualRouter](docs/providers/panos/VirtualRouter.md)
* [Terraform::Panos::VlanInterface](docs/providers/panos/VlanInterface.md)
* [Terraform::Panos::ZoneEntry](docs/providers/panos/ZoneEntry.md)
* [Terraform::Panos::Zone](docs/providers/panos/Zone.md)