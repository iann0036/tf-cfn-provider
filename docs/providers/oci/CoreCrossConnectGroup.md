# Terraform::OCI::CoreCrossConnectGroup

This resource provides the Cross Connect Group resource in Oracle Cloud Infrastructure Core service.

Creates a new cross-connect group to use with Oracle Cloud Infrastructure
FastConnect. For more information, see
[FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

For the purposes of access control, you must provide the OCID of the
compartment where you want the cross-connect group to reside. If you're
not sure which compartment to use, put the cross-connect group in the
same compartment with your VCN. For more information about
compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the cross-connect group.
It does not have to be unique, and you can change it. Avoid entering confidential information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the cross-connect group.

`DisplayName` - The display name of A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`Id` - The cross-connect group's Oracle ID (OCID).

`State` - The cross-connect group's current state.

`TimeCreated` - The date and time the cross-connect group was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_cross_connect_group](https://www.terraform.io/docs/providers/oci/r/core_cross_connect_group.html) in the _Terraform Provider Documentation_