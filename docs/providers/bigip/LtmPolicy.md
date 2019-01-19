# Terraform::BIGIP::LtmPolicy

`Terraform::BIGIP::LtmPolicy` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the Policy.

`Strategy` - (Optional) Specifies the match strategy.

`Requires` - (Optional) Specifies the protocol.

`PublishedCopy` - (Optional) If you want to publish the policy else it will be deployed in Drafts mode.

`Controls` - (Optional) Specifies the controls.

`Rule` - (Optional) Rules can be applied using the policy.

`TmName` - (Required) If Rule is used then you need to provide the tm_name it can be any value.

`Forward` - (Optional) This action will affect forwarding.

`Pool` - (Optional ) This action will direct the stream to this pool.


## See Also

* [bigip_ltm_policy](https://www.terraform.io/docs/providers/bigip/r/ltm_policy.html) in the _Terraform Provider Documentation_