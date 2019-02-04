# Terraform::HCloud::Rdns

Provides a Hetzner Cloud Reverse DNS Entry to create, modify and reset reverse dns entries for Hetzner Cloud Floating IPs or servers.

## Properties

`DnsPtr` - (Required, string) The DNS address the `IpAddress` should resolve to.
- `IpAddress` - (Required, string) The IP address that should point to `DnsPtr`.
- `ServerId` - (Required, int) The server the `IpAddress` belongs to.
- `FloatingIpId` - (Required, int) The Floating IP the `IpAddress` belongs to.

`IpAddress` - (Required, string) The IP address that should point to `DnsPtr`.
- `ServerId` - (Required, int) The server the `IpAddress` belongs to.
- `FloatingIpId` - (Required, int) The Floating IP the `IpAddress` belongs to.

`ServerId` - (Required, int) The server the `IpAddress` belongs to.
- `FloatingIpId` - (Required, int) The Floating IP the `IpAddress` belongs to.

`FloatingIpId` - (Required, int) The Floating IP the `IpAddress` belongs to.


## See Also

* [hcloud_rdns](https://www.terraform.io/docs/providers/hcloud/r/rdns.html) in the _Terraform Provider Documentation_