# Terraform::OCI::EmailSuppression

This resource provides the Suppression resource in Oracle Cloud Infrastructure Email service.

Adds recipient email addresses to the suppression list for a tenancy.
Addresses added to the suppression list via the API are denoted as
"MANUAL" in the `reason` field. *Note:* All email addresses added to the
suppression list are normalized to include only lowercase letters.

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.

`EmailAddress` - (Required) The recipient email address of the suppression.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.

`EmailAddress` - The email address of the suppression.

`Id` - The unique OCID of the suppression.

`Reason` - The reason that the email address was suppressed. For more information on the types of bounces, see [Suppression List](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).

`TimeCreated` - The date and time a recipient's email address was added to the suppression list, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

## See Also

* [oci_email_suppression](https://www.terraform.io/docs/providers/oci/r/email_suppression.html) in the _Terraform Provider Documentation_