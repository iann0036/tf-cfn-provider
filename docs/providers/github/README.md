# GitHub Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/github**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) This is the GitHub personal access token. It must be provided, but
  it can also be sourced from the `GITHUB_TOKEN` environment variable.

* `organization` - (Optional) This is the target GitHub organization to manage. The account
  corresponding to the token will need "owner" privileges for this organization. It must be provided, but
  it can also be sourced from the `GITHUB_ORGANIZATION` environment variable.

* `base_url` - (Optional) This is the target GitHub base API endpoint. Providing a value is a
  requirement when working with GitHub Enterprise.  It is optional to provide this value and
  it can also be sourced from the `GITHUB_BASE_URL` environment variable.  The value must end with a slash.

* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate.
  As the name suggests **this is insecure** and should not be used beyond experiments,
  accessing local (non-production) GHE instance etc.
  There is a number of ways to obtain trusted certificate for free, e.g. from [Let's Encrypt](https://letsencrypt.org/).
  Such trusted certificate *does not require* this option to be enabled.
  Defaults to `false`.


## Supported Resources

* [Terraform::GitHub::BranchProtection](docs/providers/github/BranchProtection.md)
* [Terraform::GitHub::IssueLabel](docs/providers/github/IssueLabel.md)
* [Terraform::GitHub::Membership](docs/providers/github/Membership.md)
* [Terraform::GitHub::OrganizationProject](docs/providers/github/OrganizationProject.md)
* [Terraform::GitHub::OrganizationWebhook](docs/providers/github/OrganizationWebhook.md)
* [Terraform::GitHub::ProjectColumn](docs/providers/github/ProjectColumn.md)
* [Terraform::GitHub::RepositoryCollaborator](docs/providers/github/RepositoryCollaborator.md)
* [Terraform::GitHub::RepositoryDeployKey](docs/providers/github/RepositoryDeployKey.md)
* [Terraform::GitHub::RepositoryProject](docs/providers/github/RepositoryProject.md)
* [Terraform::GitHub::RepositoryWebhook](docs/providers/github/RepositoryWebhook.md)
* [Terraform::GitHub::Repository](docs/providers/github/Repository.md)
* [Terraform::GitHub::TeamMembership](docs/providers/github/TeamMembership.md)
* [Terraform::GitHub::TeamRepository](docs/providers/github/TeamRepository.md)
* [Terraform::GitHub::Team](docs/providers/github/Team.md)
* [Terraform::GitHub::UserGpgKey](docs/providers/github/UserGpgKey.md)
* [Terraform::GitHub::UserInvitationAccepter](docs/providers/github/UserInvitationAccepter.md)
* [Terraform::GitHub::UserSshKey](docs/providers/github/UserSshKey.md)