# Terraform::AWS::DmsCertificate

Provides a DMS (Data Migration Service) certificate resource. DMS certificates can be created, deleted, and imported.

~> **Note:** All arguments including the PEM encoded certificate will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`CertificateId` - (Required) The certificate identifier.

`CertificatePem` - (Optional) The contents of the .pem X.509 certificate file for the certificate. Either `CertificatePem` or `CertificateWallet` must be set.

`CertificateWallet` - (Optional) The contents of the Oracle Wallet certificate for use with SSL. Either `CertificatePem` or `CertificateWallet` must be set.


## Return Values

### Fn::GetAtt

`CertificateArn` - The Amazon Resource Name (ARN) for the certificate.

## See Also

* [aws_dms_certificate](https://www.terraform.io/docs/providers/aws/r/dms_certificate.html) in the _Terraform Provider Documentation_