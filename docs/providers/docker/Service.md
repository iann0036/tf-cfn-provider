# Terraform::Docker::Service

This resource manages the lifecycle of a Docker service. By default, the creation, update and delete of services are detached.

With the [Converge Config](#convergeconfig) the behavior of the `docker cli` is imitated to guarantee that
for example, all tasks of a service are running or successfully updated or to inform `terraform` that a service could not
be updated and was successfully rolled back.

## Properties

`Auth` - (Optional, block) See [Auth](#auth) below for details.

`Name` - (Required, string) The name of the Docker service.

`TaskSpec` - (Required, block) See [TaskSpec](#task-spec) below for details.

`Mode` - (Optional, block) See [Mode](#mode) below for details.

`UpdateConfig` - (Optional, block) See [UpdateConfig](#update-rollback-config) below for details.

`RollbackConfig` - (Optional, block) See [RollbackConfig](#update-rollback-config) below for details.

`EndpointSpec` - (Optional, block) See [EndpointSpec](#endpoint-spec) below for details.

`ConvergeConfig` - (Optional, block) See [Converge Config](#converge-config) below for details.


## See Also

* [docker_service](https://www.terraform.io/docs/providers/docker/r/service.html) in the _Terraform Provider Documentation_