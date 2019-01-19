# Terraform::AWS::SpotInstanceRequest

Provides an EC2 Spot Instance Request resource. This allows instances to be
requested on the spot market.

By default Terraform creates Spot Instance Requests with a `persistent` type,
which means that for the duration of their lifetime, AWS will launch an
instance with the configured details if and when the spot market will accept
the requested price.

On destruction, Terraform will make an attempt to terminate the associated Spot
Instance if there is one present.

Spot Instances requests with a `one-time` type will close the spot request
when the instance is terminated either by the request being below the current spot
price availability or by a user.

~> **NOTE:** Because their behavior depends on the live status of the spot
market, Spot Instance Requests have a unique lifecycle that makes them behave
differently than other Terraform resources. Most importantly: there is __no
guarantee__ that a Spot Instance exists to fulfill the request at any given
point in time. See the [AWS Spot Instance
documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
for more information.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Spot Instance Request ID.

`SpotBidStatus` - The current [bid.

`SpotInstanceId` - The Instance ID (if any) that is currently fulfilling.

`PublicDns` - The public DNS name assigned to the instance. For EC2-VPC, this.

`PublicIp` - The public IP address assigned to the instance, if applicable.

`PrivateDns` - The private DNS name assigned to the instance. Can only be.

`PrivateIp` - The private IP address assigned to the instance.

## See Also

* [aws_spot_instance_request](https://www.terraform.io/docs/providers/aws/r/spot_instance_request.html) in the _Terraform Provider Documentation_