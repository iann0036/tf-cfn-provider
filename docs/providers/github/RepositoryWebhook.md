# Terraform::GitHub::RepositoryWebhook

This resource allows you to create and manage webhooks for repositories within your
GitHub organization.

This resource cannot currently be used to manage webhooks for *personal* repositories,
outside of organizations.

## Properties

`Name` - (Required) The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).

`Repository` - (Required) The repository of the webhook.

`Events` - (Required) A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/).

`Configuration` - (Required) key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.

`Active` - (Optional) Indicate of the webhook should receive events. Defaults to `true`.


## Return Values

### Fn::GetAtt

`Url` - URL of the webhook.

## See Also

* [github_repository_webhook](https://www.terraform.io/docs/providers/github/r/repository_webhook.html) in the _Terraform Provider Documentation_