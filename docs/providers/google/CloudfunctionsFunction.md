# Terraform::Google::CloudfunctionsFunction

Creates a new Cloud Function. For more information see
[the official documentation](https://cloud.google.com/functions/docs/)
and
[API](https://cloud.google.com/functions/docs/apis).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`HttpsTriggerUrl` - URL which triggers function execution. Returned only if `trigger_http` is used.

`SourceReposoitory.0.deployedUrl` - The URL pointing to the hosted repository where the function was defined at the time of deployment.

`Project` - Project of the function. If it is not provided, the provider project is used.

`Region` - Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

## See Also

* [google_cloudfunctions_function](https://www.terraform.io/docs/providers/google/r/cloudfunctions_function.html) in the _Terraform Provider Documentation_