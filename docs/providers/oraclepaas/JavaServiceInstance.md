# Terraform::OraclePaaS::JavaServiceInstance

The `Terraform::OraclePaaS::JavaServiceInstance` resource creates and manages an Oracle Java Cloud Service instance on the Oracle Cloud Platform.

## Properties

`Name` - (Required) The name of the Service Instance.

`SshPublicKey` - (Required) The ssh key to connect to the java service instance.

`Edition` - (Required) The edition for the service instance. Possible values are `SE`, `EE`, or `SUITE`.

`ServiceVersion` - (Required) Oracle WebLogic Server software version. Valid values are: `12cRelease213`, `12cRelease212`, `12cR3`, or `11gR1`.

`Backups` - (Required) Provides Cloud Storage information for service instance backups. Backups is documented below.

`MeteringFrequency` - (Optional) Billing unit. Possible values are `HOURLY` or `MONTHLY`. Default value is `HOURLY`.

`AvailabilityDomain` - (Optional) Name of a data center location in the Oracle Cloud Infrastructure region that is specified in region. This is only available for OCI.

`SnapshotName` - (Optional) Name of the snapshot to clone from.

`SourceServiceName` - (Optional) Name of the existing Oracle Java Cloud Service instance that has the snapshot from which you are creating a clone.

`Subnet` - (Optional) A subdivision of a cloud network that is set up in the data center as specified in `AvailabilityDomain`. This is only available for OCI.

`UseIdentityService` - (Optional) Flag that specifies whether to use Oracle Identity Cloud Service (true) or the local WebLogic identity store (false) for user authentication and to maintain administrators, application users, groups and roles. The default value is false.

`WeblogicServer` - (Required) The attributes required to create a WebLogic server alongside the java service instance. WebLogic Server is documented below.

`OracleTrafficDirector` - (Optional) The attributes required to create an Oracle Traffic Director (Load balancer). OTD is documented below.

`Level` - (Optional) Service level for the service instance. Possible values are `BASIC` or `PAAS`. Default value is `PAAS`.

`BackupDestination` - (Optional) Specifies whether to enable backups for this Oracle Java Cloud Service instance. Valid values are `BOTH` or `NONE`. Defaults to `BOTH`.

`DesiredState` - (Optional) Specifies the desired state of the service instance. Allowed values are `running` or `shutdown`. The default is `running`.

`Description` - (Optional) Provides additional on the java service instance.

`EnableAdminConsole` - (Optional) Flag that specifies whether to enable (true) or disable (false) the access rules that control external communication to the WebLogic Server Administration Console, Fusion Middleware Control, and Load Balancer Console.

`IpNetwork` - (Optional) The three-part name of a custom IP network to attach this service instance to. For example: `/Compute-identity_domain/user/object`.

`AssignPublicIp` - (Optional) Flag that specifies whether to assign (true) or not assign (false) public IP addresses to the nodes in your service instance. The default is `true`, which means any node added during service instance provisioning, or later added as part of a scaling operation, will have a public IP address assigned to it. This attribute is only applicable when provisioning an Oracle Java Cloud Service instance in a region on Oracle Cloud Infrastructure Classic, and a custom IP network is specified in `IpNetwork`.

`Region` - (Optional) Name of the region where the Oracle Java Cloud Service instance is to be provisioned. This attribute is only applicable to accounts where regions are supported. A region name must be specified if you want to use ipReservations or ipNetwork.

`BringYourOwnLicense` - (Optional) Flag that specifies whether to apply an existing on-premises license for Oracle WebLogic Server (true) to the new Oracle Java Cloud Service instance you are provisioning. The default value is `false`.

`ForceDelete` - (Optional) Flag that specifies whether you want to force the removal of the service instance even if the database instance cannot be reached to delete the database schemas. Default value is `true`.

`CloudStorageContainer` - (Required) Name of the Oracle Storage Cloud Service container used to provide storage for your service instance backups. Use the following format to specify the container name on OCI Object Storage `https://swiftobjectstorage.<region>.oraclecloud.com/v1/<tenancy>/<bucketname>` or for Oracle Cloud Infrastructure Classic user the format: `<storageservicename>-<storageidentitydomain>/<containername>`.

`CloudStorageUsername` - (Optional) Username for the Oracle Storage Cloud Service administrator. If left unspecified, the username for Oracle Public Cloud is used.

`CloudStoragePassword` - (Optional) Password for the Oracle Storage Cloud Service administrator. If left unspecified, the password for Oracle Public Cloud is used.

`CreateIfMissing` - (Optional) Specify if the given cloud_storage_container is to be created if it does not already exist. Default value is `false`.

`UseOauthForStorage` - (Optional)  Flag that specifies whether to use the default OAuth protected object storage for instance backups.

`Database` - (Required) Information about the database deployment on Oracle Database Cloud Service. Database is documented below.

`Shape` - (Required) Desired compute shape.

`Admin` - (Required) Admin information for the WebLogic Server. Admin is documented below.

`ApplicationDatabase` - (Optional) Details of Database Cloud Service database deployments that host application schemas. Multiple can be specified. Application Database is specified below.

`BackupVolumeSize` - (Optional) Size of the backup volume for the service. The value must be a multiple of GBs. You can specify this value in bytes or GBs. If specified in GBs, use the following format: nG, where n specifies the number of GBs. For example, you can express 10 GBs as bytes or GBs. For example: 100000000000 or 10G. This value defaults to the system configured volume size.

`ClusterName` - (Optional) - Specifies the name of the cluster that contains the Managed Servers for the service instance.

`Cluster` - (Optional) Details the properties about one or more clusters. Cluster is documented below.

`ConnectString` - (Optional) - Connection string for the database. The connection string must be entered using one of the following formats: host:port:SID, host:port/serviceName.

`ContentPort` - (Optional) - Port for accessing the deployed applications using HTTP. Default value is 8001.

`DeploymentChannelPort` - Port for accessing the Administration Server using WLST. Default value is 9001.

`Domain` - (Optional) Information about the WebLogic domain. Domain is documented below.

`IpReservations` - (Optional) A list of ip reservation names.

`LoadBalancer` - (Optional) Information about the loadbalancer to attach to the java service instance. Load Balancer is specfied below.

`ManagedServers` - (Optional) Details information about the managed servers the java service instance will look after. Managed Servers is documented below.

`MiddlewareVolumeSize` - (Optional) Size of the middleware home disk volume for the service (/u01/app/oracle/middleware). The value must be a multiple of GBs. You can specify this value in bytes or GBs. If specified in GBs, use the following format: nG, where n specifies the number of GBs. For example, you can express 10 GBs as bytes or GBs. For example: 100000000000 or 10G. This value defaults to the system configured volume size.

`NodeManager` - (Optional) Node Manager is a WebLogic Server utility that enables you to start, shut down, and restart Administration Server and Managed Server instances from a remote location. Node Manager is documented below.

`PdbServiceName` - (Optional) Name of the pluggable database for Oracle Database 12c. The default value is the pluggable database name when the database was created.

`Ports` - (Optional) A block of port specifications. Weblogic Server Ports are specified below.

`UpperStackProductName` - (Optional) The Oracle Fusion Middleware product installer to add to this Oracle Java Cloud Service instance. Valid values are `ODI` (Oracle Data Integrator) or `WCP` (Oracle WebCenter Portal).

`RootUrl` - (Computed) The URL of the WebLogic Server Administration console.

`Admin` - (Required) Admin information for the Oracle Traffic Director. Admin is documented below.

`Shape` - (Required) Desired compute shape.

`HighAvailability` - (Optional) Flag that specifies whether load balancer HA is enabled. This value defaults to false (that is, HA is not enabled).

`IpReservations` - (Optional) A list of ip reservation names.

`Listener` - (Optional) Specifies the type and number of the listener port. Listener is documented below.

`LoadBalancingPolicy` - (Optional) Policy to use for routing requests to the load balancer. Valid policies include: `least_connection_count`, `least_response_time`, `round_robin`. The default value is `least_connection_count`.

`RootUrl` - (Computed) The URL of the OTD console.

`Username` - (Required) Username for the database administrator.

`Password` - (Required) Password for the database administrator.

`Name` - (Required) Name of the database on the Database Cloud Service.

`Hostname` - (Computed) The hostname for the database.

`Username` - (Required) Username for the WebLogic Server or Oracle Traffic Director administrator.

`Password` - (Required) Password for the WebLogic Server or Oracle Traffic Director administrator.

`Port` - (Optional) Port for accessing the WebLogic Server or Oracle Traffic Director using HTTP. The default values are 7001 for WebLogic Server or 8989 for Oracle Traffic Director.

`SecuredPort` - (Optional) Secured Port for accessing the WebLogic Server. The default value is 7002.

`Hostname` - (Computed) The hostname for the admin server on the WebLogic Server or OTD.

`Username` - (Required) Username for the database administrator.

`Password` - (Required) Password for the database administrator.

`Name` - (Required) Name of the database deployment on the Database Cloud Service.

`PdbName` - (Optional) Name of the pluggable database for Oracle Database 12c. If not specified, the pluggable database name configured when the database was created will be used.

`Name` - (Required) Name of the cluster to create.

`Type` - (Required) Type of cluster to create. Valid values are `APPLICATION_CLUSTER` or `CACHING_CLUSTER`.

`ServerCount` - (Optional) Number of servers to create in this cluster. The default value is 1.

`ServersPerNode` - (Optional) Number of JVMs to start on each VM (node). The default value is 1.

`Shape` - (Optional) Desired compute shape for the nodes in this cluster.

`PathPrefixes` - (Optional) A single path prefix or multiple path prefixes separated by commas.

`Mode` - (Optional) Mode of the domain. Valid values are `DEVELOPMENT`  or `PRODUCTION`. Default value is `PRODUCTION`.

`Name` - (Optional) Name of the WebLogic domain. By default, the domain name will be generated from the first eight characters of the Oracle Java Cloud Service instance name (serviceName), using the following format: first8charsOfServiceInstanceName_domain.

`PartitionCount` - (Optional) Number of partitions to enable in the domain for WebLogic Server 12.2.1. Valid values include: 0 (no partitions), 1, 2, and 4.

`VolumeSize` - (Optional) Size of the domain volume for the service. The value must be a multiple of GBs. You can specify this value in bytes or GBs. If specified in GBs, use the following format: nG, where n specifies the number of GBs. For example, you can express 10 GBs as bytes or GBs. For example: 100000000000 or 10G.

`Port` - (Optional) Listener port for the load balancer for accessing deployed applications using HTTP. If left unspecified, applications on this service instance cannot be reached via http.

`SecuredPort` - (Optional) Secured listener port for the load balancer for accessing deployed applications using HTTPS.

`PrivilegedPort` - (Optional) Privileged listener port for accessing the deployed applications using HTTP.

`PrivilegedSecuredPort` - (Optional) Privileged listener port for accessing the deployed applications using HTTPS.

`ServerCount` - (Optional) Number of Managed Servers in the domain. Valid values include: 1, 2, 4, and 8. The default value is 1.

`InitialHeapSize` - (Optional) Initial Java heap size for a Managed Server JVM, specified in megabytes.

`MaxHeapSize` - (Optional) Maximum Java heap size for a Managed Server JVM, specified in megabytes.

`JvmArgs` - (Optional) One or more Managed Server JVM arguments separated by a space.

`InitialPermanentGeneration` - (Optional) Initial Permanent Generation space in Java heap memory.

`MaxPermanentGeneration` - (Optional) Maximum Permanent Generation space in Java heap memory.

`OverwriteJvmArgs` - (Optional) Flag that determines whether the user defined Managed Server JVM arguments specified in msJvmArgs should replace the server start arguments (true), or append the server start arguments (false). Default is false.

`Username` - (Optional) User name for the Node Manager. This value defaults to the WebLogic administrator user name.

`Password` - (Optional) Password for the Node Manager. This value defaults to the WebLogic administrator password.

`Port` - (Optional) Port for the Node Manager. This value defaults to 5556.

`PrivilegedContentPort` - (Optional) Privileged content port for accessing the deployed applications using HTTP. To disable the privileged content port, set the value to 0. The default value is 80.

`PriviligedSecuredContentPort` - (Optional) Privileged content port for accessing the deployed applications using HTTPS. To disable the privileged secured content port, set the value to 0. The default value is 443.

`DeploymentChannelPort` - (Optional) Port for accessing the WebLogic Administration Server using WLST. The default value is 9001.

`ContentPort` - (Optional) Port for accessing the deployed applications using HTTP. The default value is 8001.

`LoadBalancingPolicy` - (Optional) Policy to use for routing requests to the origin servers of the Oracle managed load balancer. Valid values are `LEAST_CONN`, `IP_HASH`, or `ROUND_ROBIN`.

`Subnets` - (Optional) A list of two OCI-managed load balancer ids.

`Status` - The status of the service instance.

`Uri` - The Uniform Resource Identifier for the Service Instance.


## See Also

* [oraclepaas_java_service_instance](https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance.html) in the _Terraform Provider Documentation_