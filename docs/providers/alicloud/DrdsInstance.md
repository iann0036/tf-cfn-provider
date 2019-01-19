# Terraform::Alicloud::DrdsInstance

Distributed Relational Database Service (DRDS) is a lightweight (stateless), flexible, stable, and efficient middleware product independently developed by Alibaba Group to resolve scalability issues with single-host relational databases.
With its compatibility with MySQL protocols and syntaxes, DRDS enables database/table sharding, smooth scaling, configuration upgrade/downgrade,
transparent read/write splitting, and distributed transactions, providing O&M capabilities for distributed databases throughout their entire lifecycle.

For information about DRDS and how to use it, see [What is DRDS](https://www.alibabacloud.com/help/doc-detail/29659.htm).

-> **NOTE:** At present, DRDS instance only can be supported in the regions: cn-shenzhen, cn-beijing, cn-hangzhou, cn-hongkong, cn-qingdao.

## Properties

`Description` - (Required) Description of the DRDS instance, This description can have a string of 2 to 256 characters.

`ZoneId` - (Optional, ForceNew) The Zone to launch the DRDS instance.

`InstanceChargeType` -  (Optional, ForceNew) Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`.

`VswitchId` - (Optional, ForceNew) The VSwitch ID to launch in.

`InstanceSeries` - (Required, ForceNew) User-defined DRDS instance node spec. Value range: - `Drds.sn1.4c8g` for DRDS instance Starter version; - `Drds.sn1.8c16g` for DRDS instance Standard edition; - `Drds.sn1.16c32g` for DRDS instance Enterprise Edition; - `Drds.sn1.32c64g` for DRDS instance Extreme Edition;.

`Specification` - (Required, ForceNew) User-defined DRDS instance specification. Value range: - `Drds.sn1.4c8g` for DRDS instance Starter version; - value range : `Drds.sn1.4c8g.8c16g`, `drds.sn1.4c8g.16c32g`, `drds.sn1.4c8g.32c64g`, `drds.sn1.4c8g.64c128g` - `Drds.sn1.8c16g` for DRDS instance Standard edition; - value range : `Drds.sn1.8c16g.16c32g`, `drds.sn1.8c16g.32c64g`, `drds.sn1.8c16g.64c128g` - `Drds.sn1.16c32g` for DRDS instance Enterprise Edition; - value range : `Drds.sn1.16c32g.32c64g`, `drds.sn1.16c32g.64c128g` - `Drds.sn1.32c64g` for DRDS instance Extreme Edition; - value range : `Drds.sn1.32c64g.128c256g`.


## Return Values

### Fn::GetAtt

`Id` - The DRDS instance ID.

## See Also

* [alicloud_drds_instance](https://www.terraform.io/docs/providers/alicloud/r/drds_instance.html) in the _Terraform Provider Documentation_