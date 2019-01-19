# Terraform::OCI::EmailSuppression

This resource provides the Suppression resource in Oracle Cloud Infrastructure Email service.

Adds recipient email addresses to the suppression list for a tenancy.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`EmailAddress` - The email address of the suppression.

`Id` - The unique OCID of the suppression.

`Reason` - The reason that the email address was suppressed. For more information on the types of bounces, see [Suppresion List](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/emaildeliveryoverview.htm#suppressionlist).

`TimeCreated` - The date and time a recipient's email address was added to the suppression list, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

## See Also

* [oci_email_suppression](https://www.terraform.io/docs/providers/oci/r/email_suppression.html) in the _Terraform Provider Documentation_