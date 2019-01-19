# Terraform::SelVPC::ResellLicenseV2

Manages a V2 license resource within Resell Selectel VPC.

## Properties

`ProjectId` - (Required) An associated Selectel VPC project. Changing this creates a new license.

`Region` - (Required) A region of where the license resides. Changing this creates a new license.

`Type` - (Required) The type of license. Changing this creates a new license.


## Return Values

### Fn::GetAtt

`Status` - Shows if the license is used or not.

`Servers` - Shows information about servers that use this license. Contains.

## See Also

* [selvpc_resell_license_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_license_v2.html) in the _Terraform Provider Documentation_