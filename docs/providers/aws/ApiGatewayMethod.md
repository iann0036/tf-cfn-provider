# Terraform::AWS::ApiGatewayMethod

Provides a HTTP Method for an API Gateway Resource.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`ResourceId` - (Required) The API resource ID.

`HttpMethod` - (Required) The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

`Authorization` - (Required) The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`).

`AuthorizerId` - (Optional) The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`.

`AuthorizationScopes` - (Optional) The authorization scopes used when the authorization is `COGNITO_USER_POOLS`.

`ApiKeyRequired` - (Optional) Specify if the method requires an API key.

`RequestModels` - (Optional) A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `Terraform::AWS::ApiGatewayModel`'s `name`.

`RequestValidatorId` - (Optional) The ID of a `Terraform::AWS::ApiGatewayRequestValidator`.

`RequestParameters` - (Optional) A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header"         = true
"method.request.querystring.some-query-param" = true
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or.

`RequestParametersInJson` - **Deprecated**, use `RequestParameters` instead.


## See Also

* [aws_api_gateway_method](https://www.terraform.io/docs/providers/aws/r/api_gateway_method.html) in the _Terraform Provider Documentation_