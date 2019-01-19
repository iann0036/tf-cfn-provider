# Terraform::Alicloud::SslVpnServer

Provides a SSL VPN server resource. [Refer to details](https://www.alibabacloud.com/help/doc-detail/64960.htm)

~> **NOTE:** Terraform will auto build ssl vpn server while it uses `Terraform::Alicloud::SslVpnServer` to build a ssl vpn server resource.

## Properties

`Name` - (Optional) The name of the SSL-VPN server.

`VpnGatewayId` - (Required, ForceNew) The ID of the VPN gateway.

`ClientIpPool` - (Required) The CIDR block from which access addresses are allocated to the virtual network interface card of the client.

`LocalSubnet` - (Required) The CIDR block to be accessed by the client through the SSL-VPN connection.

`Protocol` - (Optional) The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP.

`Cipher` - (Optional) The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none.

`Port` - (Optional) The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].

`Compress` - (Optional) Specify whether to compress the communication. Valid value: true (default) | false.


## Return Values

### Fn::GetAtt

`Id` - The ID of the SSL-VPN server.

`InternetIp` - The internet IP of the SSL-VPN server.

`Connections` - The number of current connections.

`MaxConnections` - The maximum number of connections.

## See Also

* [alicloud_ssl_vpn_server](https://www.terraform.io/docs/providers/alicloud/r/ssl_vpn_server.html) in the _Terraform Provider Documentation_