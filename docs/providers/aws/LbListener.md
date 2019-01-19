# Terraform::AWS::LbListener

Provides a Load Balancer Listener resource.

~> **Note:** `Terraform::AWS::AlbListener` is known as `awsLbListener`. The functionality is identical.

## Properties

`LoadBalancerArn` - (Required, Forces New Resource) The ARN of the load balancer.

`Port` - (Required) The port on which the load balancer is listening.

`Protocol` - (Optional) The protocol for connections from clients to the load balancer. Valid values are `TCP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.

`SslPolicy` - (Optional) The name of the SSL Policy for the listener. Required if `Protocol` is `HTTPS`.

`CertificateArn` - (Optional) The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the [`Terraform::AWS::LbListenerCertificate` resource](/docs/providers/aws/r/lb_listener_certificate.html).

`DefaultAction` - (Required) An Action block. Action blocks are documented below.

### DefaultAction Properties

`Type` - (Required) The type of routing action. Valid values are `forward`, `Redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.

`TargetGroupArn` - (Optional) The ARN of the Target Group to which to route traffic. Required if `Type` is `forward`.

`Redirect` - (Optional) Information for creating a redirect action. Required if `Type` is `Redirect`.

`FixedResponse` - (Optional) Information for creating an action that returns a custom HTTP response. Required if `Type` is `fixed-response`.

### Redirect Properties

`Host` - (Optional) The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.

`Path` - (Optional) The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.

`Port` - (Optional) The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.

`Protocol` - (Optional) The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.

`Query` - (Optional) The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?". Defaults to `#{query}`.

`StatusCode` - (Required) The HTTP redirect code. The redirect is either permanent (`HTTP_301`) or temporary (`HTTP_302`).

### FixedResponse Properties

`ContentType` - (Required) The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.

`MessageBody` - (Optional) The message body.

`StatusCode` - (Optional) The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

`AuthenticationRequestExtraParams` - (Optional) The query parameters to include in the redirect request to the authorization endpoint. Max: 10.

`OnUnauthenticatedRequest` - (Optional) The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`.

`Scope` - (Optional) The set of user claims to be requested from the IdP.

`SessionCookieName` - (Optional) The name of the cookie used to maintain session information.

`SessionTimeout` - (Optional) The maximum duration of the authentication session, in seconds.

`UserPoolArn` - (Required) The ARN of the Cognito user pool.

`UserPoolClientId` - (Required) The ID of the Cognito user pool client.

`UserPoolDomain` - (Required) The domain prefix or fully-qualified domain name of the Cognito user pool.

`AuthenticationRequestExtraParams` - (Optional) The query parameters to include in the redirect request to the authorization endpoint. Max: 10.

`AuthorizationEndpoint` - (Required) The authorization endpoint of the IdP.

`ClientId` - (Required) The OAuth 2.0 client identifier.

`ClientSecret` - (Required) The OAuth 2.0 client secret.

`Issuer` - (Required) The OIDC issuer identifier of the IdP.

`OnUnauthenticatedRequest` - (Optional) The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`.

`Scope` - (Optional) The set of user claims to be requested from the IdP.

`SessionCookieName` - (Optional) The name of the cookie used to maintain session information.

`SessionTimeout` - (Optional) The maximum duration of the authentication session, in seconds.

`TokenEndpoint` - (Required) The token endpoint of the IdP.

`UserInfoEndpoint` - (Required) The user info endpoint of the IdP.

### AuthenticationRequestExtraParams Properties

`Key` - (Required) The key of query parameter.

`Value` - (Required) The value of query parameter.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the listener (matches `arn`).

`Arn` - The ARN of the listener (matches `id`).

## See Also

* [aws_lb_listener](https://www.terraform.io/docs/providers/aws/r/lb_listener.html) in the _Terraform Provider Documentation_