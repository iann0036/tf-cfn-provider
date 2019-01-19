# Terraform::Skytap::Environment

Provides a Skytap Environment resource. An environment consists of one or more virtual machines, networks, 
and associated settings and metadata. Unlike a template, an environment can be run and have most of its settings 
modified. When an environment is created all of its VMs will be run.

## Properties

`TemplateId` - (Required, Force New) ID of the template you want to create an environment from. If updating with a new one then the environment will be recreated.

`Name` - (Required) User-defined name of the environment. Limited to 255 characters. UTF-8 character type. Will default to source template’s name if null is provided.

`Description` - (Required) User-defined description of the environment. Limited to 1000 characters. Null allowed. UTF-8 character type.

`OutboundTraffic` - (Optional) Indicates whether networks in the environment can send outbound traffic.

`Routable` - (Optional) Indicates whether networks within the environment can route traffic to one another.

`SuspendOnIdle` - (Optional) The number of seconds an environment can be idle before it is automatically suspended. Valid range: 300 to 86400 seconds (5 minutes to 1 day).

`SuspendAtTime` - (Optional) The date and time that the environment will be automatically suspended. Format: yyyy/mm/dd hh:mm:ss. By default, the suspend time uses the UTC offset for the time zone defined in your user account settings. Optionally, a different UTC offset can be supplied (for example: 2018/07/20 14:20:00 -0000). The value in the API response is converted to your time zone.

`ShutdownOnIdle` - (Optional) The number of seconds an environment can be idle before it is automatically shut down. Valid range: 300 to 86400 seconds (5 minutes to 1 day).

`ShutdownAtTime` - (Optional) The date and time that the environment will be automatically shut down. Format: yyyy/mm/dd hh:mm:ss. By default, the suspend time uses the UTC offset for the time zone defined in your user account settings. Optionally, a different UTC offset can be supplied (for example: 2018/07/20 14:20:00 -0000). The value in the API response is converted to your time zone.


## See Also

* [skytap_environment](https://www.terraform.io/docs/providers/skytap/r/environment.html) in the _Terraform Provider Documentation_