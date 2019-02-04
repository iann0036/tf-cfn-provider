# Terraform::Panos::PanoramaBfdProfile.

This resource allows you to add/update/delete BFD profiles on Panorama.

~> **Note:** This resource is only applicable for PAN-OS 7.1+.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`Name` - (Required) The BBFD profile's name.

`Mode` - (Optional) BFD operation mode.  Valid values are `active` (default)
or `passive`.

`MinimumTxInterval` - (Optional, int) Desired minimum TX interval in
ms.  Default is `1000`.

`MinimumRxInterval` - (Optional, int) Required minimum RX interval in
ms.  Default is `1000`.

`DetectionMultiplier` - (Optional, int) Multiplier sent to remote
system.  Default is `3`.

`HoldTime` - (Optional, int) Delay transmission and reception of control
packets in ms.

`MinimumRxTtl` - (Optional, int) Minimum accepted ttl on received BFD
packet.


## See Also

* [panos_panorama_bfd_profile.](https://www.terraform.io/docs/providers/panos/r/panorama_bfd_profile..html) in the _Terraform Provider Documentation_