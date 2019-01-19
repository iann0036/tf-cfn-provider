# Terraform::VSphere::License

Provides a VMware vSphere license resource. This can be used to add and remove license keys.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`EditionKey` - The product edition of the license key.

`Total` - Total number of units (example: CPUs) contained in the license.

`Used` - The number of units (example: CPUs) assigned to this license.

`Name` - The display name for the license.

## See Also

* [vsphere_license](https://www.terraform.io/docs/providers/vsphere/r/license.html) in the _Terraform Provider Documentation_