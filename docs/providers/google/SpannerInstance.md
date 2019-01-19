# Terraform::Google::SpannerInstance

Creates and manages a Google Spanner Instance. For more information, see the [official documentation](https://cloud.google.com/spanner/), or the [JSON API](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances).

## Properties

`Config` - (Required) The name of the instance's configuration (similar but not quite the same as a region) which defines defines the geographic placement and replication of your databases in this instance. It determines where your data is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc. In order to obtain a valid list please consult the [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

`DisplayName` - (Required) The descriptive name for this instance as it appears in UIs. Can be updated, however should be kept globally unique to avoid confusion.

`Name` - (Optional, Computed) The unique name (ID) of the instance. If the name is left blank, Terraform will randomly generate one when the instance is first created.

`NumNodes` - (Optional, Computed) The number of nodes allocated to this instance. Defaults to `1`. This can be updated after creation.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Labels` - (Optional) A mapping (key/value pairs) of labels to assign to the instance.


## Return Values

### Fn::GetAtt

`State` - The current state of the instance.

## See Also

* [google_spanner_instance](https://www.terraform.io/docs/providers/google/r/spanner_instance.html) in the _Terraform Provider Documentation_