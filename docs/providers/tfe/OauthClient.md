# Terraform::Tfe::OauthClient

An OAuth Client represents the connection between an organization and a VCS
provider.

-> **Note:** This resource does not currently support creation of Bitbucket
  Server OAuth clients.

## Properties

`Organization` - (Required) Name of the organization.

`ApiUrl` - (Required) The base URL of your VCS provider's API (e.g. `https://api.github.com` or `https://ghe.example.com/api/v3`).

`HttpUrl` - (Required) The homepage of your VCS provider (e.g. `https://github.com` or `https://ghe.example.com`).

`OauthToken` - (Required) The token string you were given by your VCS provider.

`ServiceProvider` - (Required) The VCS provider being connected with. Valid options are `github`, `github_enterprise`, `bitbucket_hosted`, `gitlab_hosted`, `gitlab_community_edition`, or `gitlab_enterprise_edition`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the OAuth client.

`OauthTokenId` - The ID of the OAuth token associated with the OAuth client.

## See Also

* [tfe_oauth_client](https://www.terraform.io/docs/providers/tfe/r/oauth_client.html) in the _Terraform Provider Documentation_