# Terraform::RabbitMQ::Binding

The ``Terraform::RabbitMQ::Binding`` resource creates and manages a binding relationship
between a queue an exchange.

## Properties

`Source` - (Required) The source exchange.

`Vhost` - (Required) The vhost to create the resource in.

`Destination` - (Required) The destination queue or exchange.

`DestinationType` - (Required) The type of destination (queue or exchange).

`RoutingKey` - (Optional) A routing key for the binding.

`Arguments` - (Optional) Additional key/value arguments for the binding.


## Return Values

### Fn::GetAtt

`PropertiesKey` - A unique key to refer to the binding.

## See Also

* [rabbitmq_binding](https://www.terraform.io/docs/providers/rabbitmq/r/binding.html) in the _Terraform Provider Documentation_