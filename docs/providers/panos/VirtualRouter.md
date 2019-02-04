# Terraform::Panos::VirtualRouter

This resource allows you to add/update/delete virtual routers.

**Note** - The `default` virtual router may be configured with this resource,
however it will not be deleted from the firewall.  It will only be unexported
from the vsys that it is currently imported in, and any interfaces imported
into the virtual router will be removed.

This resource has some overlap with the `Terraform::Panos::VirtualRouterEntry`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::VirtualRouter` spec does not define the
`Interfaces` field.

## Properties

`Name` - (Required) The virtual router's name.

`Vsys` - (Required) The vsys that will use this virtual router.  This should
be something like `vsys1` or `vsys3`.

`Interfaces` - (Optional) List of interfaces that should use this virtual
router.

`StaticDist` - (Optional) Admin distance - Static (default: `10`).

`StaticIpv6Dist` - (Optional) Admin distance - Static IPv6 (default: `10`).

`OspfIntDist` - (Optional) Admin distance - OSPF Int (default: `30`).

`OspfExtDist` - (Optional) Admin distance - OSPF Ext (default: `110`).

`Ospfv3IntDist` - (Optional) Admin distance - OSPFv3 Int (default:
`30`).

`Ospfv3ExtDist` - (Optional) Admin distance - OSPFv3 Ext (default:
`110`).

`IbgpDist` - (Optional) Admin distance - IBGP (default: `200`).

`EbgpDist` - (Optional) Admin distance - EBGP (default: `20`).

`RipDist` - (Optional) Admin distance - RIP (default: `120`).


## See Also

* [panos_virtual_router](https://www.terraform.io/docs/providers/panos/r/virtual_router.html) in the _Terraform Provider Documentation_