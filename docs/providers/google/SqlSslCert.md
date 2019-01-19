# Terraform::Google::SqlSslCert

Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts).

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Instance` - (Required) The name of the Cloud SQL instance. Changing this forces a new resource to be created.

`CommonName` - (Required) The common name to be used in the certificate to identify the client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Sha1Fingerprint` - The SHA1 Fingerprint of the certificate.

`PrivateKey` - The private key associated with the client certificate.

`ServerCaCert` - The CA cert of the server this client cert was generated from.

`Cert` - The actual certificate data for this client certificate.

`CertSerialNumber` - The serial number extracted from the certificate data.

`CreateTime` - The time when the certificate was created in RFC 3339 format,.

`ExpirationTime` - The time when the certificate expires in RFC 3339 format,.

## See Also

* [google_sql_ssl_cert](https://www.terraform.io/docs/providers/google/r/sql_ssl_cert.html) in the _Terraform Provider Documentation_