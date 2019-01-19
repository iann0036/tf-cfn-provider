# Terraform::AWS::CognitoUserPoolClient

Provides a Cognito User Pool Client resource.

## Properties

`AllowedOauthFlows` - (Optional) List of allowed OAuth flows (code, implicit, client_credentials).

`AllowedOauthFlowsUserPoolClient` - (Optional) Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

`AllowedOauthScopes` - (Optional) List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

`CallbackUrls` - (Optional) List of allowed callback URLs for the identity providers.

`DefaultRedirectUri` - (Optional) The default redirect URI. Must be in the list of callback URLs.

`ExplicitAuthFlows` - (Optional) List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

`GenerateSecret` - (Optional) Should an application secret be generated. AWS JavaScript SDK requires this to be false.

`LogoutUrls` - (Optional) List of allowed logout URLs for the identity providers.

`Name` - (Required) The name of the application client.

`ReadAttributes` - (Optional) List of user pool attributes the application client can read from.

`RefreshTokenValidity` - (Optional) The time limit in days refresh tokens are valid for.

`SupportedIdentityProviders` - (Optional) List of provider names for the identity providers that are supported on this client.

`UserPoolId` - (Required) The user pool the client belongs to.

`WriteAttributes` - (Optional) List of user pool attributes the application client can write to.


## See Also

* [aws_cognito_user_pool_client](https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client.html) in the _Terraform Provider Documentation_