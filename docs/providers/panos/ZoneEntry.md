# Terraform::Panos::ZoneEntry

This resource allows you to add/update/delete a specific interface in a zone.

This resource has some overlap with the `panos_zone`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_zone` spec does not define the
`interfaces` field.

This is the appropriate resource to use if you have a pre-existing zone
and don't want Terraform to delete it on `terraform destroy`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_zone_entry](https://www.terraform.io/docs/providers/panos/r/zone_entry.html) in the _Terraform Provider Documentation_