# Terraform::Tfe::OauthClient

An OAuth Client represents the connection between an organization and a VCS
provider.

-> **Note:** This resource does not currently support creation of Bitbucket
  Server OAuth clients.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the OAuth client.

`OauthTokenId` - The ID of the OAuth token associated with the OAuth client.

## See Also

* [tfe_oauth_client](https://www.terraform.io/docs/providers/tfe/r/oauth_client.html) in the _Terraform Provider Documentation_