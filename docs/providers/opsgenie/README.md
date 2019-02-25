# OpsGenie Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opsgenie** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) The API Key for the OpsGenie Integration.

You can generate an API Key within OpsGenie by creating a new API Integration with Read/Write permissions.


## Supported Resources

* [Terraform::OpsGenie::Team](Team.md)
* [Terraform::OpsGenie::User](User.md)