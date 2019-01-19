# Terraform::AWS::CodedeployDeploymentGroup

Provides a CodeDeploy Deployment Group for a CodeDeploy Application

~> **NOTE on blue/green deployments:** When using `green_fleet_provisioning_option` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by terraform and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.

## Properties

`AppName` - (Required) The name of the application.

`DeploymentGroupName` - (Required) The name of the deployment group.

`ServiceRoleArn` - (Required) The service role ARN that allows deployments.

`AlarmConfiguration` - (Optional) Configuration block of alarms associated with the deployment group (documented below).

`AutoRollbackConfiguration` - (Optional) Configuration block of the automatic rollback configuration associated with the deployment group (documented below).

`AutoscalingGroups` - (Optional) Autoscaling groups associated with the deployment group.

`BlueGreenDeploymentConfig` - (Optional) Configuration block of the blue/green deployment options for a deployment group (documented below).

`DeploymentConfigName` - (Optional) The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".

`DeploymentStyle` - (Optional) Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).

`Ec2TagFilter` - (Optional) Tag filters associated with the deployment group. See the AWS docs for details.

`Ec2TagSet` - (Optional) Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.

`EcsService` - (Optional) Configuration block(s) of the ECS services for a deployment group (documented below).

`LoadBalancerInfo` - (Optional) Single configuration block of the load balancer to use in a blue/green deployment (documented below).

`OnPremisesInstanceTagFilter` - (Optional) On premise tag filters associated with the group. See the AWS docs for details.

`TriggerConfiguration` - (Optional) Configuration block(s) of the triggers for the deployment group (documented below).


## Return Values

### Fn::GetAtt

`Id` - Application name and deployment group name.

## See Also

* [aws_codedeploy_deployment_group](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group.html) in the _Terraform Provider Documentation_