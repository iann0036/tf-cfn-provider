# Terraform::Icinga2::Checkcommand

Configures an Icinga2 checkcommand resource. This allows checkcommands to be configured, updated,
and deleted.

## Properties

`Arguments` - (Optional) A mapping of arguments to include with the command.

`Command` - (Required) Path to the command te be executed.

`Name` - (Required) Name by which to reference the checkcommand.

`Templates` - (Optional) A list of Icinga2 templates to assign to the host.


## See Also

* [icinga2_checkcommand](https://www.terraform.io/docs/providers/icinga2/r/checkcommand.html) in the _Terraform Provider Documentation_