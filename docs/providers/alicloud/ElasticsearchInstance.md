# Terraform::Alicloud::ElasticsearchInstance

Provides a Elasticsearch instance resource. It contains data nodes, dedicated master node(optional) and etc. It can be associated with private IP whitelists and kibana IP whitelist.

~> **NOTE:** Only one operation is supported in a request. So if `DataNodeSpec` and `DataNodeDiskSize` are both changed, system will respond error.

## Properties

`Description` - (Optional) The description of instance. It a string of 0 to 30 characters.

`InstanceChargeType` - (Required) Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`.

`Period` - (Optional) The duration that you will buy Elasticsearch instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.

`DataNodeAmount` - (Required) The Elasticsearch cluster's data node quantity, between 2 and 50.

`DataNodeSpec` - (Required) The data node specifications of the Elasticsearch instance.

`DataNodeDiskSize` - (Required) The single data node storage space.
- `CloudSsd`: An SSD disk, supports a maximum of 2048 GiB (2 TB).
- `CloudEfficiency` An ultra disk, supports a maximum of 5120 GiB (5 TB). If the data to be stored is larger than 2048 GiB, an ultra disk can only support the following data sizes (GiB): [`2560`, `3072`, `3584`, `4096`, `4608`, `5120`].

`DataNodeDiskType` - (Required) The data node disk type. Supported values: cloud_ssd, cloud_efficiency.

`VswitchId` - (Required) The ID of VSwitch.

`Password` - (Required) The password of the instance. The password can be 8 to 32 characters in length and must contain three of the following conditions: uppercase letters, lowercase letters, numbers, and special characters (!@#$%^&*()_+-=).

`Version` - (Required) Elasticsearch version. Supported values: 5.5.3_with_X-Pack and 6.3_with_X-Pack.

`PrivateWhitelist` - (Optional) Set the instance's IP whitelist in VPC network.

`KibanaWhitelist` - (Optional) Set the Kibana's IP whitelist in internet network.

`MasterNodeSpec` - (Optional) The dedicated master node spec. If specified, dedicated master node will be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Elasticsearch instance.

`Domain` - Instance connection domain (only VPC network access supported).

`Port` - Instance connection port.

`KibanaDomain` - Kibana console domain (Internet access supported).

`KibanaPort` - Kibana console port.

`Status` - The Elasticsearch instance status. Includes `active`, `activating`, `inactive`. Some operations are denied when status is not `active`.

## See Also

* [alicloud_elasticsearch_instance](https://www.terraform.io/docs/providers/alicloud/r/elasticsearch_instance.html) in the _Terraform Provider Documentation_