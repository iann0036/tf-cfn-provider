# Terraform::Panos::PanoramaTemplate

This resource allows you to add/update/delete Panorama templates.

This resource has some overlap with the `panos_panorama_template_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_template` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the template.

**Note** - In PAN-OS 8.1, it looks like the `devices` field has
been removed.  Creating a template stack and specifying devices in the template
stack is still present in PAN-OS 8.1.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_panorama_template](https://www.terraform.io/docs/providers/panos/r/panorama_template.html) in the _Terraform Provider Documentation_