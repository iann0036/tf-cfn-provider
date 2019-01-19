# Mailgun Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/mailgun**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Mailgun API key



## Supported Resources

* [Terraform::Mailgun::Domain](Domain.md)