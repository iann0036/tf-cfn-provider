# Terraform::AWS::LicensemanagerLicenseConfiguration

Provides a License Manager license configuration resource.

~> **Note:** Removing the `LicenseCount` attribute is not supported by the License Manager API - use `terraform taint aws_licensemanager_license_configuration.<id>` to recreate the resource instead.

## Properties

`Name` - (Required) Name of the license configuration.

`Description` - (Optional) Description of the license configuration.

`LicenseCount` - (Optional) Number of licenses managed by the license configuration.

`LicenseCountHardLimit` - (Optional) Sets the number of available licenses as a hard limit.

`LicenseCountingType` - (Required) Dimension to use to track license inventory. Specify either `vCPU`, `Instance`, `Core` or `Socket`.

`LicenseRules` - (Optional) Array of configured License Manager rules.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The license configuration ARN.

## See Also

* [aws_licensemanager_license_configuration](https://www.terraform.io/docs/providers/aws/r/licensemanager_license_configuration.html) in the _Terraform Provider Documentation_