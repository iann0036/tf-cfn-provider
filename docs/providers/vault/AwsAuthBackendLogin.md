# Terraform::Vault::AwsAuthBackendLogin

Logs into a Vault server using an AWS auth backend. Login can be
accomplished using a signed identity request from IAM or using ec2
instance metadata. For more information, see the [Vault
documentation](https://www.vaultproject.io/docs/auth/aws.html).

## Properties

`Backend` - (Optional) The unique name of the AWS auth backend. Defaults to
'aws'.

`Role` - (Optional) The name of the AWS auth backend role to create tokens
against.

`Identity` - (Optional) The base64-encoded EC2 instance identity document to
authenticate with. Can be retrieved from the EC2 metadata server.

`Signature` - (Optional) The base64-encoded SHA256 RSA signature of the
instance identity document to authenticate with, with all newline characters
removed. Can be retrieved from the EC2 metadata server.

`Pkcs7` - (Optional) The PKCS#7 signature of the identity document to
authenticate with, with all newline characters removed. Can be retrieved from
the EC2 metadata server.

`Nonce` - (Optional) The unique nonce to be used for login requests. Can be
set to a user-specified value, or will contain the server-generated value
once a token is issued. EC2 instances can only acquire a single token until
the whitelist is tidied again unless they keep track of this nonce.

`IamHttpRequestMethod` - (Optional) The HTTP method used in the signed IAM
request.

`IamRequestUrl` - (Optional) The base64-encoded HTTP URL used in the signed
request.

`IamRequestBody` - (Optional) The base64-encoded body of the signed
request.

`IamRequestHeaders` - (Optional) The base64-encoded, JSON serialized
representation of the GetCallerIdentity HTTP request headers.


## Return Values

### Fn::GetAtt

`LeaseDuration` - The duration in seconds the token will be valid, relative.

`LeaseStartTime` - The approximate time at which the token was created,.

`Renewable` - Set to true if the token can be extended through renewal.

`Metadata` - A map of information returned by the Vault server about the.

`AuthType` - The authentication type used to generate this token.

`Policies` - The Vault policies assigned to this token.

`Accessor` - The token's accessor.

`ClientToken` - The token returned by Vault.

## See Also

* [vault_aws_auth_backend_login](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login.html) in the _Terraform Provider Documentation_