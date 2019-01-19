# Terraform::AWS::IamOpenidConnectProvider

Provides an IAM OpenID Connect provider.

## Properties

`Url` - (Required) The URL of the identity provider. Corresponds to the _iss_ claim.

`ClientIdList` - (Required) A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.).

`ThumbprintList` - (Required) A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).


## Return Values

### Fn::GetAtt

`Arn` - The ARN assigned by AWS for this provider.

## See Also

* [aws_iam_openid_connect_provider](https://www.terraform.io/docs/providers/aws/r/iam_openid_connect_provider.html) in the _Terraform Provider Documentation_