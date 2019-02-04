# Terraform::AWS::ApiGatewayAuthorizer

Provides an API Gateway Authorizer.

## Properties

`AuthorizerUri` - (Optional, required for type `TOKEN`/`REQUEST`) The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`.

`Name` - (Required) The name of the authorizer.

`RestApiId` - (Required) The ID of the associated REST API.

`IdentitySource` - (Optional) The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`.

`Type` - (Optional) The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

`AuthorizerCredentials` - (Optional) The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

`AuthorizerResultTtlInSeconds` - (Optional) The TTL of cached authorizer results in seconds.
Defaults to `300`.

`IdentityValidationExpression` - (Optional) A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

`ProviderArns` - (Optional, required for type `COGNITO_USER_POOLS`) A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.


## See Also

* [aws_api_gateway_authorizer](https://www.terraform.io/docs/providers/aws/r/api_gateway_authorizer.html) in the _Terraform Provider Documentation_