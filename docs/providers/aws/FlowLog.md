# Terraform::AWS::FlowLog

Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group or a S3 Bucket.

## Properties

`TrafficType` - (Required) The type of traffic to capture. Valid values: `ACCEPT`,`REJECT`, `ALL`.

`EniId` - (Optional) Elastic Network Interface ID to attach to.

`IamRoleArn` - (Optional) The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group.

`LogDestinationType` - (Optional) The type of the logging destination. Valid values: `cloud-watch-logs`, `s3`. Default: `cloud-watch-logs`.

`LogDestination` - (Optional) The ARN of the logging destination.

`LogGroupName` - (Optional) *Deprecated:* Use `LogDestination` instead. The name of the CloudWatch log group.

`SubnetId` - (Optional) Subnet ID to attach to.

`VpcId` - (Optional) VPC ID to attach to.


## Return Values

### Fn::GetAtt

`Id` - The Flow Log ID.

## See Also

* [aws_flow_log](https://www.terraform.io/docs/providers/aws/r/flow_log.html) in the _Terraform Provider Documentation_