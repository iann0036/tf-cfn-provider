# Terraform::Brightbox::LoadBalancer

Provides a Brightbox Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.

## Properties

`Name` - (Optional) A label assigned to the Load Balancer.

`Policy` - (Optional) Method of load balancing to use, either `least-connections` or `round-robin`.

`CertificatePem` - (Optional) A X509 SSL certificate in PEM format. Must be included along with `certificate_key`. If intermediate certificates are required they should be concatenated after the main certificate.

`CertificatePrivateKey` - (Optional) The RSA private key used to sign the certificate in PEM format. Must be included along with `CertificatePem`.

`Sslv3` - (Optional) Allow SSL v3 to be used. Default is `false`.

`BufferSize` - (Optional) Buffer size in bytes.

`Nodes` - (Optional) An array of Server IDs.

`Listener` - (Required) An array of listener blocks. The Listener block is described below.

`Healthcheck` - (Required) A healthcheck block. The Healthcheck block is described below.

`Protocol` - (Required) Protocol of the listener. One of `tcp`, `http`, `https`, `http+ws`, `https+wss`.

`In` - (Required) Port to listen on.

`Out` - (Required) Port to pass through to.

`Timeout` - (Optional) Timeout of health check in milliseconds.

`Type` - (Required) Type of health check required: `tcp` or `http`.

`Port` - (Required) Port to connect to to check health.

`Request` - (Optional) Path used for HTTP check.

`Interval` - (Optional) Frequency of checks in milliseconds.

`ThresholdUp` - (Optional) Number of checks that must pass before connection is considered healthy.

`ThresholdDown` - (Optional) Number of checks that must fail before connection is considered unhealthy.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer.

`Status` - Current state of the load balancer. Usually `creating` or `active`.

`Locked` - True if the database server has been set to locked and cannot be deleted.

## See Also

* [brightbox_load_balancer](https://www.terraform.io/docs/providers/brightbox/r/load_balancer.html) in the _Terraform Provider Documentation_