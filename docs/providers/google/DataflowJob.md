# Terraform::Google::DataflowJob

Creates a job on Dataflow, which is an implementation of Apache Beam running on Google Compute Engine. For more information see
the official documentation for
[Beam](https://beam.apache.org) and [Dataflow](https://cloud.google.com/dataflow/).

## Properties

`Name` - (Required) A unique name for the resource, required by Dataflow.

`TemplateGcsPath` - (Required) The GCS path to the Dataflow job template.

`TempGcsLocation` - (Required) A writeable location on GCS for the Dataflow job to dump its temporary data.

`Parameters` - (Optional) Key/Value pairs to be passed to the Dataflow job (as used in the template).

`MaxWorkers` - (Optional) The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.

`OnDelete` - (Optional) One of "drain" or "cancel".  Specifies behavior of deletion during `terraform destroy`.  See above note.

`Project` - (Optional) The project in which the resource belongs. If it is not provided, the provider project is used.

`Zone` - (Optional) The zone in which the created job should run. If it is not provided, the provider zone is used.


## Return Values

### Fn::GetAtt

`State` - The current state of the resource, selected from the [JobState enum](https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState).

## See Also

* [google_dataflow_job](https://www.terraform.io/docs/providers/google/r/dataflow_job.html) in the _Terraform Provider Documentation_