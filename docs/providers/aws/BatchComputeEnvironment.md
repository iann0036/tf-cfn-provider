# Terraform::AWS::BatchComputeEnvironment

Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.

For information about AWS Batch, see [What is AWS Batch?][1] .
For information about compute environment, see [Compute Environments][2] .

~> **Note:** To prevent a race condition during environment deletion, make sure to set `depends_on` to the related `Terraform::AWS::IamRolePolicyAttachment`;
   otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the `DELETING` state, see [Troubleshooting AWS Batch][3] .

## Properties

`ComputeEnvironmentName` - (Required) The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.

`ComputeResources` - (Optional) Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.

`ServiceRole` - (Required) The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

`State` - (Optional) The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.

`Type` - (Required) The type of the compute environment. Valid items are `MANAGED` or `UNMANAGED`.

`BidPercentage` - (Optional) Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (`20`), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.

`DesiredVcpus` - (Optional) The desired number of EC2 vCPUS in the compute environment.

`Ec2KeyPair` - (Optional) The EC2 key pair that is used for instances launched in the compute environment.

`ImageId` - (Optional) The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

`InstanceRole` - (Required) The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.

`InstanceType` - (Required) A list of instance types that may be launched.

`MaxVcpus` - (Required) The maximum number of EC2 vCPUs that an environment can reach.

`MinVcpus` - (Required) The minimum number of EC2 vCPUs that an environment should maintain.

`SecurityGroupIds` - (Required) A list of EC2 security group that are associated with instances launched in the compute environment.

`SpotIamFleetRole` - (Optional) The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.

`Subnets` - (Required) A list of VPC subnets into which the compute resources are launched.

`Tags` - (Optional) Key-value pair tags to be applied to resources that are launched in the compute environment.

`Type` - (Required) The type of compute environment. Valid items are `EC2` or `SPOT`.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the compute environment.

`EcsClusterArn` - The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.

`Status` - The current status of the compute environment (for example, CREATING or VALID).

`StatusReason` - A short, human-readable string to provide additional details about the current status of the compute environment.

## See Also

* [aws_batch_compute_environment](https://www.terraform.io/docs/providers/aws/r/batch_compute_environment.html) in the _Terraform Provider Documentation_