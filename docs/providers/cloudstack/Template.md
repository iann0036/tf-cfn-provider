# Terraform::CloudStack::Template

Registers an existing template into the CloudStack cloud.

## Properties

`Name` - (Required) The name of the template.

`DisplayText` - (Optional) The display name of the template.

`Format` - (Required) The format of the template. Valid values are `QCOW2`,
`RAW`, and `VHD`.

`Hypervisor` - (Required) The target hypervisor for the template. Changing
this forces a new resource to be created.

`OsType` - (Required) The OS Type that best represents the OS of this
template.

`Url` - (Required) The URL of where the template is hosted. Changing this
forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to create this template for.
Changing this forces a new resource to be created.

`Zone` - (Optional) The name or ID of the zone where this template will be created.
Changing this forces a new resource to be created.

`IsDynamicallyScalable` - (Optional) Set to indicate if the template contains
tools to support dynamic scaling of VM cpu/memory (defaults false).

`IsExtractable` - (Optional) Set to indicate if the template is extractable
(defaults false).

`IsFeatured` - (Optional) Set to indicate if the template is featured
(defaults false).

`IsPublic` - (Optional) Set to indicate if the template is available for
all accounts (defaults true).

`PasswordEnabled` - (Optional) Set to indicate if the template should be
password enabled (defaults false).

`IsReadyTimeout` - (Optional) The maximum time in seconds to wait until the
template is ready for use (defaults 300 seconds).


## Return Values

### Fn::GetAtt

`Id` - The template ID.

`DisplayText` - The display text of the template.

`IsDynamicallyScalable` - Set to "true" if the template is dynamically scalable.

`IsExtractable` - Set to "true" if the template is extractable.

`IsFeatured` - Set to "true" if the template is featured.

`IsPublic` - Set to "true" if the template is public.

`PasswordEnabled` - Set to "true" if the template is password enabled.

`IsReady` - Set to "true" once the template is ready for use.

## See Also

* [cloudstack_template](https://www.terraform.io/docs/providers/cloudstack/r/template.html) in the _Terraform Provider Documentation_