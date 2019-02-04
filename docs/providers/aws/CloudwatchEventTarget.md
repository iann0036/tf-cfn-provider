# Terraform::AWS::CloudwatchEventTarget

Provides a CloudWatch Event Target resource.

## Properties

`Rule` - (Required) The name of the rule you want to add targets to.

`TargetId` - (Optional) The unique target assignment ID.  If missing, will generate a random, unique id.

`Arn` - (Required) The Amazon Resource Name (ARN) associated of the target.

`Input` - (Optional) Valid JSON text passed to the target.

`InputPath` - (Optional) The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

`RoleArn` - (Optional) The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `EcsTarget` is used.

`RunCommandTargets` - (Optional) Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

`EcsTarget` - (Optional) Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

`BatchTarget` - (Optional) Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

`KinesisTarget` - (Optional) Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

`SqsTarget` - (Optional) Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

`InputTransformer` - (Optional) Parameters used when you are providing a custom input to a target based on certain event data.

### RunCommandTargets Properties

`Key` - (Required) Can be either `tag:tag-key` or `InstanceIds`.

`Values` - (Required) If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.

### EcsTarget Properties

`Group` - (Optional) Specifies an ECS task group for the task. The maximum length is 255 characters.

`LaunchType` - (Optional) Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.

`NetworkConfiguration` - (Optional) Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.

`PlatformVersion` - (Optional) Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

`TaskCount` - (Optional) The number of tasks to create based on the TaskDefinition. The default is 1.

`TaskDefinitionArn` - (Required) The ARN of the task definition to use if the event target is an Amazon ECS cluster.

### NetworkConfiguration Properties

`Subnets` - (Required) The subnets associated with the task or service.

`SecurityGroups` - (Optional) The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

`AssignPublicIp` - (Optional) Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.

### BatchTarget Properties

`JobDefinition` - (Required) The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.

`JobName` - (Required) The name to use for this execution of the job, if the target is an AWS Batch job.

`ArraySize` - (Optional) The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.

`JobAttempts` - (Optional) The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.

### KinesisTarget Properties

`PartitionKeyPath` - (Optional) The JSON path to be extracted from the event and used as the partition key.

### SqsTarget Properties

`MessageGroupId` - (Optional) The FIFO message group ID to use as the target.

### InputTransformer Properties

`InputPaths` - (Optional) Key value pairs specified in the form of JSONPath (for example, time = $.time).

`InputTemplate` - (Required) Structure containing the template body.


## See Also

* [aws_cloudwatch_event_target](https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target.html) in the _Terraform Provider Documentation_