# Terraform::Google::BigqueryDataset

Creates a dataset resource for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets).

## Properties

`DatasetId` - (Required) A unique ID for the resource.
Changing this forces a new resource to be created.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

`FriendlyName` - (Optional) A descriptive name for the dataset.

`Description` - (Optional) A user-friendly description of the dataset.

`Location` - (Optional) The geographic location where the dataset should reside.
See [official docs](https://cloud.google.com/bigquery/docs/dataset-locations).

`DefaultPartitionExpirationMs` - (Optional) The default partition expiration
for all partitioned tables in the dataset, in milliseconds.

`DefaultTableExpirationMs` - (Optional) The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).

`Labels` - (Optional) A mapping of labels to assign to the resource.

`Access` - (Optional) An array of objects that define dataset access for
one or more entities. Structure is documented below.

`Role` - (Required unless `View` is set) Describes the rights granted to
the user specified by the other member of the access object. The following
string values are supported: `READER`, `WRITER`, `OWNER`.

`Domain` - (Optional) A domain to grant access to.

`GroupByEmail` - (Optional) An email address of a Google Group to grant
access to.

`SpecialGroup` - (Optional) A special group to grant access to.
Possible values include:
* `ProjectOwners`: Owners of the enclosing project.
* `ProjectReaders`: Readers of the enclosing project.
* `ProjectWriters`: Writers of the enclosing project.
* `AllAuthenticatedUsers`: All authenticated BigQuery users.

`UserByEmail` - (Optional) An email address of a user to grant access to.

`View` - (Optional) A view from a different dataset to grant access to.
Queries executed against that view will have read access to tables in this
dataset. The role field is not required when this field is set. If that
view is updated by any user, access to the view needs to be granted again
via an update operation. Structure is documented below.

`DatasetId` - (Required) The ID of the dataset containing this table.

`ProjectId` - (Required) The ID of the project containing this table.

`TableId` - (Required) The ID of the table.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

`Etag` - A hash of the resource.

`CreationTime` - The time when this dataset was created, in milliseconds since the epoch.

`LastModifiedTime` -  The date when this dataset or any of its tables was last modified,.

## See Also

* [google_bigquery_dataset](https://www.terraform.io/docs/providers/google/r/bigquery_dataset.html) in the _Terraform Provider Documentation_