# StatusCake Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/statuscake** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* ``username`` - (Required) The username for the statuscake account.

* ``apikey`` - (Required) The API auth token to use when making requests.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::StatusCake::Test](Test.md)