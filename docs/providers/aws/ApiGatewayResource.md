# Terraform::AWS::ApiGatewayResource

Provides an API Gateway Resource.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`ParentId` - (Required) The ID of the parent API resource.

`PathPart` - (Required) The last path segment of this API resource.


## Return Values

### Fn::GetAtt

`Id` - The resource's identifier.

`Path` - The complete path for this API resource, including all parent paths.

## See Also

* [aws_api_gateway_resource](https://www.terraform.io/docs/providers/aws/r/api_gateway_resource.html) in the _Terraform Provider Documentation_