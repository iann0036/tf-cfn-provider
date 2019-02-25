# UltraDNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ultradns** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) The UltraDNS username.
* `password` - (Required) The password associated with the username.


## Supported Resources

* [Terraform::UltraDNS::Dirpool](Dirpool.md)
* [Terraform::UltraDNS::ProbeHttp](ProbeHttp.md)
* [Terraform::UltraDNS::ProbePing](ProbePing.md)
* [Terraform::UltraDNS::Rdpool](Rdpool.md)
* [Terraform::UltraDNS::Record](Record.md)
* [Terraform::UltraDNS::Tcpool](Tcpool.md)