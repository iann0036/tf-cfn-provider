# Terraform::AWS::MqBroker

Provides an MQ Broker Resource. This resources also manages users for the broker.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

Changes to an MQ Broker can occur when you change a
parameter, such as `Configuration` or `User`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`ApplyImmediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `ApplyImmediately` can result in a
brief downtime as the broker reboots.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplyImmediately` - (Optional) Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.

`AutoMinorVersionUpgrade` - (Optional) Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.

`BrokerName` - (Required) The name of the broker.

`Configuration` - (Optional) Configuration of the broker. See below.

`DeploymentMode` - (Optional) The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.

`EngineType` - (Required) The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.

`EngineVersion` - (Required) The version of the broker engine. Currently, Amazon MQ supports only `5.15.0` or `5.15.6`.

`HostInstanceType` - (Required) The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`.

`PubliclyAccessible` - (Optional) Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

`SecurityGroups` - (Required) The list of security group IDs assigned to the broker.

`SubnetIds` - (Optional) The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.

`MaintenanceWindowStartTime` - (Optional) Maintenance window start time. See below.

`Logs` - (Optional) Logging configuration of the broker. See below.

`User` - (Optional) The list of all ActiveMQ usernames for the specified broker. See below.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The unique ID that Amazon MQ generates for the broker.

`Arn` - The ARN of the broker.

`Instances` - A list of information about allocated brokers (both active & standby).

`Instances.0.consoleUrl` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).

`Instances.0.ipAddress` - The IP Address of the broker.

`Instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):.

## See Also

* [aws_mq_broker](https://www.terraform.io/docs/providers/aws/r/mq_broker.html) in the _Terraform Provider Documentation_