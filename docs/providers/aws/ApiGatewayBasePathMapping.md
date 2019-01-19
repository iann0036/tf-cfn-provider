# Terraform::AWS::ApiGatewayBasePathMapping

Connects a custom domain name registered via `Terraform::AWS::ApiGatewayDomainName`
with a deployed API so that its methods can be called via the
custom domain name.

## Properties

`DomainName` - (Required) The already-registered domain name to connect the API to.

`ApiId` - (Required) The id of the API to connect.

`StageName` - (Optional) The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

`BasePath` - (Optional) Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.


## See Also

* [aws_api_gateway_base_path_mapping](https://www.terraform.io/docs/providers/aws/r/api_gateway_base_path_mapping.html) in the _Terraform Provider Documentation_