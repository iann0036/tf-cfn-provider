# Terraform::Panos::PanoramaIkeGateway

This resource allows you to add/update/delete Panorama IKE gateways
for both templates and template stacks.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`Name` - (Required) The object's name.

`Version` - (Optional, PAN-OS 7.0+) The IKE gateway version.  Valid values are `ikev1`, (the default), `ikev2`, or `ikev2-preferred`.  For PAN-OS 6.1, only `ikev1` is acceptable.

`EnableIpv6` - (Optional, PAN-OS 7.0+, bool) Enable IPv6 or not.

`Disabled` - (Optional, PAN-OS 7.0+, bool) Set to `true` to disable.

`PeerIpType` - (Optional) The peer IP type.  Valid values are `ip`, `dynamic`, and `fqdn` (PANOS 8.1+).

`PeerIpValue` - (Optional) The peer IP value.

`Interface` - (Required) The interface.

`LocalIpAddressType` - (Optional) The local IP address type.  Valid values for this are `ip`, or an empty string (the default) which is `None`.

`LocalIpAddressValue` - (Optional) The IP address if `LocalIpAddressType` is set to `ip`.

`AuthType` - (Optional) The auth type.  Valid values are `pre-shared-key` (the default), or `certificate`.

`PreSharedKey` - (Optional) The pre-shared key value.

`LocalIdType` - (Optional) The local ID type.  Valid values are `ipaddr`, `fqdn`, `ufqdn`, `keyid`, or `dn`.

`LocalIdValue` - (Optional) The local ID value.

`PeerIdType` - (Optional) The peer ID type.  Valid values are `ipaddr`, `fqdn`, `ufqdn`, `keyid`, or `dn`.

`PeerIdValue` - (Optional) The peer ID value.

`PeerIdCheck` - (Optional) Enable peer ID wildcard match for certificate authentication.  Valid values are `exact` or `wildcard`.

`LocalCert` - (Optional) The local certificate name.

`CertEnableHashAndUrl` - (Optional, PAN-OS 7.0+, bool) Set to `true` to use hash-and-url for local certificate.

`CertBaseUrl` - (Optional) The host and directory part of URL for local certificates.

`CertUseManagementAsSource` - (Optional, PAN-OS 7.0+, bool) Set to `true` to use management interface IP as source to retrieve http certificates.

`CertPermitPayloadMismatch` - (Optional, bool) Set to `true` to permit peer identification and certificate payload identification mismatch.

`CertProfile` - (Optional) Profile for certificate valdiation during IKE negotiation.

`CertEnableStrictValidation` - (Optional, bool) Set to `true` to enable strict validation of peer's extended key use.

`EnablePassiveMode` - (Optional, bool) Set to `true` to enable passive mode (responder only).

`EnableNatTraversal` - (Optional, bool) Set to `true` to enable NAT traversal.

`NatTraversalKeepAlive` - (Optional, int) Sending interval for NAT keep-alive packets (in seconds).

`NatTraversalEnableUdpChecksum` - (Optional, bool) Set to `true` to enable NAT traversal UDP checksum.

`EnableFragmentation` - (Optional, bool) Set to `true` to enable fragmentation.

`Ikev1ExchangeMode` - (Optional) The IKEv1 exchange mode.

`Ikev1CryptoProfile` - (Optional) IKEv1 crypto profile.

`EnableDeadPeerDetection` - (Optional, bool) Set to `true` to enable dead peer detection.

`DeadPeerDetectionInterval` - (Optional, int) The dead peer detection interval.

`DeadPeerDetectionRetry` - (Optional, int) Number of retries before disconnection.

`Ikev2CryptoProfile` - (Optional, PAN-OS 7.0+) IKEv2 crypto profile.

`Ikev2CookieValidation` - (Optional, PAN-OS 7.0+) Set to `true` to require cookie.

`EnableLivenessCheck` - (Optional, , PAN-OS 7.0+bool) Set to `true` to enable sending empty information liveness check message.

`LivenessCheckInterval` - (Optional, , PAN-OS 7.0+int) Delay interval before sending probing packets (in seconds).


## See Also

* [panos_panorama_ike_gateway](https://www.terraform.io/docs/providers/panos/r/panorama_ike_gateway.html) in the _Terraform Provider Documentation_