# Terraform::AWS::ApiGatewayStage

Provides an API Gateway Stage.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`StageName` - (Required) The name of the stage.

`DeploymentId` - (Required) The ID of the deployment that the stage points to.

`AccessLogSettings` - (Optional) Enables access logs for the API stage. Detailed below.

`CacheClusterEnabled` - (Optional) Specifies whether a cache cluster is enabled for the stage.

`CacheClusterSize` - (Optional) The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

`ClientCertificateId` - (Optional) The identifier of a client certificate for the stage.

`Description` - (Optional) The description of the stage.

`DocumentationVersion` - (Optional) The version of the associated API documentation.

`Variables` - (Optional) A map that defines the stage variables.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`XrayTracingEnabled` - (Optional) Whether active tracing with X-ray is enabled. Defaults to `false`.


## See Also

* [aws_api_gateway_stage](https://www.terraform.io/docs/providers/aws/r/api_gateway_stage.html) in the _Terraform Provider Documentation_