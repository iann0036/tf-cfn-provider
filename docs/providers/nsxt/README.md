# VMware NSX-T Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nsxt** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

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
* `remote_auth` - (Optional) Would trigger remote authorization instead of basic
  authorization. This is required for users based on vIDM authentication.
  The default for this flag is false.


## Supported Resources

* [Terraform::NSXT::AlgorithmTypeNsService](AlgorithmTypeNsService.md)
* [Terraform::NSXT::DhcpRelayProfile](DhcpRelayProfile.md)
* [Terraform::NSXT::DhcpRelayService](DhcpRelayService.md)
* [Terraform::NSXT::DhcpServerIpPool](DhcpServerIpPool.md)
* [Terraform::NSXT::DhcpServerProfile](DhcpServerProfile.md)
* [Terraform::NSXT::EtherTypeNsService](EtherTypeNsService.md)
* [Terraform::NSXT::FirewallSection](FirewallSection.md)
* [Terraform::NSXT::IcmpTypeNsService](IcmpTypeNsService.md)
* [Terraform::NSXT::IgmpTypeNsService](IgmpTypeNsService.md)
* [Terraform::NSXT::IpBlockSubnet](IpBlockSubnet.md)
* [Terraform::NSXT::IpBlock](IpBlock.md)
* [Terraform::NSXT::IpDiscoverySwitchingProfile](IpDiscoverySwitchingProfile.md)
* [Terraform::NSXT::IpPool](IpPool.md)
* [Terraform::NSXT::IpProtocolNsService](IpProtocolNsService.md)
* [Terraform::NSXT::IpSet](IpSet.md)
* [Terraform::NSXT::L4PortSetNsService](L4PortSetNsService.md)
* [Terraform::NSXT::LbClientSslProfile](LbClientSslProfile.md)
* [Terraform::NSXT::LbCookiePersistenceProfile](LbCookiePersistenceProfile.md)
* [Terraform::NSXT::LbFastTcpApplicationProfile](LbFastTcpApplicationProfile.md)
* [Terraform::NSXT::LbFastUdpApplicationProfile](LbFastUdpApplicationProfile.md)
* [Terraform::NSXT::LbHttpApplicationProfile](LbHttpApplicationProfile.md)
* [Terraform::NSXT::LbHttpForwardingRule](LbHttpForwardingRule.md)
* [Terraform::NSXT::LbHttpMonitor](LbHttpMonitor.md)
* [Terraform::NSXT::LbHttpRequestRewriteRule](LbHttpRequestRewriteRule.md)
* [Terraform::NSXT::LbHttpResponseRewriteRule](LbHttpResponseRewriteRule.md)
* [Terraform::NSXT::LbHttpVirtualServer](LbHttpVirtualServer.md)
* [Terraform::NSXT::LbHttpsMonitor](LbHttpsMonitor.md)
* [Terraform::NSXT::LbIcmpMonitor](LbIcmpMonitor.md)
* [Terraform::NSXT::LbPassiveMonitor](LbPassiveMonitor.md)
* [Terraform::NSXT::LbPool](LbPool.md)
* [Terraform::NSXT::LbServerSslProfile](LbServerSslProfile.md)
* [Terraform::NSXT::LbService](LbService.md)
* [Terraform::NSXT::LbSourceIpPersistenceProfile](LbSourceIpPersistenceProfile.md)
* [Terraform::NSXT::LbTcpMonitor](LbTcpMonitor.md)
* [Terraform::NSXT::LbTcpVirtualServer](LbTcpVirtualServer.md)
* [Terraform::NSXT::LbUdpMonitor](LbUdpMonitor.md)
* [Terraform::NSXT::LbUdpVirtualServer](LbUdpVirtualServer.md)
* [Terraform::NSXT::LogicalDhcpPort](LogicalDhcpPort.md)
* [Terraform::NSXT::LogicalDhcpServer](LogicalDhcpServer.md)
* [Terraform::NSXT::LogicalPort](LogicalPort.md)
* [Terraform::NSXT::LogicalRouterCentralizedServicePort](LogicalRouterCentralizedServicePort.md)
* [Terraform::NSXT::LogicalRouterDownlinkPort](LogicalRouterDownlinkPort.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier0](LogicalRouterLinkPortOnTier0.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier1](LogicalRouterLinkPortOnTier1.md)
* [Terraform::NSXT::LogicalSwitch](LogicalSwitch.md)
* [Terraform::NSXT::LogicalTier0Router](LogicalTier0Router.md)
* [Terraform::NSXT::LogicalTier1Router](LogicalTier1Router.md)
* [Terraform::NSXT::MacManagementSwitchingProfile](MacManagementSwitchingProfile.md)
* [Terraform::NSXT::NatRule](NatRule.md)
* [Terraform::NSXT::NsGroup](NsGroup.md)
* [Terraform::NSXT::NsServiceGroup](NsServiceGroup.md)
* [Terraform::NSXT::QosSwitchingProfile](QosSwitchingProfile.md)
* [Terraform::NSXT::SpoofguardSwitchingProfile](SpoofguardSwitchingProfile.md)
* [Terraform::NSXT::StaticRoute](StaticRoute.md)
* [Terraform::NSXT::SwitchSecuritySwitchingProfile](SwitchSecuritySwitchingProfile.md)
* [Terraform::NSXT::VlanLogicalSwitch](VlanLogicalSwitch.md)
* [Terraform::NSXT::VmTags](VmTags.md)