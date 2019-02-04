# Terraform::ACME::Certificate

The `Terraform::ACME::Certificate` resource can be used to create and manage an ACME TLS
certificate.

-> **NOTE:** As the usage model of Terraform generally sees it as being run on
a different server than a certificate would normally be placed on, the
`Terraform::ACME::Certifiate` resource only supports DNS challenges.

## Properties

`CommonName` - The certificate's common name, the primary domain that the
certificate will be recognized for. Required when not specifying a CSR.

`SubjectAlternativeNames` - The certificate's subject alternative names,
domains that this certificate will also be recognized for. Only valid when not
specifying a CSR.

`KeyType` - The key type for the certificate's private key. Can be one of:
`P256` and `P384` (for ECDSA keys of respective length) or `2048`, `4096`, and
`8192` (for RSA keys of respective length). Required when not specifying a
CSR. The default is `2048` (RSA key of 2048 bits).

`CertificateRequestPem` - A pre-created certificate request, such as one
from [`tls_cert_request`][tls-cert-request], or one from an external source,
in PEM format.  Either this, or the in-resource request options (`CommonName`,
`KeyType`, and optionally `SubjectAlternativeNames`) need to be specified.


## See Also

* [acme_certificate](https://www.terraform.io/docs/providers/acme/r/certificate.html) in the _Terraform Provider Documentation_