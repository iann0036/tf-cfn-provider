# Terraform::Docker::Service

This resource manages the lifecycle of a Docker service. By default, the creation, update and delete of services are detached.

With the [Converge Config](#convergeconfig) the behavior of the `docker cli` is imitated to guarantee that
for example, all tasks of a service are running or successfully updated or to inform `terraform` that a service could not
be updated and was successfully rolled back.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [docker_service](https://www.terraform.io/docs/providers/docker/r/service.html) in the _Terraform Provider Documentation_