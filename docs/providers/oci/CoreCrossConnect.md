# Terraform::OCI::CoreCrossConnect

This resource provides the Cross Connect resource in Oracle Cloud Infrastructure Core service.

Creates a new cross-connect. Oracle recommends you create each cross-connect in a
[CrossConnectGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CrossConnectGroup) so you can use link aggregation
with the connection.

After creating the `CrossConnect` object, you need to go the FastConnect location
and request to have the physical cable installed. For more information, see
[FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

For the purposes of access control, you must provide the OCID of the
compartment where you want the cross-connect to reside. If you're
not sure which compartment to use, put the cross-connect in the
same compartment with your VCN. For more information about
compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the cross-connect.
It does not have to be unique, and you can change it. Avoid entering confidential information.

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the cross-connect.

`CrossConnectGroupId` - (Optional) The OCID of the cross-connect group to put this cross-connect in.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FarCrossConnectOrCrossConnectGroupId` - (Optional) If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the OCID of that existing cross-connect or cross-connect group.

`IsActive` - (Optional) (Updatable) Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready.

`LocationName` - (Required) The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see [ListCrossConnectLocations](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CrossConnectLocation/ListCrossConnectLocations).  Example: `CyrusOne, Chandler, AZ`.

`NearCrossConnectOrCrossConnectGroupId` - (Optional) If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the OCID of that existing cross-connect or cross-connect group.

`PortSpeedShapeName` - (Required) The port speed for this cross-connect. To get a list of the available port speeds, see [ListCrossConnectPortSpeedShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CrossConnectPortSpeedShape/ListCrossconnectPortSpeedShapes).  Example: `10 Gbps`.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the cross-connect group.

`CrossConnectGroupId` - The OCID of the cross-connect group this cross-connect belongs to (if any).

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`Id` - The cross-connect's Oracle ID (OCID).

`LocationName` - The name of the FastConnect location where this cross-connect is installed.

`PortName` - A string identifying the meet-me room port for this cross-connect.

`PortSpeedShapeName` - The port speed for this cross-connect.  Example: `10 Gbps`.

`State` - The cross-connect's current state.

`TimeCreated` - The date and time the cross-connect was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_cross_connect](https://www.terraform.io/docs/providers/oci/r/core_cross_connect.html) in the _Terraform Provider Documentation_