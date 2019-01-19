# Terraform::Netlify::BuildHook

Manages build hooks, also known as [incoming webhooks]
(https://www.netlify.com/docs/webhooks/#outgoing-webhooks). These can,
at the time of writing, only be used to trigger new builds of the site.
To create one, provide your site id along with the name of the hook, and
the branch to be built when the hook is triggered.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [netlify_build_hook](https://www.terraform.io/docs/providers/netlify/r/build_hook.html) in the _Terraform Provider Documentation_