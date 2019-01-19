# StatusCake Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/statuscake**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``username`` - (Required) The username for the statuscake account. May alternatively be set via the
  ``STATUSCAKE_USERNAME`` environment variable.

* ``apikey`` - (Required) The API auth token to use when making requests. May alternatively
  be set via the ``STATUSCAKE_APIKEY`` environment variable.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::StatusCake::Test](docs/providers/statuscake/Test.md)