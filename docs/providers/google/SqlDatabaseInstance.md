# Terraform::Google::SqlDatabaseInstance

Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

~> **NOTE on `Terraform::Google::SqlDatabaseInstance`:** - Second-generation instances include a
default 'root'@'%' user with no password. This user will be deleted by Terraform on
instance creation. You should use `Terraform::Google::SqlUser` to define a custom user with
a restricted host and strong password.

## Properties

`Region` - (Required) The region the instance will sit in. Note, first-generation Cloud SQL instance regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations). A valid region must be provided to use this resource. If a region is not provided in the resource definition, the provider region will be used instead, but this will be an apply-time error for all first-generation instances *and* for second-generation instances if the provider region is not supported with Cloud SQL. If you choose not to provide the `Region` argument for this resource, make sure you understand this.

`Settings` - (Required) The settings to use for the database. The configuration is detailed below.

`DatabaseVersion` - (Optional, Default: `MYSQL_5_6`) The MySQL version to use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances. See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences) for more information. `POSTGRES_9_6` support is in beta.

`Name` - (Optional, Computed) The name of the instance. If the name is left blank, Terraform will randomly generate one when the instance is first created. This is done because after a name is used, it cannot be reused for up to [one week](https://cloud.google.com/sql/docs/delete-instance).

`MasterInstanceName` - (Optional) The name of the instance that will act as the master in the replication setup. Note, this requires the master to have `BinaryLogEnabled` set, as well as existing backups.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`ReplicaConfiguration` - (Optional) The configuration for replication. The configuration is detailed below.

### Settings Properties

`Tier` - (Required) The machine tier (First Generation) or type (Second Generation) to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers) for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`, and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.

`ActivationPolicy` - (Optional) This specifies when the instance should be active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.

`AuthorizedGaeApplications` - (Optional) A list of Google App Engine (GAE) project names that are allowed to access this instance.

`AvailabilityType` - (Optional) This specifies whether a PostgreSQL instance should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).

`CrashSafeReplication` - (Optional) Specific to read instances, indicates when crash-safe replication flags are enabled.

`DiskAutoresize` - (Optional, Second Generation, Default: `true`) Configuration to increase storage size automatically.

`DiskSize` - (Optional, Second Generation, Default: `10`) The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.

`DiskType` - (Optional, Second Generation, Default: `PD_SSD`) The type of data disk: PD_SSD or PD_HDD.

`PricingPlan` - (Optional, First Generation) Pricing plan for this instance, can be one of `PER_USE` or `PACKAGE`.

`ReplicationType` - (Optional) Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.

`UserLabels` - (Optional) A set of key/value user label pairs to assign to the instance.

`Name` - (Optional) Name of the flag.

`Value` - (Optional) Value of the flag.

`BinaryLogEnabled` - (Optional) True if binary logging is enabled. If `logging` is false, this must be as well. Cannot be used with Postgres.

`Enabled` - (Optional) True if backup configuration is enabled.

`StartTime` - (Optional) `HH:MM` format time indicating when backup configuration starts.

`Ipv4Enabled` - (Optional) True if the instance should be assigned an IP address. The IPv4 address cannot be disabled for Second Generation instances.

`RequireSsl` - (Optional) True if mysqld should default to `REQUIRE X509` for users connecting over IP.

`PrivateNetwork` - (Optional) The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP.

`ExpirationTime` - (Optional) The [RFC 3339](https://tools.ietf.org/html/rfc3339) formatted date time string indicating when this whitelist expires.

`Name` - (Optional) A name for this whitelist entry.

`Value` - (Optional) A CIDR notation IPv4 or IPv6 address that is allowed to access this instance. Must be set even if other two attributes are not for the whitelist to become active.

`FollowGaeApplication` - (Optional) A GAE application whose zone to remain in. Must be in the same region as this instance.

`Zone` - (Optional) The preferred compute engine [zone](https://cloud.google.com/compute/docs/zones?hl=en).

`Day` - (Optional) Day of week (`1-7`), starting on Monday.

`Hour` - (Optional) Hour of day (`0-23`), ignored if `Day` not set.

`UpdateTrack` - (Optional) Receive updates earlier (`canary`) or later (`stable`).

`CaCertificate` - (Optional) PEM representation of the trusted CA's x509 certificate.

`ClientCertificate` - (Optional) PEM representation of the slave's x509 certificate.

`ClientKey` - (Optional) PEM representation of the slave's private key. The corresponding public key in encoded in the `ClientCertificate`.

`ConnectRetryInterval` - (Optional, Default: 60) The number of seconds between connect retries.

`DumpFilePath` - (Optional) Path to a SQL file in GCS from which slave instances are created. Format is `gs://bucket/filename`.

`FailoverTarget` - (Optional) Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica. If the master instance fails, the replica instance will be promoted as the new master instance.

`MasterHeartbeatPeriod` - (Optional) Time in ms between replication heartbeats.

`Password` - (Optional) Password for the replication connection.

`SslCipher` - (Optional) Permissible ciphers for use in SSL encryption.

`Username` - (Optional) Username for replication connection.

`VerifyServerCertificate` - (Optional) True if the master's common name value is checked during the SSL handshake.


## Return Values

### Fn::GetAtt

`FirstIpAddress` - The first IPv4 address of the addresses assigned. This is.

`ConnectionName` - The connection name of the instance to be used in connection strings.

`IpAddress.0.ipAddress` - The IPv4 address assigned.

`IpAddress.0.timeToRetire` - The time this IP address will be retired, in RFC.

`IpAddress.0.type` - The type of this IP address. A PRIMARY address is an address that can accept incoming connections. An OUTGOING address is the source address of connections originating from the instance, if supported. A PRIVATE address is an address for an instance which has been configured to use private networking see: [Private IP](https://cloud.google.com/sql/docs/mysql/private-ip).

`SelfLink` - The URI of the created resource.

`Settings.version` - Used to make sure changes to the `Settings` block are.

`ServerCaCert.0.cert` - The CA Certificate used to connect to the SQL Instance via SSL.

`ServerCaCert.0.commonName` - The CN valid for the CA Cert.

`ServerCaCert.0.createTime` - Creation time of the CA Cert.

`ServerCaCert.0.expirationTime` - Expiration time of the CA Cert.

`ServerCaCert.0.sha1Fingerprint` - SHA Fingerprint of the CA Cert.

`ServiceAccountEmailAddress` - The service account email address assigned to the.

## See Also

* [google_sql_database_instance](https://www.terraform.io/docs/providers/google/r/sql_database_instance.html) in the _Terraform Provider Documentation_