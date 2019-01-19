# Terraform::AWS::ApiGatewayIntegrationResponse

Provides an HTTP Method Integration Response for an API Gateway Resource.

-> **Note:** Depends on having `Terraform::AWS::ApiGatewayIntegration` inside your rest api. To ensure this
you might need to add an explicit `depends_on` for clean runs.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`ResourceId` - (Required) The API resource ID.

`HttpMethod` - (Required) The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

`StatusCode` - (Required) The HTTP status code.

`SelectionPattern` - (Optional) Specifies the regular expression pattern used to choose an integration response based on the response from the backend. Setting this to `-` makes the integration the default one. If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched. For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

`ResponseTemplates` - (Optional) A map specifying the templates used to transform the integration response body.

`ResponseParameters` - (Optional) A map of response parameters that can be read from the backend response. For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,.

`ResponseParametersInJson` - **Deprecated**, use `ResponseParameters` instead.

`ContentHandling` - (Optional) Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.


## See Also

* [aws_api_gateway_integration_response](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration_response.html) in the _Terraform Provider Documentation_