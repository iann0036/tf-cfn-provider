# Terraform::Google::BigtableInstance

Creates a Google Bigtable instance. For more information see
[the official documentation](https://cloud.google.com/bigtable/) and
[API](https://cloud.google.com/bigtable/docs/go/reference).

## Properties

`Name` - (Required) The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.

`Cluster` - (Required) A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`InstanceType` - (Optional) The instance type to create. One of `"DEVELOPMENT"` or `"PRODUCTION"`. Defaults to `"PRODUCTION"`.

`DisplayName` - (Optional) The human-readable display name of the Bigtable instance. Defaults to the instance `Name`.

`ClusterId` - (Required) The ID of the Cloud Bigtable cluster.

`Zone` - (Required) The zone to create the Cloud Bigtable cluster in. Each cluster must have a different zone in the same region. Zones that support Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).

`NumNodes` - (Optional) The number of nodes in your Cloud Bigtable cluster. Required, with a minimum of `3` for a `PRODUCTION` instance. Must be left unset for a `DEVELOPMENT` instance.

`StorageType` - (Optional) The storage type to use. One of `"SSD"` or `"HDD"`. Defaults to `"SSD"`.


## See Also

* [google_bigtable_instance](https://www.terraform.io/docs/providers/google/r/bigtable_instance.html) in the _Terraform Provider Documentation_