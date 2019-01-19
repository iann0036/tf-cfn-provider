# Terraform::OVH::IpReverse

Provides a OVH IP reverse.

## Properties

`Ip` - (Required) The IP block to which the IP belongs.

`Reverse` - (Required) The value of the reverse.

`Ipreverse` - (Optional) The IP to set the reverse of, default to `Ip` if `Ip` is a /32 (IPv4) or a /128 (IPv6).


## Return Values

### Fn::GetAtt

`Ipreverse` - The IP to set the reverse of.

`Reverse` - The value of the reverse.

## See Also

* [ovh_ip_reverse](https://www.terraform.io/docs/providers/ovh/r/ip_reverse.html) in the _Terraform Provider Documentation_