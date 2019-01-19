# Terraform::AWS::LicensemanagerAssociation

Provides a License Manager association.

~> **Note:** License configurations can also be associated with launch templates by specifying the `license_specifications` block for an `Terraform::AWS::LaunchTemplate`.

## Properties

`LicenseConfigurationArn` - (Required) ARN of the license configuration.

`ResourceArn` - (Required) ARN of the resource associated with the license configuration.


## Return Values

### Fn::GetAtt

`Id` - The license configuration ARN.

## See Also

* [aws_licensemanager_association](https://www.terraform.io/docs/providers/aws/r/licensemanager_association.html) in the _Terraform Provider Documentation_