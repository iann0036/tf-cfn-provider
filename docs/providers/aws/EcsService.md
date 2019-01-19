# Terraform::AWS::EcsService

-> **Note:** To prevent a race condition during service deletion, make sure to set `depends_on` to the related `Terraform::AWS::IamRolePolicy`; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the `DRAINING` state.

Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).

See [ECS Services section in AWS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

## Properties

`Name` - (Required) The name of the service (up to 255 letters, numbers, hyphens, and underscores).

`TaskDefinition` - (Required) The family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service.

`DesiredCount` - (Optional) The number of instances of the task definition to place and keep running. Defaults to 0. Do not specify if using the `DAEMON` scheduling strategy.

`LaunchType` - (Optional) The launch type on which to run your service. The valid values are `EC2` and `FARGATE`. Defaults to `EC2`.

`PlatformVersion` - (Optional) The platform version on which to run your service. Only applicable for `LaunchType` set to `FARGATE`. Defaults to `LATEST`. More information about Fargate platform versions can be found in the [AWS ECS User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

`SchedulingStrategy` - (Optional) The scheduling strategy to use for the service. The valid values are `REPLICA` and `DAEMON`. Defaults to `REPLICA`. Note that [*Fargate tasks do not support the `DAEMON` scheduling strategy*](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html).

`Cluster` - (Optional) ARN of an ECS cluster.

`IamRole` - (Optional) ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.

`DeploymentController` - (Optional) Configuration block containing deployment controller configuration. Defined below.

`DeploymentMaximumPercent` - (Optional) The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment. Not valid when using the `DAEMON` scheduling strategy.

`DeploymentMinimumHealthyPercent` - (Optional) The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

`EnableEcsManagedTags` - (Optional) Specifies whether to enable Amazon ECS managed tags for the tasks within the service.

`PropagateTags` - (Optional) Specifies whether to propagate the tags from the task definition or the service to the tasks. The valid values are `SERVICE` and `TASK_DEFINITION`.

`PlacementStrategy` - (Optional) **Deprecated**, use `OrderedPlacementStrategy` instead.

`OrderedPlacementStrategy` - (Optional) Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of `OrderedPlacementStrategy` blocks is `5`. Defined below.

`HealthCheckGracePeriodSeconds` - (Optional) Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 7200. Only valid for services configured to use load balancers.

`LoadBalancer` - (Optional) A load balancer block. Load balancers documented below.

`PlacementConstraints` - (Optional) rules that are taken into consideration during task placement. Maximum number of `PlacementConstraints` is `10`. Defined below.

`NetworkConfiguration` - (Optional) The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.

`ServiceRegistries` - (Optional) The service discovery registries for the service. The maximum number of `ServiceRegistries` blocks is `1`.

`Tags` - (Optional) Key-value mapping of resource tags.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) that identifies the service.

`Name` - The name of the service.

`Cluster` - The Amazon Resource Name (ARN) of cluster which the service runs on.

`IamRole` - The ARN of IAM role used for ELB.

`DesiredCount` - The number of instances of the task definition.

## See Also

* [aws_ecs_service](https://www.terraform.io/docs/providers/aws/r/ecs_service.html) in the _Terraform Provider Documentation_