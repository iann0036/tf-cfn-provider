# Terraform::Panos::PanoramaTemplate

This resource allows you to add/update/delete Panorama templates.

This resource has some overlap with the `Terraform::Panos::PanoramaTemplateEntry`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaTemplate` spec does not define any
`Device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the template.

**Note** - In PAN-OS 8.1, it looks like the `devices` field has
been removed.  Creating a template stack and specifying devices in the template
stack is still present in PAN-OS 8.1.

## Properties

`Name` - (Required) The template's name.

`Description` - (Optional) The template's description.

`Device` - The device definition (see below).

`Serial` - (Required) The serial number of the firewall.

`VsysList` - (Optional) A subset of all available vsys on the firewall that should be in this template.  If the firewall is a virtual firewall, then this parameter should just be omitted.


## See Also

* [panos_panorama_template](https://www.terraform.io/docs/providers/panos/r/panorama_template.html) in the _Terraform Provider Documentation_