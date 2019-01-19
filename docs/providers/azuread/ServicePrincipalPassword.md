# Terraform::AzureAD::ServicePrincipalPassword

Manages a Password associated with a Service Principal within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Properties

`ServicePrincipalId` - (Required) The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

`Value` - (Required) The Password for this Service Principal.

`EndDate` - (Required) The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

`KeyId` - (Optional) A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

`StartDate` - (Optional) The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The Key ID for the Service Principal Password.

## See Also

* [azuread_service_principal_password](https://www.terraform.io/docs/providers/azuread/r/service_principal_password.html) in the _Terraform Provider Documentation_