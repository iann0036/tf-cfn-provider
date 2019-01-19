# Terraform::AWS::BatchJobDefinition

Provides a Batch Job Definition resource.

## Properties

`Name` - (Required) Specifies the name of the job definition.

`ContainerProperties` - (Optional) A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) provided as a single valid JSON document. This parameter is required if the `Type` parameter is `container`.

`Parameters` - (Optional) Specifies the parameter substitution placeholders to set in the job definition.

`RetryStrategy` - (Optional) Specifies the retry strategy to use for failed jobs that are submitted with this job definition. Maximum number of `RetryStrategy` is `1`.  Defined below.

`Timeout` - (Optional) Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `Timeout` is `1`. Defined below.

`Type` - (Required) The type of job definition.  Must be `container`.


## See Also

* [aws_batch_job_definition](https://www.terraform.io/docs/providers/aws/r/batch_job_definition.html) in the _Terraform Provider Documentation_