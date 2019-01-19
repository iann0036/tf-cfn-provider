# Terraform::BIGIP::LtmPool

`Terraform::BIGIP::LtmPool` Manages a pool configuration.

Resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the pool.

`Monitors` - (Optional) List of monitor names to associate with the pool.

`AllowNat` - (Optional).

`AllowSnat` - (Optional).

`LoadBalancingMode` - (Optional, Default = round-robin).


## See Also

* [bigip_ltm_pool](https://www.terraform.io/docs/providers/bigip/r/ltm_pool.html) in the _Terraform Provider Documentation_