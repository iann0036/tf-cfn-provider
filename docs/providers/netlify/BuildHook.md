# Terraform::Netlify::BuildHook

Manages build hooks, also known as [incoming webhooks]
(https://www.netlify.com/docs/webhooks/#outgoing-webhooks). These can,
at the time of writing, only be used to trigger new builds of the site.
To create one, provide your site id along with the name of the hook, and
the branch to be built when the hook is triggered.

## Properties

`SiteId` - (Required) Your netlify site's unique id.

`Branch` - (Required) branch to be built when the hook is triggered.

`Title` - (Required) name of the webhook - this is purely for organization and can be any name you want.


## See Also

* [netlify_build_hook](https://www.terraform.io/docs/providers/netlify/r/build_hook.html) in the _Terraform Provider Documentation_