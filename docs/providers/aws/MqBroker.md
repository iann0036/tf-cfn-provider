# Terraform::AWS::MqBroker

Provides an MQ Broker Resource. This resources also manages users for the broker.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

Changes to an MQ Broker can occur when you change a
parameter, such as `configuration` or `user`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `apply_immediately` can result in a
brief downtime as the broker reboots.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique ID that Amazon MQ generates for the broker.

`Arn` - The ARN of the broker.

`Instances` - A list of information about allocated brokers (both active & standby).

`Instances.0.consoleUrl` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).

`Instances.0.ipAddress` - The IP Address of the broker.

`Instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):.

## See Also

* [aws_mq_broker](https://www.terraform.io/docs/providers/aws/r/mq_broker.html) in the _Terraform Provider Documentation_