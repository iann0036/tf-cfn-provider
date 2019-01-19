# Terraform::AWS::AppsyncGraphqlApi

Provides an AppSync GraphQL API.

## Properties

`AuthenticationType` - (Required) The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`.

`Name` - (Required) A user-supplied name for the GraphqlApi.

`LogConfig` - (Optional) Nested argument containing logging configuration. Defined below.

`OpenidConnectConfig` - (Optional) Nested argument containing OpenID Connect configuration. Defined below.

`UserPoolConfig` - (Optional) The Amazon Cognito User Pool configuration. Defined below.


## Return Values

### Fn::GetAtt

`Id` - API ID.

`Arn` - The ARN.

`Uris` - Map of URIs associated with the API. e.g. `uris["GRAPHQL"] = https://ID.appsync-api.REGION.amazonaws.com/graphql`.

## See Also

* [aws_appsync_graphql_api](https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api.html) in the _Terraform Provider Documentation_