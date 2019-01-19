# Terraform Enterprise Provider

##Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/tfe**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Optional) The Terraform Enterprise hostname to connect to.
  Defaults to `app.terraform.io`.
* `token` - (Optional) The token used to authenticate with Terraform Enterprise.
  Only set this argument when running in a Terraform Enterprise workspace; for
  CLI usage, omit the token from the configuration and set it as `credentials`
  in the [CLI config file](/docs/commands/cli-config.html#credentials). See
  [Authentication](#authentication) above for more.


## Supported Resources

* [Terraform::Tfe::OauthClient](docs/providers/tfe/OauthClient.md)
* [Terraform::Tfe::OrganizationToken](docs/providers/tfe/OrganizationToken.md)
* [Terraform::Tfe::Organization](docs/providers/tfe/Organization.md)
* [Terraform::Tfe::PolicySet](docs/providers/tfe/PolicySet.md)
* [Terraform::Tfe::SentinelPolicy](docs/providers/tfe/SentinelPolicy.md)
* [Terraform::Tfe::SshKey](docs/providers/tfe/SshKey.md)
* [Terraform::Tfe::TeamAccess](docs/providers/tfe/TeamAccess.md)
* [Terraform::Tfe::TeamMember](docs/providers/tfe/TeamMember.md)
* [Terraform::Tfe::TeamMembers](docs/providers/tfe/TeamMembers.md)
* [Terraform::Tfe::TeamToken](docs/providers/tfe/TeamToken.md)
* [Terraform::Tfe::Team](docs/providers/tfe/Team.md)
* [Terraform::Tfe::Variable](docs/providers/tfe/Variable.md)
* [Terraform::Tfe::Workspace](docs/providers/tfe/Workspace.md)