# Terraform::NSXT::QosSwitchingProfile

Provides a resource to configure Qos switching profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this qos switching profile.

`ClassOfService` - (Optional) Class of service.

`DscpTrusted` - (Optional) Trust mode for DSCP (False by default).

`DscpPriority` - (Optional) DSCP Priority (0-63).

`IngressRateShaper` - (Optional) Ingress rate shaper configuration:.

`Enabled` - (Optional) Whether this rate shaper is enabled.

`AverageBwMbps` - (Optional) Average Bandwidth in MBPS.

`PeakBwMbps` - (Optional) Peak Bandwidth in MBPS.

`BurstSize` - (Optional) Burst size in bytes.

`EgressRateShaper` - (Optional) Egress rate shaper configuration:.

`Enabled` - (Optional) Whether this rate shaper is enabled.

`AverageBwMbps` - (Optional) Average Bandwidth in MBPS.

`PeakBwMbps` - (Optional) Peak Bandwidth in MBPS.

`BurstSize` - (Optional) Burst size in bytes.

`IngressBroadcastRateShaper` - (Optional) Ingress rate shaper configuration:.

`Enabled` - (Optional) Whether this rate shaper is enabled.

`AverageBwKbps` - (Optional) Average Bandwidth in KBPS.

`PeakBwKbps` - (Optional) Peak Bandwidth in KBPS.

`BurstSize` - (Optional) Burst size in bytes.


## Return Values

### Fn::GetAtt

`Id` - ID of the QoS switching profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_qos_switching_profile](https://www.terraform.io/docs/providers/nsxt/r/qos_switching_profile.html) in the _Terraform Provider Documentation_