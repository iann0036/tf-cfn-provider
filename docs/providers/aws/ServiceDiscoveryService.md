# Terraform::AWS::ServiceDiscoveryService

Provides a Service Discovery Service resource.

## Properties

`Name` - (Required, ForceNew) The name of the service.

`Description` - (Optional) The description of the service.

`DnsConfig` - (Required) A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

`HealthCheckConfig` - (Optional) A complex type that contains settings for an optional health check. Only for Public DNS namespaces.

`HealthCheckCustomConfig` - (Optional, ForceNew) A complex type that contains settings for ECS managed health checks.


## Return Values

### Fn::GetAtt

`Id` - The ID of the service.

`Arn` - The ARN of the service.

## See Also

* [aws_service_discovery_service](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) in the _Terraform Provider Documentation_