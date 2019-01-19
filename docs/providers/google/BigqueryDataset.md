# Terraform::Google::BigqueryDataset

Creates a dataset resource for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The URI of the created resource.

`Etag` - A hash of the resource.

`CreationTime` - The time when this dataset was created, in milliseconds since the epoch.

`LastModifiedTime` -  The date when this dataset or any of its tables was last modified,.

## See Also

* [google_bigquery_dataset](https://www.terraform.io/docs/providers/google/r/bigquery_dataset.html) in the _Terraform Provider Documentation_