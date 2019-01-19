# Terraform::AWS::IotCertificate

Creates and manages an AWS IoT certificate.

## Properties

`Active` - (Required)  Boolean flag to indicate if the certificate should be active.

`Csr` - (Required) The certificate signing request. Review the [IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html) for more information on creating a certificate from a certificate signing request (CSR).


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the created AWS IoT certificate.

## See Also

* [aws_iot_certificate](https://www.terraform.io/docs/providers/aws/r/iot_certificate.html) in the _Terraform Provider Documentation_