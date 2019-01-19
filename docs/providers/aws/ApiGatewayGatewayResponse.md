# Terraform::AWS::ApiGatewayGatewayResponse

Provides an API Gateway Gateway Response for a REST API Gateway.

## Properties

`RestApiId` - (Required) The string identifier of the associated REST API.

`ResponseType` - (Required) The response type of the associated GatewayResponse.

`StatusCode` - (Optional) The HTTP status code of the Gateway Response.

`ResponseParameters` - (Optional) A map specifying the templates used to transform the response body.

`ResponseTemplates` - (Optional) A map specifying the parameters (paths, query strings and headers) of the Gateway Response.


## See Also

* [aws_api_gateway_gateway_response](https://www.terraform.io/docs/providers/aws/r/api_gateway_gateway_response.html) in the _Terraform Provider Documentation_