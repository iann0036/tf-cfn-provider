# Terraform::RabbitMQ::Policy

The ``Terraform::RabbitMQ::Policy`` resource creates and manages policies for exchanges
and queues.

## Properties

`Name` - (Required) The name of the policy.

`Vhost` - (Required) The vhost to create the resource in.

`Policy` - (Required) The settings of the policy. The structure is described below.

### Policy Properties

`Pattern` - (Required) A pattern to match an exchange or queue name.

`Priority` - (Required) The policy with the greater priority is applied first.

`ApplyTo` - (Required) Can either be "exchanges", "queues", or "all".

`Definition` - (Required) Key/value pairs of the policy definition. See the RabbitMQ documentation for definition references and examples.


## See Also

* [rabbitmq_policy](https://www.terraform.io/docs/providers/rabbitmq/r/policy.html) in the _Terraform Provider Documentation_