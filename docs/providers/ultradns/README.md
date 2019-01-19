# UltraDNS Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ultradns**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) The UltraDNS username. It must be provided, but it can also be sourced from the `ULTRADNS_USERNAME` environment variable.
* `password` - (Required) The password associated with the username. It must be provided, but it can also be sourced from the `ULTRADNS_PASSWORD` environment variable.
* `baseurl` - (Required) The base url for the UltraDNS REST API, but it can also be sourced from the `ULTRADNS_BASEURL` environment variable.


## Supported Resources

* [Terraform::UltraDNS::Dirpool](docs/providers/ultradns/Dirpool.md)
* [Terraform::UltraDNS::ProbeHttp](docs/providers/ultradns/ProbeHttp.md)
* [Terraform::UltraDNS::ProbePing](docs/providers/ultradns/ProbePing.md)
* [Terraform::UltraDNS::Rdpool](docs/providers/ultradns/Rdpool.md)
* [Terraform::UltraDNS::Record](docs/providers/ultradns/Record.md)
* [Terraform::UltraDNS::Tcpool](docs/providers/ultradns/Tcpool.md)