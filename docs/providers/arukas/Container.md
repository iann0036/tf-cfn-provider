# Terraform::Arukas::Container

Provides container resource. This allows container to be created, updated and deleted.

For additional details please refer to [API documentation](https://arukas.io/en/documents-en/arukas-api-reference-en/).

## Properties

`Name` - (Required, string) The name of the container.

`Image` - (Required, string) The ID of the image to back this container.It must be a public image on DockerHub.

`Instances` - (Optional, int) The count of the instance. It must be between `1` and `10`.

`Plan` - (Optional, string) The plan of the Arukas. It must be `free` or `hobby` or `standard-1` or `standard-2`.

`Endpoint` - (Optional,string) The subdomain part of the endpoint assigned by Arukas. If it is not set, Arukas will do automatic assignment.

`Ports` - (Required , block) See [Ports](#ports) below for details.

`Environments` - (Required , block) See [Environments](#environments) below for details.

`Cmd` - (Optional , string) The command of the container.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Arukas application to which the Arukas Service and the container belongs.

`ServiceId` - The ID of the Arukas Service to which the container belongs.

`Name` - The name of the container.

`Image` - The ID of the image to back this container.

`Instances` - The count of the instance.

`Region` - The name of region.

`Plan` - The name of plan.

`Endpoint` - The subdomain part of the endpoint assigned by Arukas.

`Ports` - See [Ports](#ports) below for details.

`Environments` - See [Environments](#environments) below for details.

`Cmd` - The command of the container.

`PortMappings` - See [PortMappings](#port_mappings) below for details.

`EndpointFullUrl` - The URL of endpoint.

`EndpointFullHostname` - The Hostname of endpoint.

## See Also

* [arukas_container](https://www.terraform.io/docs/providers/arukas/r/container.html) in the _Terraform Provider Documentation_