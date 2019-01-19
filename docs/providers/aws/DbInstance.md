# Terraform::AWS::DbInstance

Provides an RDS instance resource.  A DB instance is an isolated database
environment in the cloud.  A DB instance can contain multiple user-created
databases.

Changes to a DB instance can occur when you manually change a parameter, such as
`allocated_storage`, and are reflected in the next maintenance window. Because
of this, Terraform may report a difference in its planning phase because a
modification has not yet taken place. You can use the `apply_immediately` flag
to instruct the service to apply the change immediately (see documentation
below).

When upgrading the major version of an engine, `allow_major_version_upgrade`
must be set to `true`.

~> **Note:** using `apply_immediately` can result in a brief downtime as the
server reboots. See the AWS Docs on [RDS Maintenance][2] for more information.

~> **Note:** All arguments including the username and password will be stored in
the raw state as plain-text. [Read more about sensitive data in
state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Address` - The hostname of the RDS instance. See also `endpoint` and `port`.

`Arn` - The ARN of the RDS instance.

`AllocatedStorage` - The amount of allocated storage.

`AvailabilityZone` - The availability zone of the instance.

`BackupRetentionPeriod` - The backup retention period.

`BackupWindow` - The backup window.

`CaCertIdentifier` - Specifies the identifier of the CA certificate for the.

`Domain` - The ID of the Directory Service Active Directory domain the instance is joined to.

`DomainIamRoleName` - The name of the IAM role to be used when making API calls to the Directory Service.

`Endpoint` - The connection endpoint in `address:port` format.

`Engine` - The database engine.

`EngineVersion` - The database engine version.

`HostedZoneId` - The canonical hosted zone ID of the DB instance (to be used.

`Id` - The RDS instance ID.

`InstanceClass` - The RDS instance class.

`MaintenanceWindow` - The instance maintenance window.

`MultiAz` - If the RDS instance is multi AZ enabled.

`Name` - The database name.

`Port` - The database port.

`ResourceId` - The RDS Resource ID of this instance.

`Status` - The RDS instance status.

`StorageEncrypted` - Specifies whether the DB instance is encrypted.

`Username` - The master username for the database.

`CharacterSetName` - The character set used on Oracle instances.

## See Also

* [aws_db_instance](https://www.terraform.io/docs/providers/aws/r/db_instance.html) in the _Terraform Provider Documentation_