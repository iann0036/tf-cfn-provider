# Terraform::Panos::Bgp

This resource allows you to add/update/delete a virtual router's
BGP configuration.

**Important Note:**  When it comes to BGP configuration, PAN-OS requires that
BGP itself first be configured before you can add other BGP sub-config, such
as dampening profiles or peer groups.  Since every BGP resource must reference a
virtual router, the key to accomplishing this is by pointing the `VirtualRouter`
param for each BGP sub-config to `Terraform::Panos::Bgp.foo.virtualRouter` instead
of `Terraform::Panos::VirtualRouter.bar.name`.

## Properties

`VirtualRouter` - (Required) The virtual router to add this BGP
configuration to.

`Enable` - (Optional, bool) Enable BGP or not (default: `true`).

`RouterId` - (Optional) Router ID of this BGP instance.

`AsNumber` - (Optional) Local AS number.

`BfdProfile` - (Optional, PAN-OS 7.1+) BFD configuration.

`RejectDefaultRoute` - (Optional, bool) Do not learn default route from
BGP (default: `true`).

`InstallRoute` - (Optional, bool) Populate BGP learned route to global
route table.

`AggregateMed` - (Optional, bool) Aggregate route only if they have
same MED attributes (default: `true`).

`DefaultLocalPreference` - (Optional) Default local preference (default:
`"100"`).

`AsFormat` - (Optional) AS format.  Valid values are `"2-byte"` (default)
or `"4-byte"`.

`AlwaysCompareMed` - (Optional, bool) Always compare MEDs.

`DeterministicMedComparison` - (Optional, bool) Deterministic MED
comparison (default: `true`).

`EcmpMultiAs` - (Optional, bool) Support multiple AS in ECMP.

`EnforceFirstAs` - (Optional, bool) Enforce First AS for EBGP (default:
`true`).

`EnableGracefulRestart` - (Optional, bool) Enable graceful restart
(default: `true`).

`StaleRouteTime` - (Optional, int) Time to remove stale routes after
peer restart, in seconds (default: `120`).

`LocalRestartTime` - (Optional, int) Local restart time to advertise to
peer, in seconds (default: `120`).

`MaxPeerRestartTime` - (Optional, int) Maximum of peer restart time
accepted, in seconds (default: `120`).

`ReflectorClusterId` - (Optional) Route reflector cluster ID.

`ConfederationMemberAs` - (Optional) Confederation requires
member-AS number.

`AllowRedistributeDefaultRoute` - (Optional, bool) Allow redistribute
default route to BGP.


## See Also

* [panos_bgp](https://www.terraform.io/docs/providers/panos/r/bgp.html) in the _Terraform Provider Documentation_