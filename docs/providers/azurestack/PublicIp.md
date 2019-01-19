# Terraform::AzureStack::PublicIp

Manages a Public IP Address.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Public IP ID.

`IpAddress` - The IP address value that was allocated.

`Fqdn` - Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.

## See Also

* [azurestack_public_ip](https://www.terraform.io/docs/providers/azurestack/r/public_ip.html) in the _Terraform Provider Documentation_