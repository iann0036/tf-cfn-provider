# Terraform::AWS::ApiGatewayMethodSettings

Provides an API Gateway Method Settings, e.g. logging or monitoring.

## Properties

`RestApiId` - (Required) The ID of the REST API.

`StageName` - (Required) The name of the stage.

`MethodPath` - (Required) Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*/*` for overriding all methods in the stage.

`Settings` - (Required) The settings block, see below.


## See Also

* [aws_api_gateway_method_settings](https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings.html) in the _Terraform Provider Documentation_