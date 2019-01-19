# Gitlab Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/gitlab**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) This is the GitLab personal access token.

* `base_url` - (Optional) This is the target GitLab base API endpoint. Providing a value is a
  requirement when working with GitLab CE or GitLab Enterprise e.g. https://my.gitlab.server/api/v3/.
  The value must end with a slash.

* `cacert_file` - (Optional) This is a file containing the ca cert to verify the gitlab instance.  This is available
  for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain.

* `insecure` - (Optional; boolean, defaults to false) When set to true this disables SSL verification of the connection to the
  GitLab instance.


## Supported Resources

* [Terraform::Gitlab::DeployKey](DeployKey.md)
* [Terraform::Gitlab::GroupMembership](GroupMembership.md)
* [Terraform::Gitlab::GroupVariable](GroupVariable.md)
* [Terraform::Gitlab::Group](Group.md)
* [Terraform::Gitlab::Label](Label.md)
* [Terraform::Gitlab::ProjectHook](ProjectHook.md)
* [Terraform::Gitlab::ProjectMembership](ProjectMembership.md)
* [Terraform::Gitlab::ProjectVariable](ProjectVariable.md)
* [Terraform::Gitlab::Project](Project.md)
* [Terraform::Gitlab::User](User.md)