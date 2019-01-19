# Terraform::AWS::Elb

Provides an Elastic Load Balancer resource, also known as a "Classic
Load Balancer" after the release of
[Application/Network Load Balancers](/docs/providers/aws/r/lb.html).

~> **NOTE on ELB Instances and ELB Attachments:** Terraform currently
provides both a standalone [ELB Attachment resource](elb_attachment.html)
(describing an instance attached to an ELB), and an ELB resource with
`instances` defined in-line. At this time you cannot use an ELB with in-line
instances in conjunction with a ELB Attachment resources. Doing so will cause a
conflict and will overwrite attachments.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The name of the ELB.

`Arn` - The ARN of the ELB.

`Name` - The name of the ELB.

`DnsName` - The DNS name of the ELB.

`Instances` - The list of instances in the ELB.

`SourceSecurityGroup` - The name of the security group that you can use as.

`SourceSecurityGroupId` - The ID of the security group that you can use as.

`ZoneId` - The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record).

## See Also

* [aws_elb](https://www.terraform.io/docs/providers/aws/r/elb.html) in the _Terraform Provider Documentation_