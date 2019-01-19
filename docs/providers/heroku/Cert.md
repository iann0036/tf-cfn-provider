# Terraform::Heroku::Cert

Provides a Heroku SSL certificate resource. It allows to set a given certificate for a Heroku app.

## Properties

`App` - (Required) The Heroku app to add to.

`CertificateChain` - (Required) The certificate chain to add.

`PrivateKey` - (Required) The private key for a given certificate chain.


## Return Values

### Fn::GetAtt

`Id` - The ID of the add-on.

`Cname` - The CNAME for the SSL endpoint.

`Name` - The name of the SSL certificate.

## See Also

* [heroku_cert](https://www.terraform.io/docs/providers/heroku/r/cert.html) in the _Terraform Provider Documentation_