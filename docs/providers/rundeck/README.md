# Rundeck Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rundeck**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``url`` - (Required) The root URL of a Rundeck server. May alternatively be set via the
  ``RUNDECK_URL`` environment variable.

* ``auth_token`` - (Required) The API auth token to use when making requests. May alternatively
  be set via the ``RUNDECK_AUTH_TOKEN`` environment variable.

* ``allow_unverified_ssl`` - (Optional) Boolean that can be set to ``true`` to disable SSL
  certificate verification. This should be used with care as it could allow an attacker to
  intercept your auth token.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::Rundeck::Job](docs/providers/rundeck/Job.md)
* [Terraform::Rundeck::PrivateKey](docs/providers/rundeck/PrivateKey.md)
* [Terraform::Rundeck::Project](docs/providers/rundeck/Project.md)
* [Terraform::Rundeck::PublicKey](docs/providers/rundeck/PublicKey.md)