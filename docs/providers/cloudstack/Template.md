# Terraform::CloudStack::Template

Registers an existing template into the CloudStack cloud.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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