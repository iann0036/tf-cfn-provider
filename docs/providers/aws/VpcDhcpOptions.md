# Terraform::AWS::VpcDhcpOptions

Provides a VPC DHCP Options resource.

## Properties

`DomainName` - (Optional) the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.

`DomainNameServers` - (Optional) List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.

`NtpServers` - (Optional) List of NTP servers to configure.

`NetbiosNameServers` - (Optional) List of NETBIOS name servers.

`NetbiosNodeType` - (Optional) The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the DHCP Options Set.

`OwnerId` - The ID of the AWS account that owns the DHCP options set.

## See Also

* [aws_vpc_dhcp_options](https://www.terraform.io/docs/providers/aws/r/vpc_dhcp_options.html) in the _Terraform Provider Documentation_