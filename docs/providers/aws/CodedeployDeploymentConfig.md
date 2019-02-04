# Terraform::AWS::CodedeployDeploymentConfig

Provides a CodeDeploy deployment config for an application

## Properties

`DeploymentConfigName` - (Required) The name of the deployment config.

`ComputePlatform` - (Optional) The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.

`MinimumHealthyHosts` - (Optional) A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.

`TrafficRoutingConfig` - (Optional) A traffic_routing_config block. Traffic Routing Config is documented below.

### MinimumHealthyHosts Properties

`Type` - (Required) The type can either be `FLEET_PERCENT` or `HOST_COUNT`.

`Value` - (Required) The value when the type is `FLEET_PERCENT` represents the minimum number of healthy instances as
a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
When the type is `HOST_COUNT`, the value represents the minimum number of healthy instances as an absolute value.

### TrafficRoutingConfig Properties

`Type` - (Optional) Type of traffic routing config. One of `TimeBasedCanary`, `TimeBasedLinear`, `AllAtOnce`.

`TimeBasedCanary` - (Optional) The time based canary configuration information. If `Type` is `TimeBasedLinear`, use `TimeBasedLinear` instead.

`TimeBasedLinear` - (Optional) The time based linear configuration information. If `Type` is `TimeBasedCanary`, use `TimeBasedCanary` instead.

### TimeBasedCanary Properties

`Interval` - (Optional) The number of minutes between the first and second traffic shifts of a `TimeBasedCanary` deployment.

`Percentage` - (Optional) The percentage of traffic to shift in the first increment of a `TimeBasedCanary` deployment.

### TimeBasedLinear Properties

`Interval` - (Optional) The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.

`Percentage` - (Optional) The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.


## Return Values

### Fn::GetAtt

`Id` - The deployment group's config name.

`DeploymentConfigId` - The AWS Assigned deployment config id.

## See Also

* [aws_codedeploy_deployment_config](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config.html) in the _Terraform Provider Documentation_