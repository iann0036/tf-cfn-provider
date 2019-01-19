# Terraform::FlexibleEngine::DwsClusterV1

Manages a DWS cluster resource within FlexibleEngine

## Properties

`AvailabilityZone` - (Optional) AZ in a cluster.

`Name` - (Required) Cluster name, which must be unique and contains 4 to 64 characters, which consist of letters, digits, hyphens (-), or underscores (_) only and must start with a letter.

`NodeType` - (Required) Node type.

`NumberOfNode` - (Required) Number of nodes in a cluster. The value ranges from 3 to 32.

`Port` - (Optional) Service port of a cluster (8000 to 10000). The default value is 8000.

`PublicIp` - (Optional) Public IP address. If the value is not specified, public connection is not used by default.

`SecurityGroupId` - (Required) ID of a security group. The ID is used for configuring cluster network.

`SubnetId` - (Required) Subnet ID, which is used for configuring cluster network.

`UserName` - (Required) Administrator username for logging in to a data warehouse cluster The administrator username must:.

`UserPwd` - (Required) Administrator password for logging in to a data warehouse cluster.

`VpcId` - (Required) VPC ID, which is used for configuring cluster network.

### PublicIp Properties

`EipId` - (Optional) EIP ID.

`PublicBindType` - (Optional) Binding type of an EIP. The value can be either of the following:.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`NumberOfNode` - See Properties above.

`AvailabilityZone` - See Properties above.

`SubnetId` - See Properties above.

`UserName` - See Properties above.

`SecurityGroupId` - See Properties above.

`PublicIp` - See Properties above.

`NodeType` - See Properties above.

`VpcId` - See Properties above.

`Port` - See Properties above.

`Created` - Cluster creation time. The format is.

`Endpoints` - View the private network connection information about the.

`Id` - Cluster ID.

`PublicEndpoints` - Public network connection information about the cluster.

`Status` - Cluster status, which can be one of the following:.

`SubStatus` - Sub-status of clusters in the AVAILABLE state. The value can.

`TaskStatus` - Cluster management task. The value can be one of the.

`Updated` - Last modification time of a cluster. The format is.

`Version` - Data warehouse version.

`ConnectInfo` - Private network connection information.

`JdbcUrl` - JDBC URL. The following is the default format:.

`PublicConnectInfo` - Public network connection information.

## See Also

* [flexibleengine_dws_cluster_v1](https://www.terraform.io/docs/providers/flexibleengine/r/dws_cluster_v1.html) in the _Terraform Provider Documentation_