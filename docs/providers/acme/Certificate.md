# Terraform::ACME::Certificate

The `acme_certificate` resource can be used to create and manage an ACME TLS
certificate.

-> **NOTE:** As the usage model of Terraform generally sees it as being run on
a different server than a certificate would normally be placed on, the
`acme_certifiate` resource only supports DNS challenges.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [acme_certificate](https://www.terraform.io/docs/providers/acme/r/certificate.html) in the _Terraform Provider Documentation_