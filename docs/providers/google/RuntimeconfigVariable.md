# Terraform::Google::RuntimeconfigVariable

Manages a RuntimeConfig variable in Google Cloud. For more information, see the
[official documentation](https://cloud.google.com/deployment-manager/runtime-configurator/),
or the
[JSON API](https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/).

## Properties

`Name` - (Required) The name of the variable to manage. Note that variable names can be hierarchical using slashes (e.g. "prod-variables/hostname").

`Parent` - (Required) The name of the RuntimeConfig resource containing this variable.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.


## Return Values

### Fn::GetAtt

`UpdateTime` - (Computed) The timestamp in RFC3339 UTC "Zulu" format,.

## See Also

* [google_runtimeconfig_variable](https://www.terraform.io/docs/providers/google/r/runtimeconfig_variable.html) in the _Terraform Provider Documentation_