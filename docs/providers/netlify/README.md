# Netlify Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/netlify**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) Environment Variable: `NETLIFY_TOKEN`
* `base_url` - (Optional) Environment Variable: `NETLIFY_BASE_URL`


## Supported Resources

* [Terraform::Netlify::BuildHook](docs/providers/netlify/BuildHook.md)
* [Terraform::Netlify::DeployKey](docs/providers/netlify/DeployKey.md)
* [Terraform::Netlify::Hook](docs/providers/netlify/Hook.md)
* [Terraform::Netlify::Site](docs/providers/netlify/Site.md)