# Terraform::TLS::SelfSignedCert

Generates a *self-signed* TLS certificate in PEM format, which is the typical
format used to configure TLS server software.

Self-signed certificates are generally not trusted by client software such
as web browsers. Therefore clients are likely to generate trust warnings when
connecting to a server that has a self-signed certificate. Self-signed certificates
are usually used only in development environments or apps deployed internally
to an organization.

This resource is intended to be used in conjunction with a Terraform provider
that has a resource that requires a TLS certificate, such as:

* ``aws_iam_server_certificate`` to register certificates for use with AWS *Elastic
Load Balancer*, *Elastic Beanstalk*, *CloudFront* or *OpsWorks*.

* ``heroku_cert`` to register certificates for applications deployed on Heroku.

## Properties

`KeyAlgorithm` - (Required) The name of the algorithm for the key provided
in `PrivateKeyPem`.

`PrivateKeyPem` - (Required) PEM-encoded private key data. This can be
read from a separate file using the ``file`` interpolation function. If the
certificate is being generated to be used for a throwaway development
environment or other non-critical application, the `Terraform::TLS::PrivateKey` resource
can be used to generate a TLS private key from within Terraform. Only
an irreversable secure hash of the private key will be stored in the Terraform
state.

`Subject` - (Required) The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for [`Terraform::TLS::CertRequest`](cert_request.html).

`ValidityPeriodHours` - (Required) The number of hours after initial issuing that the
certificate will become invalid.

`AllowedUses` - (Required) List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.

`DnsNames` - (Optional) List of DNS names for which a certificate is being requested.

`IpAddresses` - (Optional) List of IP addresses for which a certificate is being requested.

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

* [tls_self_signed_cert](https://www.terraform.io/docs/providers/tls/r/self_signed_cert.html) in the _Terraform Provider Documentation_