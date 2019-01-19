# Terraform::Rancher::Certificate

Provides a Rancher Certificate resource. This can be used to create certificates for rancher environments and retrieve their information.

## Properties

`Name` - (Required) The name of the certificate.

`Description` - (Optional) A certificate description.

`EnvironmentId` - (Required) The ID of the environment to create the certificate for.

`Cert` - (Required) The certificate content.

`CertChain` - (Optional) The certificate chain.

`Key` - (Required) The certificate key.


## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

`Cn` - The certificate CN.

`Algorithm` - The certificate algorithm.

`CertFingerprint` - The certificate fingerprint.

`ExpiresAt` - The certificate expiration date.

`IssuedAt` - The certificate creation date.

`Issuer` - The certificate issuer.

`KeySize` - The certificate key size.

`SerialNumber` - The certificate serial number.

`SubjectAlternativeNames` - The list of certificate Subject Alternative Names.

`Version` - The certificate version.

## See Also

* [rancher_certificate](https://www.terraform.io/docs/providers/rancher/r/certificate.html) in the _Terraform Provider Documentation_