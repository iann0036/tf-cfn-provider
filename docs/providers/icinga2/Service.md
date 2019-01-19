# Terraform::Icinga2::Service

Configures an Icinga2 service resource. This allows service to be configured, updated,
and deleted.

## Properties

`Name` - (Required) The name of the Service object.

`CheckCommand` - (Required) The name of an existing Icinga2 CheckCommand object that is used to determine if the service is available on the host.

`Hostname` - (Required) The host to check the service's status on.


## See Also

* [icinga2_service](https://www.terraform.io/docs/providers/icinga2/r/service.html) in the _Terraform Provider Documentation_