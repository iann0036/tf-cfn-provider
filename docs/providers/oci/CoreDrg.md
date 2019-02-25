# Terraform::OCI::CoreDrg

This resource provides the Drg resource in Oracle Cloud Infrastructure Core service.

Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information,
see [Dynamic Routing Gateways (DRGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want
the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,
the DRG attachment, or other Networking Service components. If you're not sure which compartment
to use, put the DRG in the same compartment as the VCN. For more information about compartments
and access control, see [Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the DRG, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the DRG.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the DRG.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The DRG's Oracle ID (OCID).

`State` - The DRG's current state.

`TimeCreated` - The date and time the DRG was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_drg](https://www.terraform.io/docs/providers/oci/r/core_drg.html) in the _Terraform Provider Documentation_