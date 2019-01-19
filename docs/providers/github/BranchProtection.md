# Terraform::GitHub::BranchProtection

Protects a GitHub branch.

This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users and teams, can also be configured.

## Properties

`Repository` - (Required) The GitHub repository name.

`Branch` - (Required) The Git branch to protect.

`EnforceAdmins` - (Optional) Boolean, setting this to `true` enforces status checks for repository administrators.

`RequiredStatusChecks` - (Optional) Enforce restrictions for required status checks. See [Required Status Checks](#required-status-checks) below for details.

`RequiredPullRequestReviews` - (Optional) Enforce restrictions for pull request reviews. See [Required Pull Request Reviews](#required-pull-request-reviews) below for details.

`Restrictions` - (Optional) Enforce restrictions for the users and teams that may push to the branch. See [Restrictions](#restrictions) below for details.


## See Also

* [github_branch_protection](https://www.terraform.io/docs/providers/github/r/branch_protection.html) in the _Terraform Provider Documentation_