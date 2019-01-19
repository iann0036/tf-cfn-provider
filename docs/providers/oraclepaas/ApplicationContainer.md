# Terraform::OraclePaaS::ApplicationContainer

The `Terraform::OraclePaaS::ApplicationContainer` resource creates and manages an Application Container.

## Properties

`Name` - (Required) The name of the Application Container.

`ManifestFile` - (Optional) The json manifest file containing the attributes related to launching an application. Use either `ManifestFile` or `manifest_attributes` when specifying launch information.

`Manifest` - (Optional) The manifest attributes related to launching an application. Use either `ManifestFile` or `Manifest` when specifying launch information. Manifest attributes is documented below.

`DeploymentFile` - (Optional) The json deployment file containing the attributes related to deploying an application. Use either `DeploymentFile` or `deployment_attributes` when specifying deployment information.

`Deployment` - (Optional) The deployment attributes related to deploying an application. Use either `DeploymentFile` or `Deployment` when specifying deployment information. Deployment attributes is documented below.

`ArchiveUrl` - (Optional) Location of the application archive file in Oracle Storage Cloud Service, in the format app-name/file-name.

`AuthType` - (Optional) Uses Oracle Identity Cloud Service to control who can access your Java SE 7 or 8, Node.js, or PHP application. Allowed values are `basic` and `oauth`.

`AvailabilityDomain` - (Optional) A list of one or more datacenter locations in the OCI region. Required on OCI.

`GitRepository` - (Optional) The URL of the git repository to use the application container.

`GitUsername` - (Optional) The username of a user with access to the git respository if the repository is private.

`GitPassword` - (Optional) The password for the user with access to the git repository if the repository is private.

`LoadBalancerSubnets` - (Optional) Two load balancer subnets. Required on OCI.

`Notes` - (Optional) Comments about the application deployment.

`NotificationEmail` - (Optional) Email address to which application deployment status updates are sent.

`Region` - (Optional) The name of the region where the application container will be deployed. Required on OCI.

`Runtime` - (Optional) The allowed runtime environment variables. The allowed variables are `java`, `node`, `php`, `python`, `golang`, `dotnet`, or `ruby`. The default is `java`.

`SubscriptionType` - (Optional) Whether the subscription type is `hourly` or `monthly`. The default is `hourly`.

`Tags` - (Optional) A map of tags for the application container.

`Runtime` - (Optional) Details the availble runtime attributes. Runtime is documented below.

`Type` - (Optional) Determines whether the application is public or private. The default is `worker` (private).

`Command` - (Optional) Launch command to execute after the application has been uploaded.

`Release` - (Optional) Details the release attributes of a specific build. Release is documented below.

`StartupTime` - (Optional) The maximum time in seconds to wait for an application to start.

`ShutdownTime` - (Optional) The maximum time in seconds to wait for an application to stop.

`Notes` - (Optional) Comments about the launch configuration.

`Mode` - (Optional) The restart mode for application instances when the application is restarted. The only allowed value is `rolling`.

`Clustered` - (Optional) Boolean for whether the application instances act as a cluster with failover capability.

`Home` - (Optional) The context root of the application.

`HealthCheckEndpoint` - (Optional) The URL that the application uses for health checks.

`Memory` - (Optional) The amount of memory in gigabytes made available to the application. The default is `2G`.

`Instances` - (Optional) The number of application instances. The default is `2`.

`Notes` - (Optional) Comments about the deployment.

`Environment` - (Optional) A map of environment variables used by the application.

`SecureEnvironment` - (Optional) A list of environment variables marked as secured on the user interface.

`JavaSystemProperties` - (Optional) A map os java system properties used by the application.

`Services` - (Optional) Service bindings for connections to other Oracle Cloud services. Services is documented below.

`MajorVersion` - (Required) The major version of the runtime environment.

`Build` - (Optional) The value for a specific build.

`Commit` - (Optional) The value for a specific commit.

`Version` - (Optional) The value for a specific version.

`Identifier` - (Required) The value for the identifier.

`Type` - (Required) The type of service. Allowed values are `JAAS`, `DBAAS`, `MYSQLCS`, `OEHCS`, `OEHPCS`, `DHCS`, `caching`.

`Name` - (Required) The name of the existing service.

`Username` - (Required) The username to connect to the service.

`Password` - (Required) The password to connect to the service.

`AppUrl` - URL of the created application.

`WebUrl` - Web URL of the application.


## See Also

* [oraclepaas_application_container](https://www.terraform.io/docs/providers/oraclepaas/r/application_container.html) in the _Terraform Provider Documentation_