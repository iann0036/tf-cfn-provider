# Terraform::BIGIP::LtmPoolAttachment

`Terraform::BIGIP::LtmPoolAttachment` Manages nodes membership in pools

Resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Pool` - (Required) Name of the pool in /Partition/Name format.

`Node` - (Required) Node to add to the pool in /Partition/NodeName:Port format (e.g. /Common/Node01:80).


## See Also

* [bigip_ltm_pool_attachment](https://www.terraform.io/docs/providers/bigip/r/ltm_pool_attachment.html) in the _Terraform Provider Documentation_