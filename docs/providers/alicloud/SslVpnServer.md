# Terraform::Alicloud::SslVpnServer

Provides a SSL VPN server resource. [Refer to details](https://www.alibabacloud.com/help/doc-detail/64960.htm)

~> **NOTE:** Terraform will auto build ssl vpn server while it uses `alicloud_ssl_vpn_server` to build a ssl vpn server resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the SSL-VPN server.

`InternetIp` - The internet IP of the SSL-VPN server.

`Connections` - The number of current connections.

`MaxConnections` - The maximum number of connections.

## See Also

* [alicloud_ssl_vpn_server](https://www.terraform.io/docs/providers/alicloud/r/ssl_vpn_server.html) in the _Terraform Provider Documentation_