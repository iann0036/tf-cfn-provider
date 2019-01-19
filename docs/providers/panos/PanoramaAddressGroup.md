# Terraform::Panos::PanoramaAddressGroup

This resource allows you to add/update/delete Panorama address groups.

Address groups are either statically defined or dynamically defined, so only
`static_addresses` or `dynamic_match` should be defined within a given address
group.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_panorama_address_group](https://www.terraform.io/docs/providers/panos/r/panorama_address_group.html) in the _Terraform Provider Documentation_