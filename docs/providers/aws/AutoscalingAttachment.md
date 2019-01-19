# Terraform::AWS::AutoscalingAttachment

Provides an AutoScaling Attachment resource.

~> **NOTE on AutoScaling Groups and ASG Attachments:** Terraform currently provides
both a standalone ASG Attachment resource (describing an ASG attached to
an ELB), and an [AutoScaling Group resource](autoscaling_group.html) with
`load_balancers` defined in-line. At this time you cannot use an ASG with in-line
load balancers in conjunction with an ASG Attachment resource. Doing so will cause a
conflict and will overwrite attachments.

## Properties

`AutoscalingGroupName` - (Required) Name of ASG to associate with the ELB.

`Elb` - (Optional) The name of the ELB.

`AlbTargetGroupArn` - (Optional) The ARN of an ALB Target Group.


## See Also

* [aws_autoscaling_attachment](https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment.html) in the _Terraform Provider Documentation_