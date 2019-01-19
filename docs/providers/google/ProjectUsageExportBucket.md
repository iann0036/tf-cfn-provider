# Terraform::Google::ProjectUsageExportBucket

Sets up a usage export bucket for a particular project.  A usage export bucket
is a pre-configured GCS bucket which is set up to receive daily and monthly
reports of the GCE resources used.

For more information see the [Docs](https://cloud.google.com/compute/docs/usage-export)
and for further details, the
[API Documentation](https://cloud.google.com/compute/docs/reference/rest/beta/projects/setUsageExportBucket).

~> **Note:** You should specify only one of these per project.  If there are two or more
they will fight over which bucket the reports should be stored in.  It is
safe to have multiple resources with the same backing bucket.

## Properties


## See Also

* [google_project_usage_export_bucket](https://www.terraform.io/docs/providers/google/r/project_usage_export_bucket.html) in the _Terraform Provider Documentation_