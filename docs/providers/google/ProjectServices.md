# Terraform::Google::ProjectServices

Allows management of enabled API services for an existing Google Cloud
Platform project. Services in an existing project that are not defined
in the config will be removed.

For a list of services available, visit the
[API library page](https://console.cloud.google.com/apis/library) or run `gcloud services list`.

~> **Note:** This resource attempts to be the authoritative source on *all* enabled APIs, which often
	leads to conflicts when certain actions enable other APIs. If you do not need to ensure that
	*exclusively* a particular set of APIs are enabled, you should most likely use the
	[google_project_service](google_project_service.html) resource, one resource per API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [google_project_services](https://www.terraform.io/docs/providers/google/r/project_services.html) in the _Terraform Provider Documentation_