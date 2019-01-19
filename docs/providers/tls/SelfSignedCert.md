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

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CertPem` - The certificate data in PEM format.

`ValidityStartTime` - The time after which the certificate is valid, as an.

`ValidityEndTime` - The time until which the certificate is invalid, as an.

## See Also

* [tls_self_signed_cert](https://www.terraform.io/docs/providers/tls/r/self_signed_cert.html) in the _Terraform Provider Documentation_