# Terraform::AWS::Instance

Provides an EC2 instance resource. This allows instances to be created, updated,
and deleted. Instances also support [provisioning](/docs/provisioners/index.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The instance ID.

`Arn` - The ARN of the instance.

`AvailabilityZone` - The availability zone of the instance.

`PlacementGroup` - The placement group of the instance.

`KeyName` - The key name of the instance.

`PasswordData` - Base-64 encoded encrypted password data for the instance.

`PublicDns` - The public DNS name assigned to the instance. For EC2-VPC, this.

`PublicIp` - The public IP address assigned to the instance, if applicable. **NOTE**: If you are using an [`aws_eip`](/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address directly and not use `public_ip`, as this field will change after the EIP is attached.

`Ipv6Addresses` - A list of assigned IPv6 addresses, if any.

`NetworkInterfaceId` - The ID of the network interface that was created with the instance.

`PrimaryNetworkInterfaceId` - The ID of the instance's primary network interface.

`PrivateDns` - The private DNS name assigned to the instance. Can only be.

`PrivateIp` - The private IP address assigned to the instance.

`SecurityGroups` - The associated security groups.

`VpcSecurityGroupIds` - The associated security groups in non-default VPC.

`SubnetId` - The VPC subnet ID.

`CreditSpecification` - Credit specification of instance.

## See Also

* [aws_instance](https://www.terraform.io/docs/providers/aws/r/instance.html) in the _Terraform Provider Documentation_