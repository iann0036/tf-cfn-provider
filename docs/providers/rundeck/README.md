# Rundeck Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rundeck**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``url`` - (Required) The root URL of a Rundeck server.

* ``auth_token`` - (Required) The API auth token to use when making requests.

* ``allow_unverified_ssl`` - (Optional) Boolean that can be set to ``true`` to disable SSL
  certificate verification. This should be used with care as it could allow an attacker to
  intercept your auth token.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::Rundeck::Job](Job.md)
* [Terraform::Rundeck::PrivateKey](PrivateKey.md)
* [Terraform::Rundeck::Project](Project.md)
* [Terraform::Rundeck::PublicKey](PublicKey.md)