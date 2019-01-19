# Terraform::Arukas::Container

Provides container resource. This allows container to be created, updated and deleted.

For additional details please refer to [API documentation](https://arukas.io/en/documents-en/arukas-api-reference-en/).

## Properties

TBC

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