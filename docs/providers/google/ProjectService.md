# Terraform::Google::ProjectService

Allows management of a single API service for an existing Google Cloud Platform project. 

For a list of services available, visit the
[API library page](https://console.cloud.google.com/apis/library) or run `gcloud services list`.

~> **Note:** This resource _must not_ be used in conjunction with
   `Terraform::Google::ProjectServices` or they will fight over which services should be enabled.

## Properties

`Service` - (Required) The service to enable.

`Project` - (Optional) The project ID. If not provided, the provider project is used.

`DisableOnDestroy` - (Optional) If true, disable the service when the terraform resource is destroyed.  Defaults to true.  May be useful in the event that a project is long-lived but the infrastructure running in that project changes frequently.


## See Also

* [google_project_service](https://www.terraform.io/docs/providers/google/r/project_service.html) in the _Terraform Provider Documentation_