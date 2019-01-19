# Terraform::Alicloud::CsApplication

This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
Each application can contain one or more services.

-> **NOTE:** Application orchestration template must be a valid Docker Compose YAML template.

-> **NOTE:** At present, this resource only support swarm cluster.

## Properties

`ClusterName` - (Required, Force new resource) The swarm cluster's name.

`Name` - (Required, Force new resource) The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.

`Description` - The description of application.

`Version` - The application deploying version. Each updating, it must be different with current. Default to "1.0".

`Template` - The application deployment template and it must be [Docker Compose format](https://docs.docker.com/compose/).

`Environment` - A key/value map used to replace the variable parameter in the Compose template.

`LatestImage` - Whether to use latest docker image while each updating application. Default to false.

`BlueGreen` - Wherther to use "Blue Green" method when release a new version. Default to false.

`BlueGreenConfirm` - Whether to confirm a "Blue Green" application. Default to false. It will be ignored when `BlueGreen` is false.


## Return Values

### Fn::GetAtt

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