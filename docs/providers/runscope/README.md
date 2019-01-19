# RunScope Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/runscope**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_token` - (Required) The Runscope access token.
  This can also be specified with the `RUNSCOPE_ACCESS_TOKEN` shell
  environment variable.
* `api_url` - (Optional) If set, specifies the Runscope api url, this
   defaults to `"https://api.runscope.com`. This can also be specified
   with the `RUNSCOPE_API_URL` shell environment variable.


## Supported Resources

* [Terraform::RunScope::Bucket](docs/providers/runscope/Bucket.md)
* [Terraform::RunScope::Environment](docs/providers/runscope/Environment.md)
* [Terraform::RunScope::Schedule](docs/providers/runscope/Schedule.md)
* [Terraform::RunScope::Step](docs/providers/runscope/Step.md)
* [Terraform::RunScope::Test](docs/providers/runscope/Test.md)