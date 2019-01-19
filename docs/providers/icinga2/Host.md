# Terraform::Icinga2::Host

Configures an Icinga2 host resource. This allows hosts to be configured, updated,
and deleted.

## Properties

`Address` - (Required) The address of the host.

`CheckCommand` - (Required) The name of an existing Icinga2 CheckCommand object that is used to determine if the host is available or not.

`Hostname` - (Required) The hostname of the host.

`Templates` - (Optional) A list of Icinga2 templates to assign to the host.

`Vars` - (Optional) A mapping of variables to assign to the host.


## See Also

* [icinga2_host](https://www.terraform.io/docs/providers/icinga2/r/host.html) in the _Terraform Provider Documentation_