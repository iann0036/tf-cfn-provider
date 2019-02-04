# Terraform::GitHub::Membership

Provides a GitHub membership resource.

This resource allows you to add/remove users from your organization. When applied,
an invitation will be sent to the user to become part of the organization. When
destroyed, either the invitation will be cancelled or the user will be removed.

## Properties

`Username` - (Required) The user to add to the organization.

`Role` - (Optional) The role of the user within the organization.
Must be one of `member` or `admin`. Defaults to `member`.


## See Also

* [github_membership](https://www.terraform.io/docs/providers/github/r/membership.html) in the _Terraform Provider Documentation_