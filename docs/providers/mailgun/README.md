# Mailgun Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/mailgun** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) Mailgun API key



## Supported Resources

* [Terraform::Mailgun::Domain](Domain.md)