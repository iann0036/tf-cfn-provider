# Terraform::HuaweiCloud::DmsInstanceV1

Manages a DMS instance in the huaweicloud DMS Service.

## Properties

`Name` - (Required) Indicates the name of an instance. An instance name starts with a letter, consists of 4 to 64 characters, and supports only letters, digits, and hyphens (-).

`Description` - (Optional) Indicates the description of an instance. It is a character string containing not more than 1024 characters.

`Engine` - (Optional) Indicates a message engine. Options: rabbitmq and kafka.

`EngineVersion` - (Optional) Indicates the version of a message engine.

`Specification` - (Optional) This parameter is mandatory if the engine is kafka. Indicates the baseline bandwidth of a Kafka instance, that is, the maximum amount of data transferred per unit time. Unit: byte/s. Options: 300 MB, 600 MB, 1200 MB.

`StorageSpace` - (Required) Indicates the message storage space. Value range: Single-node RabbitMQ instance: 100–90000 GB Cluster RabbitMQ instance: 100 GB x Number of nodes to 90000 GB, 200 GB x Number of nodes to 90000 GB, 300 GB x Number of nodes to 90000 GB Kafka instance with specification being 300 MB: 1200–90000 GB Kafka instance with specification being 600 MB: 2400–90000 GB Kafka instance with specification being 1200 MB: 4800–90000 GB.

`PartitionNum` - (Optional) This parameter is mandatory when a Kafka instance is created. Indicates the maximum number of topics in a Kafka instance. When specification is 300 MB: 900 When specification is 600 MB: 1800 When specification is 1200 MB: 1800.

`AccessUser` - (Optional) Indicates a username. If the engine is rabbitmq, this parameter is mandatory. If the engine is kafka, this parameter is optional. A username consists of 4 to 64 characters and supports only letters, digits, and hyphens (-).

`Password` - (Optional) If the engine is rabbitmq, this parameter is mandatory. If the engine is kafka, this parameter is mandatory when ssl_enable is true and is invalid when ssl_enable is false. Indicates the password of an instance. An instance password must meet the following complexity requirements: Must be 8 to 32 characters long. Must contain at least 2 of the following character types: lowercase letters, uppercase letters, digits, and special characters (`~!@#$%^&*()-_=+\|[{}]:'",<.>/?).

`VpcId` - (Required) Indicates the ID of a VPC.

`SecurityGroupId` - (Required) Indicates the ID of a security group.

`SubnetId` - (Required) Indicates the ID of a subnet.

`AvailableZones` - (Required) Indicates the ID of an AZ. The parameter value can not be left blank or an empty array. For details, see section Querying AZ Information.

`ProductId` - (Required) Indicates a product ID.

`MaintainBegin` - (Optional) Indicates the time at which a maintenance time window starts. Format: HH:mm:ss. The start time and end time of a maintenance time window must indicate the time segment of a supported maintenance time window. For details, see section Querying Maintenance Time Windows. The start time must be set to 22:00, 02:00, 06:00, 10:00, 14:00, or 18:00. Parameters maintain_begin and maintain_end must be set in pairs. If parameter maintain_begin is left blank, parameter maintain_end is also blank. In this case, the system automatically allocates the default start time 02:00.

`MaintainEnd` - (Optional) Indicates the time at which a maintenance time window ends. Format: HH:mm:ss. The start time and end time of a maintenance time window must indicate the time segment of a supported maintenance time window. For details, see section Querying Maintenance Time Windows. The end time is four hours later than the start time. For example, if the start time is 22:00, the end time is 02:00. Parameters maintain_begin and maintain_end must be set in pairs. If parameter maintain_end is left blank, parameter maintain_begin is also blank. In this case, the system automatically allocates the default end time 06:00.

`EnablePublicip` - (Optional) Indicates whether to enable public access to a RabbitMQ instance. true: enable, false: disable.

`PublicipId` - (Optional) Indicates the ID of the elastic IP address (EIP) bound to a RabbitMQ instance. This parameter is mandatory if public access is enabled (that is, enable_publicip is set to true).

`StorageSpecCode` - (Optional) Indicates the storage I/O specification. For details on how to select a disk type, see Disk Types and Disk Performance. Options for a RabbitMQ instance: dms.physical.storage.normal dms.physical.storage.high dms.physical.storage.ultra Options for a Kafka instance: When specification is 300 MB: dms.physical.storage.high or dms.physical.storage.ultra When specification is 600 MB: dms.physical.storage.ultra When specification is 1200 MB: dms.physical.storage.ultra.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`Description` - See Properties above.

`Engine` - See Properties above.

`EngineVersion` - See Properties above.

`Specification` - See Properties above.

`StorageSpace` - Indicates the time when a instance is created.

`PartitionNum` - See Properties above.

`AccessUser` - See Properties above.

`Password` - See Properties above.

`VpcId` - See Properties above.

`SecurityGroupId` - See Properties above.

`SecurityGroupName` - Indicates the name of a security group.

`SubnetId` - See Properties above.

`SubnetName` - Indicates the name of a subnet.

`SubnetCidr` - Indicates a subnet segment.

`AvailableZones` - See Properties above.

`ProductId` - See Properties above.

`MaintainBegin` - See Properties above.

`MaintainEnd` - See Properties above.

`EnablePublicip` - See Properties above.

`PublicipId` - See Properties above.

`StorageSpecCode` - See Properties above.

`UsedStorageSpace` - Indicates the used message storage space. Unit: GB.

`ConnectAddress` - Indicates the IP address of an instance.

`Port` - Indicates the port number of an instance.

`Status` - Indicates the status of an instance. For details, see section Instance Status.

`InstanceId` - Indicates the ID of an instance.

`ResourceSpecCode` - Indicates a resource specifications identifier.

`Type` - Indicates an instance type. Options: "single" and "cluster".

`CreatedAt` - Indicates the time when an instance is created. The time is in the format.

`UserId` - Indicates a user ID.

## See Also

* [huaweicloud_dms_instance_v1](https://www.terraform.io/docs/providers/huaweicloud/r/dms_instance_v1.html) in the _Terraform Provider Documentation_