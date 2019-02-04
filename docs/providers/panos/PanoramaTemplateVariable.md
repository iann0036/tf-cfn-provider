# Terraform::Panos::PanoramaTemplateVariable

This resource allows you to add/update/delete variables for both Panorama
templates and template stacks.

Template variables are available in PAN-OS 8.1+.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`Name` - (Required) The template's name.  This must start with a dollar sign ($).

`Type` - (Optional) The variable type.  Valid values are `ip-netmask`
(default), `ip-range`, `fqdn`, `group-id`, or `interface`.

`Value` - (Required) The variable value.


## See Also

* [panos_panorama_template_variable](https://www.terraform.io/docs/providers/panos/r/panorama_template_variable.html) in the _Terraform Provider Documentation_