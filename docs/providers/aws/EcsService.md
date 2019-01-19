# Terraform::AWS::EcsService

-> **Note:** To prevent a race condition during service deletion, make sure to set `depends_on` to the related `aws_iam_role_policy`; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the `DRAINING` state.

Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).

See [ECS Services section in AWS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Amazon Resource Name (ARN) that identifies the service.

`Name` - The name of the service.

`Cluster` - The Amazon Resource Name (ARN) of cluster which the service runs on.

`IamRole` - The ARN of IAM role used for ELB.

`DesiredCount` - The number of instances of the task definition.

## See Also

* [aws_ecs_service](https://www.terraform.io/docs/providers/aws/r/ecs_service.html) in the _Terraform Provider Documentation_