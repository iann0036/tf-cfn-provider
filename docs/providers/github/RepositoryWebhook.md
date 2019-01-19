# Terraform::GitHub::RepositoryWebhook

This resource allows you to create and manage webhooks for repositories within your
GitHub organization.

This resource cannot currently be used to manage webhooks for *personal* repositories,
outside of organizations.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Url` - URL of the webhook.

## See Also

* [github_repository_webhook](https://www.terraform.io/docs/providers/github/r/repository_webhook.html) in the _Terraform Provider Documentation_