# Terraform::FlexibleEngine::MlsInstanceV1

Manages mls instance resource within FlexibleEngine

## Properties

`Region` - (Optional) The region in which to create the MLS instance. If omitted, the `Region` argument of the provider is used. Changing this creates a new instance.

`Name` - (Required) Specifies the MLS instance name. The DB instance name of the same type is unique in the same tenant. Changing this creates a new instance.

`Version` - (Required) Specifies MLS Software version, only `1.2.0` is supported now. Changing this creates a new instance.

`Network` - (Required) Specifies the instance network information. The structure is described below. Changing this creates a new instance.

`Agency` - (Optional) Specifies the agency name. This parameter is mandatory only when you bind an instance to an elastic IP address (EIP). An instance must be bound to an EIP to grant MLS rights to abtain a tenant's token. NOTE: The tenant must create an agency on the Identity and Access Management (IAM) interface in advance. Changing this creates a new instance.

`Flavor` - (Required) Specifies the instance flavor, only `mls.c2.2xlarge.common` is supported now. Changing this creates a new instance.

`MrsCluster` - (Required) Specifies the MRS cluster information which the instance is associated. The structure is described below. NOTE: The current MRS instance requires an MRS cluster whose version is 1.3.0 and that is configured with the Spark component. MRS clusters whose version is not 1.3.0 or that are not configured with the Spark component cannot be selected. Changing this creates a new instance.

`VpcId` - (Required) Specifies the ID of the virtual private cloud (VPC) where the instance resides. Changing this creates a new instance.

`SubnetId` - (Required) Specifies the ID of the subnet where the instance resides. Changing this creates a new instance.

`SecurityGroup` - (Optional) Specifies the ID of the security group of the instance. Changing this creates a new instance.

`AvailableZone` - (Required) Specifies the AZ of the instance. Changing this creates a new instance.

`PublicIp` - (Required) Specifies the IP address of the instance. The structure is described below. Changing this creates a new instance.

`BindType` - (Required) Specifies the bind type. Possible values: `auto_assign` and `not_use`. Changing this creates a new instance.

`Id` - (Required) Specifies the ID of the MRS cluster. Changing this creates a new instance.

`UserName` - (Optional) Specifies the MRS cluster username. This parameter is mandatory only when the MRS cluster is in the security mode. Changing this creates a new instance.

`UserPassword` - (Optional) Specifies the password of the MRS cluster user. The password and username work in a pair. Changing this creates a new instance.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Version` - See Properties above.

`Agency` - See Properties above.

`Flavor` - See Properties above.

`Network/vpcId` - See Properties above.

`Network/subnetId` - See Properties above.

`Network/securityGroup` - See Properties above.

`Network/availableZone` - See Properties above.

`Network/publicIp/bindType` - See Properties above.

`Network/publicIp/eipId` - Indicates the EIP ID, This is returned only when bind_type is.

`MrsCluster` - See Properties above.

`Status` - Indicates the MLS instance status.

`InnerEndpoint` - Indicates the URL for accessing the instance. Only machines in the same.

`PublicEndpoint` - Indicates the URL for accessing the instance. The URL can be accessed.

`Created` - Indicates the creation time in the following format: yyyy-mm-dd Thh:mm:ssZ.

`Updated` - Indicates the update time in the following format: yyyy-mm-dd Thh:mm:ssZ.

## See Also

* [flexibleengine_mls_instance_v1](https://www.terraform.io/docs/providers/flexibleengine/r/mls_instance_v1.html) in the _Terraform Provider Documentation_