# Bitbucket Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/bitbucket**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) Your username used to connect to bitbucket. You can
  also set this via the environment variable. `BITBUCKET_USERNAME`

* `password` - (Required) Your password used to connect to bitbucket. You can
  also set this via the environment variable. `BITBUCKET_PASSWORD`


## Supported Resources

* [Terraform::Bitbucket::DefaultReviewers](docs/providers/bitbucket/DefaultReviewers.md)
* [Terraform::Bitbucket::Hook](docs/providers/bitbucket/Hook.md)
* [Terraform::Bitbucket::Repository](docs/providers/bitbucket/Repository.md)