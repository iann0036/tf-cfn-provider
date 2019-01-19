# Terraform::AWS::AcmpcaCertificateAuthority

Provides a resource to manage AWS Certificate Manager Private Certificate Authorities (ACM PCA Certificate Authorities).

~> **NOTE:** Creating this resource will leave the certificate authority in a `PENDING_CERTIFICATE` status, which means it cannot yet issue certificates. To complete this setup, you must fully sign the certificate authority CSR available in the `certificate_signing_request` attribute and import the signed certificate outside of Terraform. Terraform can support another resource to manage that workflow automatically in the future.

## Properties

`CertificateAuthorityConfiguration` - (Required) Nested argument containing algorithms and certificate subject information. Defined below.

`Enabled` - (Optional) Whether the certificate authority is enabled or disabled. Defaults to `true`.

`RevocationConfiguration` - (Optional) Nested argument containing revocation configuration. Defined below.

`Tags` - (Optional) Specifies a key-value map of user-defined tags that are attached to the certificate authority.

`Type` - (Optional) The type of the certificate authority. Currently, this must be `SUBORDINATE`.


## See Also

* [aws_acmpca_certificate_authority](https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority.html) in the _Terraform Provider Documentation_