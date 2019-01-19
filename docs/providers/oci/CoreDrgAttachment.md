# Terraform::OCI::CoreDrgAttachment

This resource provides the Drg Attachment resource in Oracle Cloud Infrastructure Core service.

Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time,
and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more
information about DRGs, see
[Dynamic Routing Gateways (DRGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm).

You may optionally specify a *display name* for the attachment, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the same compartment
as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment containing the DRG attachment.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DrgId` - The OCID of the DRG.

`Id` - The DRG attachment's Oracle ID (OCID).

`RouteTableId` - The OCID of the route table the DRG attachment is using. For information about why you would associate a route table with a DRG attachment, see [Advanced Scenario: Transit Routing](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

`State` - The DRG attachment's current state.

`TimeCreated` - The date and time the DRG attachment was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN.

## See Also

* [oci_core_drg_attachment](https://www.terraform.io/docs/providers/oci/r/core_drg_attachment.html) in the _Terraform Provider Documentation_