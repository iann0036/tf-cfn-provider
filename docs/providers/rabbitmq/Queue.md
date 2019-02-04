# Terraform::RabbitMQ::Queue

The ``Terraform::RabbitMQ::Queue`` resource creates and manages a queue.

## Properties

`Name` - (Required) The name of the queue.

`Vhost` - (Required) The vhost to create the resource in.

`Settings` - (Required) The settings of the queue. The structure is
described below.

### Settings Properties

`Durable` - (Optional) Whether the queue survives server restarts.
Defaults to `false`.

`AutoDelete` - (Optional) Whether the queue will self-delete when all
consumers have unsubscribed.

`Arguments` - (Optional) Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `ArgumentsJson`.

`ArgumentsJson` - (Optional) A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.


## See Also

* [rabbitmq_queue](https://www.terraform.io/docs/providers/rabbitmq/r/queue.html) in the _Terraform Provider Documentation_