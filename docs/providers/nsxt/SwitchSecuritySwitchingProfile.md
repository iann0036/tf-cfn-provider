# Terraform::NSXT::SwitchSecuritySwitchingProfile

Provides a resource to configure switch security switching profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this qos switching profile.

`BlockNonIp` - (Optional) Indicates whether blocking of all traffic except IP/(G)ARP/BPDU is enabled.

`BlockClientDhcp` - (Optional) Indicates whether DHCP client blocking is enabled.

`BlockServerDhcp` - (Optional) Indicates whether DHCP server blocking is enabled.

`BpduFilterEnabled` - (Optional) Indicates whether BPDU filter is enabled.

`BpduFilterWhitelist` - (Optional) Set of allowed MAC addresses to be excluded from BPDU filtering, if enabled.

`RateLimits` - (Optional) Rate limit definitions for broadcast and multicast traffic. * `Enabled` - (Optional) Whether rate limitimg is enabled. * `RxBroadcast` - (Optional) Incoming broadcast traffic limit in packets per second. * `RxMulticast` - (Optional) Incoming multicast traffic limit in packets per second. * `TxBroadcast` - (Optional) Outgoing broadcast traffic limit in packets per second. * `TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.

`Enabled` - (Optional) Whether rate limitimg is enabled. * `RxBroadcast` - (Optional) Incoming broadcast traffic limit in packets per second. * `RxMulticast` - (Optional) Incoming multicast traffic limit in packets per second. * `TxBroadcast` - (Optional) Outgoing broadcast traffic limit in packets per second. * `TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.

`RxBroadcast` - (Optional) Incoming broadcast traffic limit in packets per second. * `RxMulticast` - (Optional) Incoming multicast traffic limit in packets per second. * `TxBroadcast` - (Optional) Outgoing broadcast traffic limit in packets per second. * `TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.

`RxMulticast` - (Optional) Incoming multicast traffic limit in packets per second. * `TxBroadcast` - (Optional) Outgoing broadcast traffic limit in packets per second. * `TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.

`TxBroadcast` - (Optional) Outgoing broadcast traffic limit in packets per second. * `TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.

`TxMulticast` - (Optional) Outgoing multicast traffic limit in packets per second.


## Return Values

### Fn::GetAtt

`Id` - ID of the switch security switching profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_switch_security_switching_profile](https://www.terraform.io/docs/providers/nsxt/r/switch_security_switching_profile.html) in the _Terraform Provider Documentation_