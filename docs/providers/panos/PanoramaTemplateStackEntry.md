# Terraform::Panos::PanoramaTemplateStackEntry

This resource allows you to add/update/delete a specific device in a Panorama
template stack.

This resource has some overlap with the `Terraform::Panos::PanoramaTemplateStack`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaTemplateStack` spec does not define the
`devices` field.

This is the appropriate resource to use if you have a pre-existing template stack
in Panorama and don't want Terraform to delete it on `terraform destroy`.

## Properties

`Template` - (Required) The template name.

`Device` - (Required) The serial number of the device to add.


## See Also

* [panos_panorama_template_stack_entry](https://www.terraform.io/docs/providers/panos/r/panorama_template_stack_entry.html) in the _Terraform Provider Documentation_