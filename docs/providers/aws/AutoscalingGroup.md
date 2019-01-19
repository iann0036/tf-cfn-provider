# Terraform::AWS::AutoscalingGroup

Provides an AutoScaling Group resource.

-> **Note:** You must specify either `launch_configuration`, `launch_template`, or `mixed_instances_policy`.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The autoscaling group id.

`Arn` - The ARN for this AutoScaling Group.

`AvailabilityZones` - The availability zones of the autoscale group.

`MinSize` - The minimum size of the autoscale group.

`MaxSize` - The maximum size of the autoscale group.

`DefaultCooldown` - Time between a scaling activity and the succeeding scaling activity.

`Name` - The name of the autoscale group.

`HealthCheckGracePeriod` - Time after instance comes into service before checking health.

`HealthCheckType` - "EC2" or "ELB". Controls how health checking is done.

`LaunchConfiguration` - The launch configuration of the autoscale group.

## See Also

* [aws_autoscaling_group](https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html) in the _Terraform Provider Documentation_