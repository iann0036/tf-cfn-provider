# Terraform::AWS::LicensemanagerLicenseConfiguration

Provides a License Manager license configuration resource.

~> **Note:** Removing the `license_count` attribute is not supported by the License Manager API - use `terraform taint aws_licensemanager_license_configuration.<id>` to recreate the resource instead.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The license configuration ARN.

## See Also

* [aws_licensemanager_license_configuration](https://www.terraform.io/docs/providers/aws/r/licensemanager_license_configuration.html) in the _Terraform Provider Documentation_