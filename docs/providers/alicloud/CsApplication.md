# Terraform::Alicloud::CsApplication

This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
Each application can contain one or more services.

-> **NOTE:** Application orchestration template must be a valid Docker Compose YAML template.

-> **NOTE:** At present, this resource only support swarm cluster.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the container application. It's formate is `<cluster_name>:<name>`.

`ClusterName` - The name of the container cluster.

`Name` - The application name.

`Description` - The application description.

`Template` - The application deploying template.

`Environment` - The application environment variables.

`Services` - List of services in the application. It contains several attributes to `Block Nodes`.

`DefaultDomain` - The application default domain and it can be used to configure routing service.

## See Also

* [alicloud_cs_application](https://www.terraform.io/docs/providers/alicloud/r/cs_application.html) in the _Terraform Provider Documentation_