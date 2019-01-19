# Terraform::BIGIP::LtmSnat

`Terraform::BIGIP::LtmSnat` Manages a snat configuration

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the snat.

`Partition` - (Optional) Displays the administrative partition within which this profile resides.

`Origins` - (Optional) IP or hostname of the snat.

`Snatpool` - (Optional) Specifies the name of a SNAT pool. You can only use this option when automap and translation are not used.

`Mirror` - (Optional) Enables or disables mirroring of SNAT connections.

`Sourceport` - (Optional) Specifies whether the system preserves the source port of the connection. The default is preserve. Use of the preserve-strict setting should be restricted to UDP only under very special circumstances such as nPath or transparent (that is, no translation of any other L3/L4 field), where there is a 1:1 relationship between virtual IP addresses and node addresses, or when clustered multi-processing (CMP) is disabled. The change setting is useful for obfuscating internal network addresses.

`Translation` - (Optional) Specifies the name of a translated IP address. Note that translated addresses are outside the traffic management system. You can only use this option when automap and snatpool are not used.

`Vlansdisabled` - (Optional) Disables the SNAT on all VLANs.

`Vlans` - (Optional) Specifies the name of the VLAN to which you want to assign the SNAT. The default is vlans-enabled.


## See Also

* [bigip_ltm_snat](https://www.terraform.io/docs/providers/bigip/r/ltm_snat.html) in the _Terraform Provider Documentation_