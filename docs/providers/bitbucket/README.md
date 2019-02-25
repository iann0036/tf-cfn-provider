# Bitbucket Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/bitbucket** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) Your username used to connect to bitbucket. `BITBUCKET_USERNAME`

* `password` - (Required) Your password used to connect to bitbucket. `BITBUCKET_PASSWORD`


## Supported Resources

* [Terraform::Bitbucket::DefaultReviewers](DefaultReviewers.md)
* [Terraform::Bitbucket::Hook](Hook.md)
* [Terraform::Bitbucket::Repository](Repository.md)