# Terraform::Netlify::Site

Primary settings for the Netlify site - should contain the bulk of your configuration. Allows configuration of most aspects of your Netlify site.

## Properties

`Name` - (Required) - name of your site on netlify.

`Repo` - (Required) See [Repository](#repo).

`CustomDomain` - (Optional) - a custom domain name, must be configured using a cname in accordance with [netlify's docs](https://www.netlify.com/docs/custom-domains).

`DeployUrl` - (Optional).


## See Also

* [netlify_site](https://www.terraform.io/docs/providers/netlify/r/site.html) in the _Terraform Provider Documentation_