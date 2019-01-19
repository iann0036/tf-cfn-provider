# Terraform::Google::SqlDatabaseInstance

Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

~> **NOTE on `google_sql_database_instance`:** - Second-generation instances include a
default 'root'@'%' user with no password. This user will be deleted by Terraform on
instance creation. You should use `google_sql_user` to define a custom user with
a restricted host and strong password.

## Properties

TBC

## Return Values

### Fn::GetAtt

`FirstIpAddress` - The first IPv4 address of the addresses assigned. This is.

`ConnectionName` - The connection name of the instance to be used in connection strings.

`IpAddress.0.ipAddress` - The IPv4 address assigned.

`IpAddress.0.timeToRetire` - The time this IP address will be retired, in RFC.

`IpAddress.0.type` - The type of this IP address. A PRIMARY address is an address that can accept incoming connections. An OUTGOING address is the source address of connections originating from the instance, if supported. A PRIVATE address is an address for an instance which has been configured to use private networking see: [Private IP](https://cloud.google.com/sql/docs/mysql/private-ip).

`SelfLink` - The URI of the created resource.

`Settings.version` - Used to make sure changes to the `settings` block are.

`ServerCaCert.0.cert` - The CA Certificate used to connect to the SQL Instance via SSL.

`ServerCaCert.0.commonName` - The CN valid for the CA Cert.

`ServerCaCert.0.createTime` - Creation time of the CA Cert.

`ServerCaCert.0.expirationTime` - Expiration time of the CA Cert.

`ServerCaCert.0.sha1Fingerprint` - SHA Fingerprint of the CA Cert.

`ServiceAccountEmailAddress` - The service account email address assigned to the.

## See Also

* [google_sql_database_instance](https://www.terraform.io/docs/providers/google/r/sql_database_instance.html) in the _Terraform Provider Documentation_