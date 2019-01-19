# Terraform::OCI::EmailSender

This resource provides the Sender resource in Oracle Cloud Infrastructure Email service.

Creates a sender for a tenancy in a given compartment.

## Properties

TBC

## Return Values

### Fn::GetAtt

`EmailAddress` - The email address of the sender.

`Id` - The unique OCID of the sender.

`IsSpf` - Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/emaildeliveryoverview.htm#spf).

`State` - The current status of the approved sender.

`TimeCreated` - The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

## See Also

* [oci_email_sender](https://www.terraform.io/docs/providers/oci/r/email_sender.html) in the _Terraform Provider Documentation_