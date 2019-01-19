# Terraform::Brightbox::Cloudip

Provides a Brightbox CloudIP resource.

## Properties

`Target` - (Required) The CloudIP mapping target. This is the interface from a server, or the id of a load balancer or cloud sql resource.

`Name` - (Optional) a label to assign to the CloudIP.

`ReverseDns` - (Optional) The reverse DNS entry for the CloudIP.


## Return Values

### Fn::GetAtt

`Id` - The ID of the CloudIP.

`Fqdn` - Fully Qualified Domain Name of the CloudIP.

`PublicIp` - the public IPV4 address of the CloudIP.

`Status` - Current state of the CloudIP: `mapped` or `unmapped`.

`Username` - The username used to log onto the server.

## See Also

* [brightbox_cloudip](https://www.terraform.io/docs/providers/brightbox/r/cloudip.html) in the _Terraform Provider Documentation_