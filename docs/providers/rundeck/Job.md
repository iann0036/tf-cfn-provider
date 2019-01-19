# Terraform::Rundeck::Job

The job resource allows Rundeck jobs to be managed by Terraform. In Rundeck a job is a particular
named set of steps that can be executed against one or more of the nodes configured for its
associated project.

Each job belongs to a project. A project can be created with the `Terraform::Rundeck::Project` resource.

## Properties

`Name` - (Required) The name of the job, used to describe the job in the Rundeck UI.

`Description` - (Required) A longer description of the job, describing the job in the Rundeck UI.

`ProjectName` - (Required) The name of the project that this job should belong to.

`GroupName` - (Optional) The name of a group within the project in which to place the job. Setting this creates collapsable subcategories within the Rundeck UI's project job index.

`LogLevel` - (Optional) The log level that Rundeck should use for this job. Defaults to "INFO".

`Schedule` - (Optional) The jobs schedule in Unix crontab format.

`AllowConcurrentExecutions` - (Optional) Boolean defining whether two or more executions of this job can run concurrently. The default is `false`, meaning that jobs will only run sequentially.

`MaxThreadCount` - (Optional) The maximum number of threads to use to execute this job, which controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that the nodes will be visited sequentially.

`ContinueOnError` - (Optional) Boolean defining whether Rundeck will continue to run subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution will stop and the execution will be considered to have failed.

`RankAttribute` - (Optional) The name of the attribute that will be used to decide in which order the nodes will be visited while executing the job across multiple nodes.

`RankOrder` - (Optional) Keyword deciding which direction the nodes are sorted in terms of the chosen `RankAttribute`. May be either "ascending" (the default) or "descending".

`NodeFilterQuery` - (Optional) A query string using [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax) that defines which subset of the project's nodes will be used to execute this job.


## Return Values

### Fn::GetAtt

`Id` - A unique identifier for the job.

## See Also

* [rundeck_job](https://www.terraform.io/docs/providers/rundeck/r/job.html) in the _Terraform Provider Documentation_