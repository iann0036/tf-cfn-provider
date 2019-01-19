# Terraform::OneAndOne::Ip

Manages a Public IP on 1&1

## Properties

`IpType` - (Required) IP type. Can be `IPV4` or `IPV6`.

`ReverseDns` - (Optional).

`Datacenter` - (Optional) Location of desired 1and1 datacenter. Can be `DE`, `GB`, `US` or `ES`.

`IpAddress` - (Computed) The IP address.


## See Also

* [oneandone_ip](https://www.terraform.io/docs/providers/oneandone/r/ip.html) in the _Terraform Provider Documentation_