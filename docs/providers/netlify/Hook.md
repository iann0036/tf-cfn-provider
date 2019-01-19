# Terraform::Netlify::Hook

An [outgoing webhook](https://www.netlify.com/docs/webhooks/#outgoing-webhooks-and-notifications), typically used to netlify a third party service about deploys.

## Properties

`SiteId` - (Required) - id of the site on netlify.

`Type` - (Required) - type of outgoing webhook, for example slack, email, github commit status, etc.

`Event` - (Required) - when to send the data, for example on deploy create, succeed, fail, etc.

`Data` - (Required) object/hash of data to be sent along with the webhook. this varies depending on the `Type`.


## See Also

* [netlify_hook](https://www.terraform.io/docs/providers/netlify/r/hook.html) in the _Terraform Provider Documentation_