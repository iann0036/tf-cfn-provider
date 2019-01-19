# Terraform::TLS::LocallySignedCert

Generates a TLS certificate using a *Certificate Signing Request* (CSR) and
signs it with a provided certificate authority (CA) private key.

Locally-signed certificates are generally only trusted by client software when
setup to use the provided CA. They are normally used in development environments
or when deployed internally to an organization.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CertPem` - The certificate data in PEM format.

`ValidityStartTime` - The time after which the certificate is valid, as an.

`ValidityEndTime` - The time until which the certificate is invalid, as an.

## See Also

* [tls_locally_signed_cert](https://www.terraform.io/docs/providers/tls/r/locally_signed_cert.html) in the _Terraform Provider Documentation_