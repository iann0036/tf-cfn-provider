# Terraform::Google::BigqueryTable

Creates a table resource in a dataset for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

## Properties

TBC

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