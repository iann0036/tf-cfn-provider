# Bitbucket Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/bitbucket**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) Your username used to connect to bitbucket. `BITBUCKET_USERNAME`

* `password` - (Required) Your password used to connect to bitbucket. `BITBUCKET_PASSWORD`


## Supported Resources

* [Terraform::Bitbucket::DefaultReviewers](DefaultReviewers.md)
* [Terraform::Bitbucket::Hook](Hook.md)
* [Terraform::Bitbucket::Repository](Repository.md)