# Terraform::OCI::EmailSender

This resource provides the Sender resource in Oracle Cloud Infrastructure Email service.

Creates a sender for a tenancy in a given compartment.

## Properties

`CompartmentId` - (Required) The OCID of the compartment that contains the sender.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`EmailAddress` - (Required) The email address of the sender.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID for the compartment.

`IsSpf` - Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`TimeCreated` - The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

`State` - The current status of the approved sender.

`EmailAddress` - The email address of the sender.

`Id` - The unique OCID of the sender.

## See Also

* [oci_email_sender](https://www.terraform.io/docs/providers/oci/r/email_sender.html) in the _Terraform Provider Documentation_