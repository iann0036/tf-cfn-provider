# Terraform::AWS::AcmCertificate

The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.

It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a [`Terraform::AWS::AcmCertificateValidation`](acm_certificate_validation.html) resource for this.

Most commonly, this resource is used to together with [`Terraform::AWS::Route53Record`](route53_record.html) and
[`Terraform::AWS::AcmCertificateValidation`](acm_certificate_validation.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

Domain validation through E-Mail is also supported but should be avoided as it requires a manual step outside
of Terraform.

It's recommended to specify `create_before_destroy = true` in a [lifecycle][1] block to replace a certificate
which is currently in use (eg, by [`Terraform::AWS::LbListener`](lb_listener.html)).

## Properties

`DomainName` - (Required) A domain name for which the certificate should be issued
* `SubjectAlternativeNames` - (Optional) A list of domains that should be SANs in the issued certificate
* `ValidationMethod` - (Required) Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

`SubjectAlternativeNames` - (Optional) A list of domains that should be SANs in the issued certificate
* `ValidationMethod` - (Required) Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

`ValidationMethod` - (Required) Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

`PrivateKey` - (Required) The certificate's PEM-formatted private key
* `CertificateBody` - (Required) The certificate's PEM-formatted public key
* `CertificateChain` - (Optional) The certificate's PEM-formatted chain.

`CertificateBody` - (Required) The certificate's PEM-formatted public key
* `CertificateChain` - (Optional) The certificate's PEM-formatted chain.

`CertificateChain` - (Optional) The certificate's PEM-formatted chain.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the certificate.

`Arn` - The ARN of the certificate.

`DomainName` - The domain to be validated.

`DomainValidationOptions` - A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if `DNS`-validation was used.

`ValidationEmails` - A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.

`ResourceRecordName` - The name of the DNS record to create to validate the certificate.

`ResourceRecordType` - The type of DNS record to create.

`ResourceRecordValue` - The value the DNS record needs to have.

## See Also

* [aws_acm_certificate](https://www.terraform.io/docs/providers/aws/r/acm_certificate.html) in the _Terraform Provider Documentation_