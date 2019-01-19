# Terraform::AWS::BatchComputeEnvironment

Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.

For information about AWS Batch, see [What is AWS Batch?][1] .
For information about compute environment, see [Compute Environments][2] .

~> **Note:** To prevent a race condition during environment deletion, make sure to set `depends_on` to the related `aws_iam_role_policy_attachment`;
   otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the `DELETING` state, see [Troubleshooting AWS Batch][3] .

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the compute environment.

`EcsClusterArn` - The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.

`Status` - The current status of the compute environment (for example, CREATING or VALID).

`StatusReason` - A short, human-readable string to provide additional details about the current status of the compute environment.

## See Also

* [aws_batch_compute_environment](https://www.terraform.io/docs/providers/aws/r/batch_compute_environment.html) in the _Terraform Provider Documentation_