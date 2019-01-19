# Gitlab Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/gitlab**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) This is the GitLab personal access token. It must be provided, but
  it can also be sourced from the `GITLAB_TOKEN` environment variable.

* `base_url` - (Optional) This is the target GitLab base API endpoint. Providing a value is a
  requirement when working with GitLab CE or GitLab Enterprise e.g. https://my.gitlab.server/api/v3/.
  It is optional to provide this value and it can also be sourced from the `GITLAB_BASE_URL` environment variable.
  The value must end with a slash.

* `cacert_file` - (Optional) This is a file containing the ca cert to verify the gitlab instance.  This is available
  for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain.

* `insecure` - (Optional; boolean, defaults to false) When set to true this disables SSL verification of the connection to the
  GitLab instance.


## Supported Resources

* [Terraform::Gitlab::DeployKey](docs/providers/gitlab/DeployKey.md)
* [Terraform::Gitlab::GroupMembership](docs/providers/gitlab/GroupMembership.md)
* [Terraform::Gitlab::GroupVariable](docs/providers/gitlab/GroupVariable.md)
* [Terraform::Gitlab::Group](docs/providers/gitlab/Group.md)
* [Terraform::Gitlab::Label](docs/providers/gitlab/Label.md)
* [Terraform::Gitlab::ProjectHook](docs/providers/gitlab/ProjectHook.md)
* [Terraform::Gitlab::ProjectMembership](docs/providers/gitlab/ProjectMembership.md)
* [Terraform::Gitlab::ProjectVariable](docs/providers/gitlab/ProjectVariable.md)
* [Terraform::Gitlab::Project](docs/providers/gitlab/Project.md)
* [Terraform::Gitlab::User](docs/providers/gitlab/User.md)