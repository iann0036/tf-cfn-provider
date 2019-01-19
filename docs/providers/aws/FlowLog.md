# Terraform::AWS::FlowLog

Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group or a S3 Bucket.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Flow Log ID.

## See Also

* [aws_flow_log](https://www.terraform.io/docs/providers/aws/r/flow_log.html) in the _Terraform Provider Documentation_