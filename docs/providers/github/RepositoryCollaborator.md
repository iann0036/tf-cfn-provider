# Terraform::GitHub::RepositoryCollaborator

Provides a GitHub repository collaborator resource.

This resource allows you to add/remove collaborators from repositories in your
organization. Collaborators can have explicit (and differing levels of) read,
write, or administrator access to specific repositories in your organization,
without giving the user full organization membership.

When applied, an invitation will be sent to the user to become a collaborator
on a repository. When destroyed, either the invitation will be cancelled or the
collaborator will be removed from the repository.

Further documentation on GitHub collaborators:

- [Adding outside collaborators to repositories in your organization](https://help.github.com/articles/adding-outside-collaborators-to-repositories-in-your-organization/)
- [Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)

## Properties

`Repository` - (Required) The GitHub repository.

`Username` - (Required) The user to add to the repository as a collaborator.

`Permission` - (Optional) The permission of the outside collaborator for the repository.
Must be one of `pull`, `push`, or `admin`. Defaults to `push`.


## See Also

* [github_repository_collaborator](https://www.terraform.io/docs/providers/github/r/repository_collaborator.html) in the _Terraform Provider Documentation_