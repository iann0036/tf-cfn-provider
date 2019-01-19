# Terraform::VSphere::License

Provides a VMware vSphere license resource. This can be used to add and remove license keys.

## Properties

`LicenseKey` - (Required) The license key to add.

`Labels` - (Optional) A map of key/value pairs to be attached as labels (tags) to the license key.


## Return Values

### Fn::GetAtt

`EditionKey` - The product edition of the license key.

`Total` - Total number of units (example: CPUs) contained in the license.

`Used` - The number of units (example: CPUs) assigned to this license.

`Name` - The display name for the license.

## See Also

* [vsphere_license](https://www.terraform.io/docs/providers/vsphere/r/license.html) in the _Terraform Provider Documentation_