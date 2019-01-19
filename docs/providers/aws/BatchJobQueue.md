# Terraform::AWS::BatchJobQueue

Provides a Batch Job Queue resource.

## Properties

`Name` - (Required) Specifies the name of the job queue.

`ComputeEnvironments` - (Required) Specifies the set of compute environments mapped to a job queue and their order.  The position of the compute environments in the list will dictate the order. You can associate up to 3 compute environments with a job queue.

`Priority` - (Required) The priority of the job queue. Job queues with a higher priority are evaluated first when associated with the same compute environment.

`State` - (Required) The state of the job queue. Must be one of: `ENABLED` or `DISABLED`.


## See Also

* [aws_batch_job_queue](https://www.terraform.io/docs/providers/aws/r/batch_job_queue.html) in the _Terraform Provider Documentation_