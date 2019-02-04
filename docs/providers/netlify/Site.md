# Terraform::Netlify::Site

Primary settings for a Netlify site - should contain the bulk of your configuration. Allows configuration of most aspects of your Netlify site.

## Properties

`Name` - (Required) - Name of your site on Netlify (e.g. **mysite**.netlify.com).

`Repo` - (Required) - See [Repository](#repo).

`CustomDomain` - (Optional) - Custom domain of the site, must be configured using a CNAME in accordance with [Netlify's docs](https://www.netlify.com/docs/custom-domains). (e.g. `www.example.com`).

`DeployUrl` - (Optional).


## See Also

* [netlify_site](https://www.terraform.io/docs/providers/netlify/r/site.html) in the _Terraform Provider Documentation_