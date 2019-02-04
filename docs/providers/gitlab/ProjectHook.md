# Terraform::Gitlab::ProjectHook

This resource allows you to create and manage hooks for your GitLab projects.
For further information on hooks, consult the [gitlab
documentation](https://docs.gitlab.com/ce/user/project/integrations/webhooks.html).

## Properties

`Project` - (Required) The name or id of the project to add the hook to.

`Url` - (Required) The url of the hook to invoke.

`Token` - (Optional) A token to present when invoking the hook.

`EnableSslVerification` - (Optional) Enable ssl verification when invoking
the hook.

`PushEvents` - (Optional) Invoke the hook for push events.

`IssuesEvents` - (Optional) Invoke the hook for issues events.

`MergeRequestsEvents` - (Optional) Invoke the hook for merge requests.

`TagPushEvents` - (Optional) Invoke the hook for tag push events.

`NoteEvents` - (Optional) Invoke the hook for notes events.

`JobEvents` - (Optional) Invoke the hook for job events.

`PipelineEvents` - (Optional) Invoke the hook for pipeline events.

`WikiPageEvents` - (Optional) Invoke the hook for wiki page events.


## Return Values

### Fn::GetAtt

`Id` - The unique id assigned to the hook by the GitLab server.

## See Also

* [gitlab_project_hook](https://www.terraform.io/docs/providers/gitlab/r/project_hook.html) in the _Terraform Provider Documentation_