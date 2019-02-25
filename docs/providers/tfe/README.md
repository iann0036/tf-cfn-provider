# Terraform Enterprise Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/tfe** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `hostname` - (Optional) The Terraform Enterprise hostname to connect to.
  Defaults to `app.terraform.io`.
* `token` - (Optional) The token used to authenticate with Terraform Enterprise.
  Only set this argument when running in a Terraform Enterprise workspace; for
  CLI usage, omit the token from the configuration and set it as `credentials`
  in the [CLI config file](/docs/commands/cli-config.html#credentials). See
  [Authentication](#authentication) above for more.


## Supported Resources

* [Terraform::Tfe::OauthClient](OauthClient.md)
* [Terraform::Tfe::OrganizationToken](OrganizationToken.md)
* [Terraform::Tfe::Organization](Organization.md)
* [Terraform::Tfe::PolicySet](PolicySet.md)
* [Terraform::Tfe::SentinelPolicy](SentinelPolicy.md)
* [Terraform::Tfe::SshKey](SshKey.md)
* [Terraform::Tfe::TeamAccess](TeamAccess.md)
* [Terraform::Tfe::TeamMember](TeamMember.md)
* [Terraform::Tfe::TeamMembers](TeamMembers.md)
* [Terraform::Tfe::TeamToken](TeamToken.md)
* [Terraform::Tfe::Team](Team.md)
* [Terraform::Tfe::Variable](Variable.md)
* [Terraform::Tfe::Workspace](Workspace.md)