# Terraform::DigitalOcean::Certificate

Provides a DigitalOcean Certificate resource that allows you to manage
certificates for configuring TLS termination in Load Balancers.
Certificates created with this resource can be referenced in your
Load Balancer configuration via their ID. The certificate can either
be a custom one provided by you or automatically generated one with
Let's Encrypt.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique ID of the certificate.

`Name` - The name of the certificate.

`NotAfter` - The expiration date of the certificate.

`Sha1Fingerprint` - The SHA-1 fingerprint of the certificate.

## See Also

* [digitalocean_certificate](https://www.terraform.io/docs/providers/digitalocean/r/certificate.html) in the _Terraform Provider Documentation_