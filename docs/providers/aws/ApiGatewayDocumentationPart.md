# Terraform::AWS::ApiGatewayDocumentationPart

Provides a settings of an API Gateway Documentation Part.

## Properties

`Location` - (Required) The location of the targeted API entity of the to-be-created documentation part. See below.

`Properties` - (Required) A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

`RestApiId` - (Required) The ID of the associated Rest API.


## See Also

* [aws_api_gateway_documentation_part](https://www.terraform.io/docs/providers/aws/r/api_gateway_documentation_part.html) in the _Terraform Provider Documentation_