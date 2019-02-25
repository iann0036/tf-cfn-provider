# GitHub Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/github** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Optional) This is the GitHub personal access token.

* `organization` - (Optional) This is the target GitHub organization to manage. The account
  corresponding to the token will need "owner" privileges for this organization.

* `base_url` - (Optional) This is the target GitHub base API endpoint. Providing a value is a
  requirement when working with GitHub Enterprise.  The value must end with a slash.

* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate.
  As the name suggests **this is insecure** and should not be used beyond experiments,
  accessing local (non-production) GHE instance etc.
  There is a number of ways to obtain trusted certificate for free, e.g. from [Let's Encrypt](https://letsencrypt.org/).
  Such trusted certificate *does not require* this option to be enabled.
  Defaults to `false`.


## Supported Resources

* [Terraform::GitHub::BranchProtection](BranchProtection.md)
* [Terraform::GitHub::IssueLabel](IssueLabel.md)
* [Terraform::GitHub::Membership](Membership.md)
* [Terraform::GitHub::OrganizationProject](OrganizationProject.md)
* [Terraform::GitHub::OrganizationWebhook](OrganizationWebhook.md)
* [Terraform::GitHub::ProjectColumn](ProjectColumn.md)
* [Terraform::GitHub::RepositoryCollaborator](RepositoryCollaborator.md)
* [Terraform::GitHub::RepositoryDeployKey](RepositoryDeployKey.md)
* [Terraform::GitHub::RepositoryProject](RepositoryProject.md)
* [Terraform::GitHub::RepositoryWebhook](RepositoryWebhook.md)
* [Terraform::GitHub::Repository](Repository.md)
* [Terraform::GitHub::TeamMembership](TeamMembership.md)
* [Terraform::GitHub::TeamRepository](TeamRepository.md)
* [Terraform::GitHub::Team](Team.md)
* [Terraform::GitHub::UserGpgKey](UserGpgKey.md)
* [Terraform::GitHub::UserInvitationAccepter](UserInvitationAccepter.md)
* [Terraform::GitHub::UserSshKey](UserSshKey.md)