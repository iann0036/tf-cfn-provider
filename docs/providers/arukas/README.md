# Arukas Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/arukas**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) This is the Arukas API token. It must be provided, but
  it can also be sourced from the `ARUKAS_JSON_API_TOKEN` environment variable.

* `secret` - (Required) This is the Arukas API secret. It must be provided, but
  it can also be sourced from the `ARUKAS_JSON_API_SECRET` environment variable.

* `api_url` - (Optional) Override Arukas API Root URL. Also taken from the `ARUKAS_JSON_API_URL`
  environment variable if provided.

* `trace` - (Optional) The flag of Arukas API trace log. Also taken from the `ARUKAS_DEBUG`
  environment variable if provided.

* `timeout` - (Optional) Override Arukas API timeout seconds. Also taken from the `ARUKAS_TIMEOUT`
  environment variable if provided.


## Supported Resources

* [Terraform::Arukas::Container](docs/providers/arukas/Container.md)