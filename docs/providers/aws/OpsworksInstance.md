# Terraform::AWS::OpsworksInstance

Provides an OpsWorks instance resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The id of the OpsWorks instance.

`AgentVersion` - The AWS OpsWorks agent version.

`AvailabilityZone` - The availability zone of the instance.

`Ec2InstanceId` - EC2 instance ID.

`SshKeyName` - The key name of the instance.

`PublicDns` - The public DNS name assigned to the instance. For EC2-VPC, this.

`PublicIp` - The public IP address assigned to the instance, if applicable.

`PrivateDns` - The private DNS name assigned to the instance. Can only be.

`PrivateIp` - The private IP address assigned to the instance.

`SubnetId` - The VPC subnet ID.

`Tenancy` - The Instance tenancy.

`SecurityGroupIds` - The associated security groups.

## See Also

* [aws_opsworks_instance](https://www.terraform.io/docs/providers/aws/r/opsworks_instance.html) in the _Terraform Provider Documentation_