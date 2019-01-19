# Terraform::OPC::LbaasCertificate

The `Terraform::OPC::LbaasCertificate` resource creates and manages an Load Balancer Classic TLS/SSL Digital Certificate.

Server certificates are used to secure the connection between clients and the load balancers. Trusted certificates are used to secure the connection between the load balancer and the origin servers in the server pool.

## Properties

`Name` - (Required) The name of the Certificate.

`CertificateBody` - (Required) The Certificate data in PEM format.

`Type` - (Required) Sets the Certificate Type. `TRUSTED` or `SERVER`.

`CertificateChain` - (Optional) PEM encoded bodies of all certificates in the chain up to and including the CA certificate. This is not need when the certificate is self signed.

`PrivateKey` - (Optional) The private key data in PEM format. Only required for Server Certificates.


## See Also

* [opc_lbaas_certificate](https://www.terraform.io/docs/providers/opc/r/lbaas_certificate.html) in the _Terraform Provider Documentation_