# Terraform::HuaweiCloud::IamAgencyV3

Manages an agency resource within huawei cloud.

## Properties

`Name` - (Required) The name of agency. The name is a string of 1 to 64 characters.

`Description` - (Optional) Provides supplementary information about the agency. The value is a string of 0 to 255 characters.

`DelegatedDomainName` - (Required) The name of delegated domain.

`ProjectRole` - (Optional) An array of roles and projects which are used to grant permissions to agency on project. The structure is documented below.

`DomainRoles` - (optional) An array of role names which stand for the permissionis to be granted to agency on domain.

`Project` - (Required) The name of project.

`Roles` - (Required) An array of role names.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`Description` - See Properties above.

`DelegatedDomainName` - See Properties above.

`ProjectRole` - See Properties above.

`DomainRoles` - See Properties above.

`Duration` - Validity period of an agency. The default value is null,.

`ExpireTime` - The expiration time of agency.

`CreateTime` - The time when the agency was created.

`Id` - The agency ID.

## See Also

* [huaweicloud_iam_agency_v3](https://www.terraform.io/docs/providers/huaweicloud/r/iam_agency_v3.html) in the _Terraform Provider Documentation_