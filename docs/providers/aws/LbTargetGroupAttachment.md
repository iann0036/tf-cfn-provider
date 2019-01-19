# Terraform::AWS::LbTargetGroupAttachment

Provides the ability to register instances and containers with an Application Load Balancer (ALB) or Network Load Balancer (NLB) target group. For attaching resources with Elastic Load Balancer (ELB), see the [`Terraform::AWS::ElbAttachment` resource](/docs/providers/aws/r/elb_attachment.html).

~> **Note:** `Terraform::AWS::AlbTargetGroupAttachment` is known as `awsLbTargetGroupAttachment`. The functionality is identical.

## Properties

`TargetGroupArn` - (Required) The ARN of the target group with which to register targets.

`Port` - (Optional) The port on which targets receive traffic.

`AvailabilityZone` - (Optional) The Availability Zone where the IP address of the target is to be registered.


## Return Values

### Fn::GetAtt

`Id` - A unique identifier for the attachment.

## See Also

* [aws_lb_target_group_attachment](https://www.terraform.io/docs/providers/aws/r/lb_target_group_attachment.html) in the _Terraform Provider Documentation_