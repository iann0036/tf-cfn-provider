# Terraform::Google::BigqueryTable

Creates a table resource in a dataset for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

## Properties

`DatasetId` - (Required) The dataset ID to create the table in.
Changing this forces a new resource to be created.

`TableId` - (Required) A unique ID for the resource.
Changing this forces a new resource to be created.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

`Description` - (Optional) The field description.

`ExpirationTime` - (Optional) The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.

`FriendlyName` - (Optional) A descriptive name for the table.

`Labels` - (Optional) A mapping of labels to assign to the resource.

`Schema` - (Optional) A JSON schema for the table.

`TimePartitioning` - (Optional) If specified, configures time-based
partitioning for this table. Structure is documented below.

`View` - (Optional) If specified, configures this table as a view.
Structure is documented below.

### TimePartitioning Properties

`ExpirationMs` -  (Optional) Number of milliseconds for which to keep the
storage for a partition.

`Field` - (Optional) The field used to determine how to create a time-based
partition. If time-based partitioning is enabled without this value, the
table is partitioned based on the load time.

`Type` - (Required) The only type supported is DAY, which will generate
one partition per day based on data loading time.

`RequirePartitionFilter` - (Optional) If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.

### View Properties

`Query` - (Required) A query that BigQuery executes when the view is referenced.

`UseLegacySql` - (Optional) Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.


## Return Values

### Fn::GetAtt

`CreationTime` - The time when this table was created, in milliseconds since the epoch.

`Etag` - A hash of the resource.

`LastModifiedTime` - The time when this table was last modified, in milliseconds since the epoch.

`Location` - The geographic location where the table resides. This value is inherited from the dataset.

`NumBytes` - The size of this table in bytes, excluding any data in the streaming buffer.

`NumLongTermBytes` - The number of bytes in the table that are considered "long-term storage".

`NumRows` - The number of rows of data in this table, excluding any data in the streaming buffer.

`SelfLink` - The URI of the created resource.

`Type` - Describes the table type.

## See Also

* [google_bigquery_table](https://www.terraform.io/docs/providers/google/r/bigquery_table.html) in the _Terraform Provider Documentation_