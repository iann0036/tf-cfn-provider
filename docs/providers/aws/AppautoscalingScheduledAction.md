# Terraform::AWS::AppautoscalingScheduledAction

Provides an Application AutoScaling ScheduledAction resource.

## Properties

`Name` - (Required) The name of the scheduled action.

`ServiceNamespace` - (Required) The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs.

`ResourceId` - (Required) The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId).

`ScalableDimension` - (Optional) The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount.

`ScalableTargetAction` - (Optional) The new minimum and maximum capacity. You can set both values or just one. See [below](#scalable-target-action-arguments).

`Schedule` - (Optional) The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule).

`StartTime` - (Optional) The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z.

`EndTime` - (Optional) The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the scheduled action.

## See Also

* [aws_appautoscaling_scheduled_action](https://www.terraform.io/docs/providers/aws/r/appautoscaling_scheduled_action.html) in the _Terraform Provider Documentation_