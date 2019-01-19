# VMware NSX-T Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nsxt**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (Required) The host name or IP address of the NSX-T manager.
* `username` - (Required) The user name to connect to the NSX-T manager as.
* `password` - (Required) The password for the NSX-T manager user.
* `client_auth_cert_file` - (Optional) The path to a certificate file for
  certificate authorization.
* `client_auth_key_file` - (Optional) The path to a private key file for the
  certificate supplied to `client_auth_cert_file`.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to disable
  SSL certificate verification. This should be used with care as it could allow
  an attacker to intercept your auth token. If omitted, default value is
  `false`.
* `ca_file` - (Optional) The path to an optional CA certificate file for SSL
  validation. Can also be specified with the `NSXT_CA_FILE` environment
  variable.
* `max_retries` - (Optional) The maximum number of retires before failing an API
  request.
* `retry_min_delay` - (Optional) The minimum delay, in milliseconds, between
  retires made to the API. Default:`500`.
* `retry_max_delay` - (Optional) The maximum delay, in milliseconds, between
  retires made to the API. Default:`5000`.
* `retry_on_status_codes` - (Optional) A list of HTTP status codes to retry on.
  By default, the provider will retry on HTTP error 429 (too many requests),
  essentially retrying on throttled connections.


## Supported Resources

* [Terraform::NSXT::AlgorithmTypeNsService](docs/providers/nsxt/AlgorithmTypeNsService.md)
* [Terraform::NSXT::DhcpRelayProfile](docs/providers/nsxt/DhcpRelayProfile.md)
* [Terraform::NSXT::DhcpRelayService](docs/providers/nsxt/DhcpRelayService.md)
* [Terraform::NSXT::DhcpServerIpPool](docs/providers/nsxt/DhcpServerIpPool.md)
* [Terraform::NSXT::DhcpServerProfile](docs/providers/nsxt/DhcpServerProfile.md)
* [Terraform::NSXT::EtherTypeNsService](docs/providers/nsxt/EtherTypeNsService.md)
* [Terraform::NSXT::FirewallSection](docs/providers/nsxt/FirewallSection.md)
* [Terraform::NSXT::IcmpTypeNsService](docs/providers/nsxt/IcmpTypeNsService.md)
* [Terraform::NSXT::IgmpTypeNsService](docs/providers/nsxt/IgmpTypeNsService.md)
* [Terraform::NSXT::IpBlockSubnet](docs/providers/nsxt/IpBlockSubnet.md)
* [Terraform::NSXT::IpBlock](docs/providers/nsxt/IpBlock.md)
* [Terraform::NSXT::IpDiscoverySwitchingProfile](docs/providers/nsxt/IpDiscoverySwitchingProfile.md)
* [Terraform::NSXT::IpPool](docs/providers/nsxt/IpPool.md)
* [Terraform::NSXT::IpProtocolNsService](docs/providers/nsxt/IpProtocolNsService.md)
* [Terraform::NSXT::IpSet](docs/providers/nsxt/IpSet.md)
* [Terraform::NSXT::L4PortSetNsService](docs/providers/nsxt/L4PortSetNsService.md)
* [Terraform::NSXT::LbClientSslProfile](docs/providers/nsxt/LbClientSslProfile.md)
* [Terraform::NSXT::LbCookiePersistenceProfile](docs/providers/nsxt/LbCookiePersistenceProfile.md)
* [Terraform::NSXT::LbFastTcpApplicationProfile](docs/providers/nsxt/LbFastTcpApplicationProfile.md)
* [Terraform::NSXT::LbFastUdpApplicationProfile](docs/providers/nsxt/LbFastUdpApplicationProfile.md)
* [Terraform::NSXT::LbHttpApplicationProfile](docs/providers/nsxt/LbHttpApplicationProfile.md)
* [Terraform::NSXT::LbHttpForwardingRule](docs/providers/nsxt/LbHttpForwardingRule.md)
* [Terraform::NSXT::LbHttpMonitor](docs/providers/nsxt/LbHttpMonitor.md)
* [Terraform::NSXT::LbHttpRequestRewriteRule](docs/providers/nsxt/LbHttpRequestRewriteRule.md)
* [Terraform::NSXT::LbHttpResponseRewriteRule](docs/providers/nsxt/LbHttpResponseRewriteRule.md)
* [Terraform::NSXT::LbHttpVirtualServer](docs/providers/nsxt/LbHttpVirtualServer.md)
* [Terraform::NSXT::LbHttpsMonitor](docs/providers/nsxt/LbHttpsMonitor.md)
* [Terraform::NSXT::LbIcmpMonitor](docs/providers/nsxt/LbIcmpMonitor.md)
* [Terraform::NSXT::LbPassiveMonitor](docs/providers/nsxt/LbPassiveMonitor.md)
* [Terraform::NSXT::LbPool](docs/providers/nsxt/LbPool.md)
* [Terraform::NSXT::LbServerSslProfile](docs/providers/nsxt/LbServerSslProfile.md)
* [Terraform::NSXT::LbService](docs/providers/nsxt/LbService.md)
* [Terraform::NSXT::LbSourceIpPersistenceProfile](docs/providers/nsxt/LbSourceIpPersistenceProfile.md)
* [Terraform::NSXT::LbTcpMonitor](docs/providers/nsxt/LbTcpMonitor.md)
* [Terraform::NSXT::LbTcpVirtualServer](docs/providers/nsxt/LbTcpVirtualServer.md)
* [Terraform::NSXT::LbUdpMonitor](docs/providers/nsxt/LbUdpMonitor.md)
* [Terraform::NSXT::LbUdpVirtualServer](docs/providers/nsxt/LbUdpVirtualServer.md)
* [Terraform::NSXT::LogicalDhcpPort](docs/providers/nsxt/LogicalDhcpPort.md)
* [Terraform::NSXT::LogicalDhcpServer](docs/providers/nsxt/LogicalDhcpServer.md)
* [Terraform::NSXT::LogicalPort](docs/providers/nsxt/LogicalPort.md)
* [Terraform::NSXT::LogicalRouterCentralizedServicePort](docs/providers/nsxt/LogicalRouterCentralizedServicePort.md)
* [Terraform::NSXT::LogicalRouterDownlinkPort](docs/providers/nsxt/LogicalRouterDownlinkPort.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier0](docs/providers/nsxt/LogicalRouterLinkPortOnTier0.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier1](docs/providers/nsxt/LogicalRouterLinkPortOnTier1.md)
* [Terraform::NSXT::LogicalSwitch](docs/providers/nsxt/LogicalSwitch.md)
* [Terraform::NSXT::LogicalTier0Router](docs/providers/nsxt/LogicalTier0Router.md)
* [Terraform::NSXT::LogicalTier1Router](docs/providers/nsxt/LogicalTier1Router.md)
* [Terraform::NSXT::MacManagementSwitchingProfile](docs/providers/nsxt/MacManagementSwitchingProfile.md)
* [Terraform::NSXT::NatRule](docs/providers/nsxt/NatRule.md)
* [Terraform::NSXT::NsGroup](docs/providers/nsxt/NsGroup.md)
* [Terraform::NSXT::NsServiceGroup](docs/providers/nsxt/NsServiceGroup.md)
* [Terraform::NSXT::QosSwitchingProfile](docs/providers/nsxt/QosSwitchingProfile.md)
* [Terraform::NSXT::SpoofguardSwitchingProfile](docs/providers/nsxt/SpoofguardSwitchingProfile.md)
* [Terraform::NSXT::StaticRoute](docs/providers/nsxt/StaticRoute.md)
* [Terraform::NSXT::SwitchSecuritySwitchingProfile](docs/providers/nsxt/SwitchSecuritySwitchingProfile.md)
* [Terraform::NSXT::VmTags](docs/providers/nsxt/VmTags.md)