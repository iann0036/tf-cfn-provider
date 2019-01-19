# Terraform::Brightbox::Cloudip

Provides a Brightbox CloudIP resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the CloudIP.

`Fqdn` - Fully Qualified Domain Name of the CloudIP.

`PublicIp` - the public IPV4 address of the CloudIP.

`Status` - Current state of the CloudIP: `mapped` or `unmapped`.

`Username` - The username used to log onto the server.

## See Also

* [brightbox_cloudip](https://www.terraform.io/docs/providers/brightbox/r/cloudip.html) in the _Terraform Provider Documentation_