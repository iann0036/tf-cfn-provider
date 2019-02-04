# Terraform::RabbitMQ::Exchange

The ``Terraform::RabbitMQ::Exchange`` resource creates and manages an exchange.

## Properties

`Name` - (Required) The name of the exchange.

`Vhost` - (Required) The vhost to create the resource in.

`Settings` - (Required) The settings of the exchange. The structure is
described below.

### Settings Properties

`Type` - (Required) The type of exchange.

`Durable` - (Optional) Whether the exchange survives server restarts.
Defaults to `false`.

`AutoDelete` - (Optional) Whether the exchange will self-delete when all
queues have finished using it.

`Arguments` - (Optional) Additional key/value settings for the exchange.


## See Also

* [rabbitmq_exchange](https://www.terraform.io/docs/providers/rabbitmq/r/exchange.html) in the _Terraform Provider Documentation_