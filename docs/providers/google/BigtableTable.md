# Terraform::Google::BigtableTable

Creates a Google Cloud Bigtable table inside an instance. For more information see
[the official documentation](https://cloud.google.com/bigtable/) and
[API](https://cloud.google.com/bigtable/docs/go/reference).

## Properties

`Name` - (Required) The name of the table.

`InstanceName` - (Required) The name of the Bigtable instance.

`SplitKeys` - (Optional) A list of predefined keys to split the table on.

`ColumnFamily` - (Optional) A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

### ColumnFamily Properties

`Family` - (Optional) The name of the column family.


## See Also

* [google_bigtable_table](https://www.terraform.io/docs/providers/google/r/bigtable_table.html) in the _Terraform Provider Documentation_