# Terraform::AWS::ApiGatewayMethodResponse

Provides an HTTP Method Response for an API Gateway Resource.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`ResourceId` - (Required) The API resource ID.

`HttpMethod` - (Required) The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

`StatusCode` - (Required) The HTTP status code.

`ResponseModels` - (Optional) A map of the API models used for the response's content type.

`ResponseParameters` - (Optional) A map of response parameters that can be sent to the caller. For example: `response_parameters = { "method.response.header.X-Some-Header" = true }` would define that the header `X-Some-Header` can be provided on the response.

`ResponseParametersInJson` - **Deprecated**, use `ResponseParameters` instead.


## See Also

* [aws_api_gateway_method_response](https://www.terraform.io/docs/providers/aws/r/api_gateway_method_response.html) in the _Terraform Provider Documentation_