# Terraform::AWS::LbListenerRule

Provides a Load Balancer Listener Rule resource.

~> **Note:** `Terraform::AWS::AlbListenerRule` is known as `awsLbListenerRule`. The functionality is identical.

## Properties

`ListenerArn` - (Required, Forces New Resource) The ARN of the listener to which to attach the rule.

`Priority` - (Optional) The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.

`Action` - (Required) An Action block. Action blocks are documented below.

`Condition` - (Required) A Condition block. Condition blocks are documented below.

### AuthenticationRequestExtraParams Properties

`Key` - (Required) The key of query parameter.

`Value` - (Required) The value of query parameter.

### AuthenticateCognito Properties

`UserPoolArn` - (Required) The ARN of the Cognito user pool.

`UserPoolClientId` - (Required) The ID of the Cognito user pool client.

`UserPoolDomain` - (Required) The domain prefix or fully-qualified domain name of the Cognito user pool.

### AuthenticateOidc Properties

`AuthenticationRequestExtraParams` - (Optional) The query parameters to include in the redirect request to the authorization endpoint. Max: 10.

`OnUnauthenticatedRequest` - (Optional) The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`.

`Scope` - (Optional) The set of user claims to be requested from the IdP.

`SessionCookieName` - (Optional) The name of the cookie used to maintain session information.

`SessionTimeout` - (Optional) The maximum duration of the authentication session, in seconds.

`AuthorizationEndpoint` - (Required) The authorization endpoint of the IdP.

`ClientId` - (Required) The OAuth 2.0 client identifier.

`ClientSecret` - (Required) The OAuth 2.0 client secret.

`Issuer` - (Required) The OIDC issuer identifier of the IdP.

`TokenEndpoint` - (Required) The token endpoint of the IdP.

`UserInfoEndpoint` - (Required) The user info endpoint of the IdP.

### Redirect Properties

`Host` - (Optional) The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.

`Path` - (Optional) The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.

`Port` - (Optional) The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.

`Protocol` - (Optional) The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.

`Query` - (Optional) The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?". Defaults to `#{query}`.

### Action Properties

`Type` - (Required) The type of routing action. Valid values are `forward`, `Redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.

`TargetGroupArn` - (Optional) The ARN of the Target Group to which to route traffic. Required if `Type` is `forward`.

`Redirect` - (Optional) Information for creating a redirect action. Required if `Type` is `Redirect`.

`FixedResponse` - (Optional) Information for creating an action that returns a custom HTTP response. Required if `Type` is `fixed-response`.

`AuthenticateCognito` - (Optional) Information for creating an authenticate action using Cognito. Required if `Type` is `authenticate-cognito`.

`AuthenticateOidc` - (Optional) Information for creating an authenticate action using OIDC. Required if `Type` is `authenticate-oidc`.

### FixedResponse Properties

`StatusCode` - (Optional) The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

`ContentType` - (Required) The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.

`MessageBody` - (Optional) The message body.

### Condition Properties

`Field` - (Required) The name of the field. Must be one of `path-pattern` for path based routing or `host-header` for host based routing.

`Values` - (Required) The path patterns to match. A maximum of 1 can be defined.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the rule (matches `arn`).

`Arn` - The ARN of the rule (matches `id`).

## See Also

* [aws_lb_listener_rule](https://www.terraform.io/docs/providers/aws/r/lb_listener_rule.html) in the _Terraform Provider Documentation_