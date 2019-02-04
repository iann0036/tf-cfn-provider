# Terraform::AWS::Lb

Provides a Load Balancer resource.

~> **Note:** `Terraform::AWS::Alb` is known as `awsLb`. The functionality is identical.

## Properties

`Name` - (Optional) The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with `tf-lb`.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Internal` - (Optional) If true, the LB will be internal.

`LoadBalancerType` - (Optional) The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.

`SecurityGroups` - (Optional) A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.

`AccessLogs` - (Optional) An Access Logs block. Access Logs documented below. Only valid for Load Balancers of type `application`.

`Subnets` - (Optional) A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type `network`. Changing this value
for load balancers of type `network` will force a recreation of the resource.

`SubnetMapping` - (Optional) A subnet mapping block as documented below.

`IdleTimeout` - (Optional) The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.

`EnableDeletionProtection` - (Optional) If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent Terraform from deleting the load balancer. Defaults to `false`.

`EnableCrossZoneLoadBalancing` - (Optional) If true, cross-zone load balancing of the load balancer will be enabled.
This is a `network` load balancer feature. Defaults to `false`.

`EnableHttp2` - (Optional) Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.

`IpAddressType` - (Optional) The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### AccessLogs Properties

`Bucket` - (Required) The S3 bucket name to store the logs in.

`Prefix` - (Optional) The S3 bucket prefix. Logs are stored in the root if not configured.

`Enabled` - (Optional) Boolean to enable / disable `AccessLogs`. Defaults to `false`, even when `Bucket` is specified.

### SubnetMapping Properties

`SubnetId` - (Required) The id of the subnet of which to attach to the load balancer. You can specify only one subnet per Availability Zone.

`AllocationId` - (Optional) The allocation ID of the Elastic IP address.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the load balancer (matches `arn`).

`Arn` - The ARN of the load balancer (matches `id`).

`ArnSuffix` - The ARN suffix for use with CloudWatch Metrics.

`DnsName` - The DNS name of the load balancer.

`ZoneId` - The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).

## See Also

* [aws_lb](https://www.terraform.io/docs/providers/aws/r/lb.html) in the _Terraform Provider Documentation_