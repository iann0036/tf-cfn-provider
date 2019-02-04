# Terraform::Cloudflare::SpectrumApplication

Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare's DDoS, TLS, and IP Firewall to your other TCP-based services.

## Properties

`Protocol` - (Required) The port configuration at Cloudflare’s edge. e.g. `tcp/22`.

`Dns` - (Required) The name and type of DNS record for the Spectrum application. Fields documented below.

`OriginDirect` - (Optional) A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.

`OriginDns` - (Optional) A destination DNS addresses to the origin. Fields documented below.

`OriginPort` - (Optional) If using `OriginDns` this is a required attribute. Origin port to proxy traffice to e.g. `22`.

`Tls` - (Optional) TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.

`IpFirewall` - (Optional) Enables the IP Firewall for this application. Defaults to `true`.

`ProxyProtocol` - (Optional) Enables Proxy Protocol v1 to the origin. Defaults to `false`.

`Type` - (Required) The type of DNS record associated with the application. Valid values: `CNAME`.

`Name` - (Required) The name of the DNS record associated with the application.i.e. `ssh.example.com`.

`Name` - (Required) Fully qualified domain name of the origin e.g. origin-ssh.example.com.


## Return Values

### Fn::GetAtt

`Id` - Unique identifier in the API for the spectrum application.

## See Also

* [cloudflare_spectrum_application](https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application.html) in the _Terraform Provider Documentation_