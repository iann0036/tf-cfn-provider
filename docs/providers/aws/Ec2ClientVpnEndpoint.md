# Terraform::AWS::Ec2ClientVpnEndpoint

Provides an AWS Client VPN endpoint for OpenVPN clients. For more information on usage, please see the 
[AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

## Properties

`Description` - (Optional) Name of the repository.

`ClientCidrBlock` - (Required) The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.

`DnsServers` - (Optional) Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.

`ServerCertificateArn` - (Required) The ARN of the ACM server certificate.

`TransportProtocol` - (Optional) The transport protocol to be used by the VPN session. Default value is `udp`.

`AuthenticationOptions` - (Required) Information about the authentication method to be used to authenticate clients.

`ConnectionLogOptions` - (Required) Information about the client connection logging options.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Client VPN endpoint.

`DnsName` - The DNS name to be used by clients when establishing their VPN session.

`Status` - The current state of the Client VPN endpoint.

## See Also

* [aws_ec2_client_vpn_endpoint](https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint.html) in the _Terraform Provider Documentation_