# Terraform::Google::CloudiotRegistry

Creates a device registry in Google's Cloud IoT Core platform. For more information see
[the official documentation](https://cloud.google.com/iot/docs/) and
[API](https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries).

## Properties

`Name` - (Required) A unique name for the resource, required by device registry. Changing this forces a new resource to be created.

`Project` - (Optional) The project in which the resource belongs. If it is not provided, the provider project is used.

`Region` - (Optional) The Region in which the created address should reside. If it is not provided, the provider region is used.

`EventNotificationConfig` - (Optional) A PubSub topics to publish device events. Structure is documented below.

`StateNotificationConfig` - (Optional) A PubSub topic to publish device state updates. Structure is documented below.

`MqttConfig` - (Optional) Activate or deactivate MQTT. Structure is documented below.

`HttpConfig` - (Optional) Activate or deactivate HTTP. Structure is documented below.

`Credentials` - (Optional) List of public key certificates to authenticate devices. Structure is documented below.

### EventNotificationConfig Properties

`PubsubTopicName` - (Required) PubSub topic name to publish device events.

### StateNotificationConfig Properties

`PubsubTopicName` - (Required) PubSub topic name to publish device state updates.

### MqttConfig Properties

`MqttEnabledState` - (Required) The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.

### HttpConfig Properties

`HttpEnabledState` - (Required) The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.

### Credentials Properties

`PublicKeyCertificate` - (Required) The certificate format and data.

### PublicKeyCertificate Properties

`Format` - (Required) The field allows only  `X509_CERTIFICATE_PEM`.

`Certificate` - (Required) The certificate data.


## See Also

* [google_cloudiot_registry](https://www.terraform.io/docs/providers/google/r/cloudiot_registry.html) in the _Terraform Provider Documentation_