# Terraform::AWS::AcmCertificateValidation

This resource represents a successful validation of an ACM certificate in concert
with other resources.

Most commonly, this resource is used together with [`Terraform::AWS::Route53Record`](route53_record.html) and
[`Terraform::AWS::AcmCertificate`](acm_certificate.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

~> **WARNING:** This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.

## Properties

`CertificateArn` - (Required) The ARN of the certificate that is being validated.

`ValidationRecordFqdns` - (Optional) List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation.


## See Also

* [aws_acm_certificate_validation](https://www.terraform.io/docs/providers/aws/r/acm_certificate_validation.html) in the _Terraform Provider Documentation_