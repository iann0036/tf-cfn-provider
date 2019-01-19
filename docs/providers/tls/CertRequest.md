# Terraform::TLS::CertRequest

Generates a *Certificate Signing Request* (CSR) in PEM format, which is the
typical format used to request a certificate from a certificate authority.

This resource is intended to be used in conjunction with a Terraform provider
for a particular certificate authority in order to provision a new certificate.
This is a *logical resource*, so it contributes only to the current Terraform
state and does not create any external managed resources.

~> **Compatibility Note** From Terraform 0.7.0 to 0.7.4 this resource was
converted to a data source, and the resource form of it was deprecated. This
turned out to be a design error since a cert request includes a random number
in the form of the signature nonce, and so the data source form of this
resource caused non-convergent configuration. The data source form is no longer
supported as of Terraform 0.7.5 and any users should return to using the
resource form.

## Properties

`KeyAlgorithm` - (Required) The name of the algorithm for the key provided in `PrivateKeyPem`.

`PrivateKeyPem` - (Required) PEM-encoded private key data. This can be read from a separate file using the ``file`` interpolation function. Only an irreversable secure hash of the private key will be stored in the Terraform state.

`Subject` - (Required) The subject for which a certificate is being requested. This is a nested configuration block whose structure is described below.

`DnsNames` - (Optional) List of DNS names for which a certificate is being requested.

`IpAddresses` - (Optional) List of IP addresses for which a certificate is being requested.


## Return Values

### Fn::GetAtt

`CertRequestPem` - The certificate request data in PEM format.

## See Also

* [tls_cert_request](https://www.terraform.io/docs/providers/tls/r/cert_request.html) in the _Terraform Provider Documentation_