# Terraform::TLS::LocallySignedCert

Generates a TLS certificate using a *Certificate Signing Request* (CSR) and
signs it with a provided certificate authority (CA) private key.

Locally-signed certificates are generally only trusted by client software when
setup to use the provided CA. They are normally used in development environments
or when deployed internally to an organization.

## Properties

`CertRequestPem` - (Required) PEM-encoded request certificate data.

`CaKeyAlgorithm` - (Required) The name of the algorithm for the key provided
in `CaPrivateKeyPem`.

`CaPrivateKeyPem` - (Required) PEM-encoded private key data for the CA.
This can be read from a separate file using the ``file`` interpolation
function.

`CaCertPem` - (Required) PEM-encoded certificate data for the CA.

`ValidityPeriodHours` - (Required) The number of hours after initial issuing that the
certificate will become invalid.

`AllowedUses` - (Required) List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.

`EarlyRenewalHours` - (Optional) If set, the resource will consider the certificate to
have expired the given number of hours before its actual expiry time. This can be useful
to deploy an updated certificate in advance of the expiration of the current certificate.
Note however that the old certificate remains valid until its true expiration time, since
this resource does not (and cannot) support certificate revocation. Note also that this
advance update can only be performed should the Terraform configuration be applied during the
early renewal period.

`IsCaCertificate` - (Optional) Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to `false`, meaning that the certificate does not represent
a certificate authority.


## Return Values

### Fn::GetAtt

`CertPem` - The certificate data in PEM format.

`ValidityStartTime` - The time after which the certificate is valid, as an.

`ValidityEndTime` - The time until which the certificate is invalid, as an.

## See Also

* [tls_locally_signed_cert](https://www.terraform.io/docs/providers/tls/r/locally_signed_cert.html) in the _Terraform Provider Documentation_