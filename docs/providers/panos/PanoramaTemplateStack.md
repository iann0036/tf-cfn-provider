# Terraform::Panos::PanoramaTemplateStack

This resource allows you to add/update/delete Panorama template stacks.

This resource has some overlap with the `panos_panorama_template_stack_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_template_stack` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the template stack.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_panorama_template_stack](https://www.terraform.io/docs/providers/panos/r/panorama_template_stack.html) in the _Terraform Provider Documentation_