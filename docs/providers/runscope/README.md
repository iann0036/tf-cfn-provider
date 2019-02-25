# RunScope Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/runscope** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_token` - (Required) The Runscope access token.
* `api_url` - (Optional) If set, specifies the Runscope api url, this
   defaults to `"https://api.runscope.com`.


## Supported Resources

* [Terraform::RunScope::Bucket](Bucket.md)
* [Terraform::RunScope::Environment](Environment.md)
* [Terraform::RunScope::Schedule](Schedule.md)
* [Terraform::RunScope::Step](Step.md)
* [Terraform::RunScope::Test](Test.md)