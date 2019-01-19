# Terraform::GitHub::OrganizationWebhook

This resource allows you to create and manage webhooks for GitHub organization.

## Properties

`Name` - (Required) The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).

`Events` - (Required) A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/).

`Configuration` - (Required) key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.

`Active` - (Optional) Indicate of the webhook should receive events. Defaults to `true`.


## Return Values

### Fn::GetAtt

`Url` - URL of the webhook.

## See Also

* [github_organization_webhook](https://www.terraform.io/docs/providers/github/r/organization_webhook.html) in the _Terraform Provider Documentation_