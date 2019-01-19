# Terraform::AWS::LbListenerCertificate

Provides a Load Balancer Listener Certificate resource.

This resource is for additional certificates and does not replace the default certificate on the listener.

~> **Note:** `Terraform::AWS::AlbListenerCertificate` is known as `awsLbListenerCertificate`. The functionality is identical.

## Properties

`ListenerArn` - (Required, Forces New Resource) The ARN of the listener to which to attach the certificate.

`CertificateArn` - (Required, Forces New Resource) The ARN of the certificate to attach to the listener.


## See Also

* [aws_lb_listener_certificate](https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html) in the _Terraform Provider Documentation_