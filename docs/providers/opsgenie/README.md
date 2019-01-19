# OpsGenie Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opsgenie**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) The API Key for the OpsGenie Integration. If omitted, the
  `OPSGENIE_API_KEY` environment variable is used.

You can generate an API Key within OpsGenie by creating a new API Integration with Read/Write permissions.


## Supported Resources

* [Terraform::OpsGenie::Team](docs/providers/opsgenie/Team.md)
* [Terraform::OpsGenie::User](docs/providers/opsgenie/User.md)