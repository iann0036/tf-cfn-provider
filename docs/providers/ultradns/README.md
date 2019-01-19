# UltraDNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ultradns**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) The UltraDNS username.
* `password` - (Required) The password associated with the username.


## Supported Resources

* [Terraform::UltraDNS::Dirpool](Dirpool.md)
* [Terraform::UltraDNS::ProbeHttp](ProbeHttp.md)
* [Terraform::UltraDNS::ProbePing](ProbePing.md)
* [Terraform::UltraDNS::Rdpool](Rdpool.md)
* [Terraform::UltraDNS::Record](Record.md)
* [Terraform::UltraDNS::Tcpool](Tcpool.md)