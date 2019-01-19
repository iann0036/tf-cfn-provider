# Terraform::Alicloud::SslVpnClientCert

Provides a SSL VPN client cert resource.

~> **NOTE:** Terraform will auto build SSL VPN client certs  while it uses `Terraform::Alicloud::SslVpnClientCert` to build a ssl vpn client certs resource.
             It depends on VPN instance and SSL VPN Server.

## Properties

`Name` - (Optional) The name of the client certificate.

`SslVpnServerId` - (Required, Forces new resource) The ID of the SSL-VPN server.


## Return Values

### Fn::GetAtt

`Id` - The ID of the SSL-VPN client certificate.

`Status` - The status of the client certificate.

## See Also

* [alicloud_ssl_vpn_client_cert](https://www.terraform.io/docs/providers/alicloud/r/ssl_vpn_client_cert.html) in the _Terraform Provider Documentation_