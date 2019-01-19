# Terraform::BIGIP::LtmSnatpool

`Terraform::BIGIP::LtmSnatpool` Collections of SNAT translation addresses

Resource should be named with their "full path". The full path is the combination of the partition + name of the resource, for example /Common/my-snatpool.

## Properties

`Name` - (Required) Name of the snatpool.

`Members` - (Required) Specifies a translation address to add to or delete from a SNAT pool (at least one address is required).


## See Also

* [bigip_ltm_snatpool](https://www.terraform.io/docs/providers/bigip/r/ltm_snatpool.html) in the _Terraform Provider Documentation_