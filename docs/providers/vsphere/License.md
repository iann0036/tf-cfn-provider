# Terraform::VSphere::License

Provides a VMware vSphere license resource. This can be used to add and remove license keys.

## Properties

TBC

## Return Values

### Fn::GetAtt

`EditionKey` - The product edition of the license key.

`Total` - Total number of units (example: CPUs) contained in the license.

`Used` - The number of units (example: CPUs) assigned to this license.

`Name` - The display name for the license.

## See Also

* [vsphere_license](https://www.terraform.io/docs/providers/vsphere/r/license.html) in the _Terraform Provider Documentation_