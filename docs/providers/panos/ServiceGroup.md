# Terraform::Panos::ServiceGroup

This resource allows you to add/update/delete service groups.

## Properties

`Name` - (Required) The service group's name.

`Vsys` - (Optional) The vsys to put the service group into (default: `vsys1`).

`Services` - (Required) List of services to put in this service group.

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_service_group](https://www.terraform.io/docs/providers/panos/r/service_group.html) in the _Terraform Provider Documentation_