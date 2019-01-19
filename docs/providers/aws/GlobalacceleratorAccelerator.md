# Terraform::AWS::GlobalacceleratorAccelerator

Provides a Global Accelerator accelerator.

## Properties

`Name` - (Required) The name of the accelerator.

`IpAddressType` - (Optional) The value for the address type must be `IPV4`.

`Enabled` - (Optional) Indicates whether the accelerator is enabled. The value is true or false. The default value is true.

`Attributes` - (Optional) The attributes of the accelerator. Fields documented below.

`FlowLogsEnabled` - (Optional) Indicates whether flow logs are enabled.

`FlowLogsS3Bucket` - (Optional) The name of the Amazon S3 bucket for the flow logs.

`FlowLogsS3Prefix` - (Optional) The prefix for the location in the Amazon S3 bucket for the flow logs.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) of the accelerator.

`IpSets` - IP address set associated with the accelerator.

`IpAddresses` - The array of IP addresses in the IP address set.

`IpFamily` - The types of IP addresses included in this IP set.

## See Also

* [aws_globalaccelerator_accelerator](https://www.terraform.io/docs/providers/aws/r/globalaccelerator_accelerator.html) in the _Terraform Provider Documentation_