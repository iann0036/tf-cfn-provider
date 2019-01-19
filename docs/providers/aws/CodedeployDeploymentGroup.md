# Terraform::AWS::CodedeployDeploymentGroup

Provides a CodeDeploy Deployment Group for a CodeDeploy Application

~> **NOTE on blue/green deployments:** When using `green_fleet_provisioning_option` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by terraform and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - Application name and deployment group name.

## See Also

* [aws_codedeploy_deployment_group](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group.html) in the _Terraform Provider Documentation_