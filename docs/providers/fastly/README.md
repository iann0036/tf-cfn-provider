# Fastly Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/fastly**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Optional) This is the API key. It must be provided, but
  it can also be sourced from the `FASTLY_API_KEY` environment variable

* `base_url` - (Optional) This is the API server hostname. It is required
  if using a private instance of the API and otherwise defaults to the
  public Fastly production service. It can also be sourced from the
  `FASTLY_API_URL` environment variable


## Supported Resources

* [Terraform::Fastly::ServiceV1](docs/providers/fastly/ServiceV1.md)