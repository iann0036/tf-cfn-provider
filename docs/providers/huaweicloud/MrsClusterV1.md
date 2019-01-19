# Terraform::HuaweiCloud::MrsClusterV1

Manages resource cluster within HuaweiCloud MRS.

## Properties

`BillingType` - (Required) The value is 12, indicating on-demand payment.

`Region` - (Required) Cluster region information. Obtain the value from Regions and Endpoints.

`MasterNodeNum` - (Required) Number of Master nodes The value is 2.

`MasterNodeSize` - (Required) Best match based on several years of commissioning experience. MRS supports specifications of hosts, and host specifications are determined by CPUs, memory, and disks space. MRS supports instance specifications detailed in [MRS specifications](https://support.huaweicloud.com/en-us/api-mrs/mrs_01_9006.html).

`CoreNodeNum` - (Required) Number of Core nodes Value range: 3 to 100 A maximum of 100 Core nodes are supported by default. If more than 100 Core nodes are required, contact technical support engineers or invoke background APIs to modify the database.

`CoreNodeSize` - (Required) Instance specification of a Core node Configuration method of this parameter is identical to that of master_node_size.

`AvailableZoneId` - (Required) ID of an available zone. Obtain the value from Regions and Endpoints. North China AZ1 (cn-north-1a): ae04cf9d61544df3806a3feeb401b204, North China AZ2 (cn-north-1b): d573142f24894ef3bd3664de068b44b0, East China AZ1 (cn-east-2a): 72d50cedc49846b9b42c21495f38d81c, East China AZ2 (cn-east-2b): 38b0f7a602344246bcb0da47b5d548e7, East China AZ3 (cn-east-2c): 5547fd6bf8f84bb5a7f9db062ad3d015, South China AZ1(cn-south-1a): 34f5ff4865cf4ed6b270f15382ebdec5, South China AZ2(cn-south-2b): 043c7e39ecb347a08dc8fcb6c35a274e, South China AZ3(cn-south-1c): af1687643e8c4ec1b34b688e4e3b8901,.

`ClusterName` - (Required) Cluster name, which is globally unique and contains only 1 to 64 letters, digits, hyphens (-), and underscores (_).

`VpcId` - (Required) ID of the VPC where the subnet locates Obtain the VPC ID from the management console as follows: Register an account and log in to the management console. Click Virtual Private Cloud and select Virtual Private Cloud from the left list. On the Virtual Private Cloud page, obtain the VPC ID from the list.

`SubnetId` - (Required) Subnet ID Obtain the subnet ID from the management console as follows: Register an account and log in to the management console. Click Virtual Private Cloud and select Virtual Private Cloud from the left list. On the Virtual Private Cloud page, obtain the subnet ID from the list.

`ClusterVersion` - (Optional) Version of the clusters Currently, MRS 1.6.3, MRS 1.7.2 and MRS 1.8.1 are supported. The latest version of MRS is used by default. Currently, the latest version is MRS 1.8.1.

`ClusterType` - (Optional) Type of clusters 0: analysis cluster 1: streaming cluster The default value is 0.

`VolumeType` - (Required) Type of disks SATA and SSD are supported. SATA: common I/O SSD: super high-speed I/O.

`VolumeSize` - (Required) Data disk storage space of a Core node Users can add disks to expand storage capacity when creating a cluster. There are the following scenarios: Separation of data storage and computing: Data is stored in the OBS system. Costs of clusters are relatively low but computing performance is poor. The clusters can be deleted at any time. It is recommended when data computing is not frequently performed. Integration of data storage and computing: Data is stored in the HDFS system. Costs of clusters are relatively high but computing performance is good. The clusters cannot be deleted in a short term. It is recommended when data computing is frequently performed. Value range: 100 GB to 32000 GB.

`NodePublicCertName` - (Required) Name of a key pair You can use a key to log in to the Master node in the cluster.

`SafeMode` - (Required) MRS cluster running mode 0: common mode The value indicates that the Kerberos authentication is disabled. Users can use all functions provided by the cluster. 1: safe mode The value indicates that the Kerberos authentication is enabled. Common users cannot use the file management or job management functions of an MRS cluster and cannot view cluster resource usage or the job records of Hadoop and Spark. To use these functions, the users must obtain the relevant permissions from the MRS Manager administrator. The request has the cluster_admin_secret parameter only when safe_mode is set to 1.

`ClusterAdminSecret` - (Optional) Indicates the password of the MRS Manager administrator. The password for MRS 1.5.0: Must contain 6 to 32 characters. Must contain at least two types of the following: Lowercase letters Uppercase letters Digits Special characters of `~!@#$%^&*()-_=+\|[{}];:'",<.>/? Spaces Must be different from the username. Must be different from the username written in reverse order. The password for MRS 1.3.0: Must contain 8 to 64 characters. Must contain at least four types of the following: Lowercase letters Uppercase letters Digits Special characters of `~!@#$%^&*()-_=+\|[{}];:'",<.>/? Spaces Must be different from the username. Must be different from the username written in reverse order. This parameter needs to be configured only when safe_mode is set to 1.

`LogCollection` - (Optional) Indicates whether logs are collected when cluster installation fails. 0: not collected 1: collected The default value is 0. If log_collection is set to 1, OBS buckets will be created to collect the MRS logs. These buckets will be charged.

`ComponentList` - (Required) Service component list.

`AddJobs` - (Optional) You can submit a job when you create a cluster to save time and use MRS easily. Only one job can be added.

`ComponentName` - (Required) Component name Currently, Hadoop, Spark, HBase, Hive, Hue, Loader, Flume, Kafka and Storm are supported.

`JobType` - (Required) Job type 1: MapReduce 2: Spark 3: Hive Script 4: HiveQL (not supported currently) 5: DistCp, importing and exporting data (not supported in this API currently). 6: Spark Script 7: Spark SQL, submitting Spark SQL statements (not supported in this API currently). NOTE: Spark and Hive jobs can be added to only clusters including Spark and Hive components.

`JobName` - (Required) Job name It contains only 1 to 64 letters, digits, hyphens (-), and underscores (_). NOTE: Identical job names are allowed but not recommended.

`JarPath` - (Required) Path of the .jar file or .sql file for program execution The parameter must meet the following requirements: Contains a maximum of 1023 characters, excluding special characters such as ;|&><'$. The address cannot be empty or full of spaces. Starts with / or s3a://. Spark Script must end with .sql; while MapReduce and Spark Jar must end with .jar. sql and jar are case-insensitive.

`Arguments` - (Optional) Key parameter for program execution The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter. The parameter contains a maximum of 2047 characters, excluding special characters such as ;|&>'<$, and can be empty.

`Input` - (Optional) Path for inputting data, which must start with / or s3a://. A correct OBS path is required. The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&>'<$, and can be empty.

`Output` - (Optional) Path for outputting data, which must start with / or s3a://. A correct OBS path is required. If the path does not exist, the system automatically creates it. The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&>'<$, and can be empty.

`JobLog` - (Optional) Path for storing job logs that record job running status. This path must start with / or s3a://. A correct OBS path is required. The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&>'<$, and can be empty.

`ShutdownCluster` - (Optional) Whether to delete the cluster after the jobs are complete true: Yes false: No.

`FileAction` - (Optional) Data import and export import export.

`SubmitJobOnceClusterRun` - (Required) true: A job is submitted when a cluster is created. false: A job is submitted separately. The parameter is set to true in this example.

`Hql` - (Optional) HiveQL statement.

`HiveScriptPath` - (Optional) SQL program path This parameter is needed by Spark Script and Hive Script jobs only and must meet the following requirements: Contains a maximum of 1023 characters, excluding special characters such as ;|&><'$. The address cannot be empty or full of spaces. Starts with / or s3a://. Ends with .sql. sql is case-insensitive.


## Return Values

### Fn::GetAtt

`BillingType` - See Properties above.

`DataCenter` - See Properties above.

`MasterNodeNum` - See Properties above.

`MasterNodeSize` - See Properties above.

`CoreNodeNum` - See Properties above.

`CoreNodeSize` - See Properties above.

`AvailableZoneId` - See Properties above.

`ClusterName` - See Properties above.

`VpcId` - See Properties above.

`SubnetId` - See Properties above.

`ClusterVersion` - See Properties above.

`ClusterType` - See Properties above.

`VolumeType` - See Properties above.

`VolumeSize` - See Properties above.

`NodePublicCertName` - See Properties above.

`SafeMode` - See Properties above.

`ClusterAdminSecret` - See Properties above.

`LogCollection` - See Properties above.

`ComponentList` - See Properties below.

`AddJobs` - See Properties above.

`OrderId` - Order ID for creating clusters.

`ClusterId` - Cluster ID.

`AvailableZoneName` - Name of an availability zone.

`InstanceId` - Instance ID.

`HadoopVersion` - Hadoop version.

`MasterNodeIp` - IP address of a Master node.

`ExternalIp` - Internal IP address.

`PrivateIpFirst` - Primary private IP address.

`ExternalIp` - External IP address.

`SlaveSecurityGroupsId` - Standby security group ID.

`SecurityGroupsId` - Security group ID.

`ExternalAlternateIp` - Backup external IP address.

`MasterNodeSpecId` - Specification ID of a Master node.

`CoreNodeSpecId` - Specification ID of a Core node.

`MasterNodeProductId` - Product ID of a Master node.

`CoreNodeProductId` - Product ID of a Core node.

`Duration` - Cluster subscription duration.

`Vnc` - URI address for remote login of the elastic cloud server.

`Fee` - Cluster creation fee, which is automatically calculated.

`DeploymentId` - Deployment ID of a cluster.

`ClusterState` - Cluster status Valid values include: existing history starting.

`TenantId` - Project ID.

`CreateAt` - Cluster creation time.

`UpdateAt` - Cluster update time.

`ErrorInfo` - Error information.

`ChargingStartTime` - Time when charging starts.

`Remark` - Remarks of a cluster.

`ComponentName` - (Required) Component name Currently, Hadoop, Spark, HBase,.

## See Also

* [huaweicloud_mrs_cluster_v1](https://www.terraform.io/docs/providers/huaweicloud/r/mrs_cluster_v1.html) in the _Terraform Provider Documentation_