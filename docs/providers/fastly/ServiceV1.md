# Terraform::Fastly::ServiceV1

Provides a Fastly Service, representing the configuration for a website, app,
API, or anything else to be served through Fastly. A Service encompasses Domains
and Backends.

The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly's guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Service.

`ActiveVersion` - The currently active version of your Fastly.

`Director` - Set of Directors. See above for details.

`ResponseObject` - Set of Response Object configurations. See above for details.

`DefaultTtl` - Default TTL.

`ForceDestroy` - Force the destruction of the Service on delete.

## See Also

* [fastly_service_v1](https://www.terraform.io/docs/providers/fastly/r/service_v1.html) in the _Terraform Provider Documentation_