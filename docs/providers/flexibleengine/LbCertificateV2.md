# Terraform::FlexibleEngine::LbCertificateV2

Manages a V2 certificate resource within FlexibleEngine.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB certificate. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
LB certificate.

`Name` - (Optional) Human-readable name for the Certificate. Does not have
to be unique.

`Description` - (Optional) Human-readable description for the Certificate.

`Domain` - (Optional) The domain of the Certificate.

`PrivateKey` - (Required) The private encrypted key of the Certificate, PEM format.

`Certificate` - (Required) The public encrypted key of the Certificate, PEM format.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Domain` - See Properties above.

`PrivateKey` - See Properties above.

`Certificate` - See Properties above.

`UpdateTime` - Indicates the update time.

`CreateTime` - Indicates the creation time.

## See Also

* [flexibleengine_lb_certificate_v2](https://www.terraform.io/docs/providers/flexibleengine/r/lb_certificate_v2.html) in the _Terraform Provider Documentation_