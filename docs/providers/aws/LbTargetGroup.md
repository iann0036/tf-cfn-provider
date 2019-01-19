# Terraform::AWS::LbTargetGroup

Provides a Target Group resource for use with Load Balancer resources.

~> **Note:** `aws_alb_target_group` is known as `aws_lb_target_group`. The functionality is identical.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ARN of the Target Group (matches `arn`).

`Arn` - The ARN of the Target Group (matches `id`).

`ArnSuffix` - The ARN suffix for use with CloudWatch Metrics.

`Name` - The name of the Target Group.

## See Also

* [aws_lb_target_group](https://www.terraform.io/docs/providers/aws/r/lb_target_group.html) in the _Terraform Provider Documentation_