# Terraform::AWS::Ec2ClientVpnNetworkAssociation

Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the 
[AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

## Properties

`ClientVpnEndpointId` - (Required) The ID of the Client VPN endpoint.

`SubnetId` - (Required) The ID of the subnet to associate with the Client VPN endpoint.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the target network association.

`SecurityGroups` - The IDs of the security groups applied to the target network association.

`Status` - The current state of the target network association.

`VpcId` - The ID of the VPC in which the target network (subnet) is located.

## See Also

* [aws_ec2_client_vpn_network_association](https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_network_association.html) in the _Terraform Provider Documentation_