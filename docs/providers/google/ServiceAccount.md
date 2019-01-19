# Terraform::Google::ServiceAccount

Allows management of a [Google Cloud Platform service account](https://cloud.google.com/compute/docs/access/service-accounts)

## Properties

`AccountId` - (Required) The account id that is used to generate the service account email address and a stable unique id. It is unique within a project, must be 6-30 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])` to comply with RFC1035. Changing this forces a new service account to be created.

`DisplayName` - (Optional) The display name for the service account. Can be updated without creating a new resource.

`Project` - (Optional) The ID of the project that the service account will be created in. Defaults to the provider project configuration.


## Return Values

### Fn::GetAtt

`Email` - The e-mail address of the service account. This value.

`Name` - The fully-qualified name of the service account.

`UniqueId` - The unique id of the service account.

## See Also

* [google_service_account](https://www.terraform.io/docs/providers/google/r/service_account.html) in the _Terraform Provider Documentation_