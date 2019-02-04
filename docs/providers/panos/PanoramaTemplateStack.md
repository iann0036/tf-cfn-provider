# Terraform::Panos::PanoramaTemplateStack

This resource allows you to add/update/delete Panorama template stacks.

This resource has some overlap with the `Terraform::Panos::PanoramaTemplateStackEntry`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaTemplateStack` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the template stack.

## Properties

`Name` - (Required) The stack's name.

`Description` - (Optional) The stack's description.

`DefaultVsys` - (Optional) The default virtual system template configuration
pushed to firewalls with a single virtual system.  **Note** - you can only
set this if there is at least one template in this stack.

`Templates` - (Optional) List of templates in this stack.

`Devices` - (Optional) List of serial numbers to include in this stack.


## See Also

* [panos_panorama_template_stack](https://www.terraform.io/docs/providers/panos/r/panorama_template_stack.html) in the _Terraform Provider Documentation_