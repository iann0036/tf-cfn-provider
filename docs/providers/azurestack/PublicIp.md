# Terraform::AzureStack::PublicIp

Manages a Public IP Address.

## Properties

`Name` - (Required) Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the public ip.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`PublicIpAddressAllocation` - (Required) Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

`IdleTimeoutInMinutes` - (Optional) Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

`DomainNameLabel` - (Optional) Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

`ReverseFqdn` - (Optional) A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Public IP ID.

`IpAddress` - The IP address value that was allocated.

`Fqdn` - Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.

## See Also

* [azurestack_public_ip](https://www.terraform.io/docs/providers/azurestack/r/public_ip.html) in the _Terraform Provider Documentation_