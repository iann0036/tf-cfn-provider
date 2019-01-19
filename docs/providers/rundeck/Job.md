# Terraform::Rundeck::Job

The job resource allows Rundeck jobs to be managed by Terraform. In Rundeck a job is a particular
named set of steps that can be executed against one or more of the nodes configured for its
associated project.

Each job belongs to a project. A project can be created with the `rundeck_project` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - A unique identifier for the job.

## See Also

* [rundeck_job](https://www.terraform.io/docs/providers/rundeck/r/job.html) in the _Terraform Provider Documentation_