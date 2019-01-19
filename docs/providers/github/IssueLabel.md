# Terraform::GitHub::IssueLabel

Provides a GitHub issue label resource.

This resource allows you to create and manage issue labels within your
GitHub organization.

Issue labels are keyed off of their "name", so pre-existing issue labels result
in a 422 HTTP error if they exist outside of Terraform. Normally this would not
be an issue, except new repositories are created with a "default" set of labels,
and those labels easily conflict with custom ones.

This resource will first check if the label exists, and then issue an update,
otherwise it will create.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [github_issue_label](https://www.terraform.io/docs/providers/github/r/issue_label.html) in the _Terraform Provider Documentation_