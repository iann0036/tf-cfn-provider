# Terraform::AWS::ApiGatewayRequestValidator

Manages an API Gateway Request Validator.

## Properties

`Name` - (Required) The name of the request validator.

`RestApiId` - (Required) The ID of the associated Rest API.

`ValidateRequestBody` - (Optional) Boolean whether to validate request body. Defaults to `false`.

`ValidateRequestParameters` - (Optional) Boolean whether to validate request parameters. Defaults to `false`.


## See Also

* [aws_api_gateway_request_validator](https://www.terraform.io/docs/providers/aws/r/api_gateway_request_validator.html) in the _Terraform Provider Documentation_