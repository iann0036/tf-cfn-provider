# Terraform::OCI::IdentitySmtpCredential

This resource provides the Smtp Credential resource in Oracle Cloud Infrastructure Identity service.

Creates a new SMTP credential for the specified user. An SMTP credential has an SMTP user name and an SMTP password.
You must specify a *description* for the SMTP credential (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateSmtpCredential](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/SmtpCredentialSummary/UpdateSmtpCredential).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Description` - The description you assign to the SMTP credential. Does not have to be unique, and it's changeable.

`Id` - The OCID of the SMTP credential.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`Password` - The SMTP password.

`State` - The credential's current state.

`TimeCreated` - Date and time the `SmtpCredential` object was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`TimeExpires` - Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user the SMTP credential belongs to.

`Username` - The SMTP user name.

## See Also

* [oci_identity_smtp_credential](https://www.terraform.io/docs/providers/oci/r/identity_smtp_credential.html) in the _Terraform Provider Documentation_