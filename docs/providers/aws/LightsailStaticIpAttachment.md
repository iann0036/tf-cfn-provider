# Terraform::AWS::LightsailStaticIpAttachment

Provides a static IP address attachment - relationship between a Lightsail static IP & Lightsail instance.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

## Properties

`StaticIpName` - (Required) The name of the allocated static IP.

`InstanceName` - (Required) The name of the Lightsail instance to attach the IP to.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the Lightsail static IP.

`IpAddress` - The allocated static IP address.

`SupportCode` - The support code.

## See Also

* [aws_lightsail_static_ip_attachment](https://www.terraform.io/docs/providers/aws/r/lightsail_static_ip_attachment.html) in the _Terraform Provider Documentation_