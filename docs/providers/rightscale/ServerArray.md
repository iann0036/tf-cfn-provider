# Terraform::RightScale::ServerArray

Use this resource to create, update or destroy RightScale [server arrays](http://reference.rightscale.com/api1.5/resources/ResourceServerArrays.html).

## Properties

`Name` - (Required) The name of the server_array.

`Description` - (Optional) Description of the server_array.

`State` - (Required) he status of the server array. If enabled, the server array is enabled for scaling actions. One of "enabled" or "disabled".

`DeploymentHref` - (Required) Href of deployment in which to create server_array.

`ArrayType` - (Required) The type of server_array. One of "alert" or "queue".

`Optimized` - (Optional) A flag indicating whether Instances of this ServerArray should be optimized for high-performance volumes (e.g. Volumes supporting a specified number of IOPS). Not supported in all Clouds.

`DatacenterPolicy` - (Required) This is an array of datacenter policies. Each one must contain:.

### DatacenterPolicy Properties

`DatacenterHref` - (Required) The href of the server_array's datacenter / zone.

`Max` - (Required) Maximum numbers of servers that can be allocated in this datacenter (0 for unlimited).

`Weight` - (Required) Instance allocation (should total 100% accross datacenter_policies).

`ElasticityParams` - (Required).

`Bounds` - (Required).

`MinCount` - (Required) The minimum number of servers that must be operational at all times in the server array.

`MaxCount` - (Required) The maximum number of servers that can be operational at the same time in the server array.

`Pacing` - (Required).

`ResizeDownBy` - (Required) The number of servers to scale down by.

`ResizeUpBy` - (Required) The number of servers to scale up by.

`ResizeCalmTime` - (Optional) The time (in minutes) on how long you want to wait before you repeat another action.

`AlertSpecificParams` - (Required if alert array_type specified).

`DecisionThreshold` - (Required) The percentage of servers that must agree in order to trigger an alert before an action is taken.

`VotersTagPredicate` - (Optional) The Voters Tag that RightScale will use in order to determine when to scale up/down.

`QueueSpecificParams` - (Required if queue alert_type specified).

`CollectAuditEntries` - (Optional) The audit SQS queue that will store audit entries.

`ItemAge` - (Required).

`Algorithm` - (Optional) The algorithm that defines how an item's age will be determined, either by the average age or max (oldest) age.

`MaxAge` - (Optional) The threshold (in seconds) before a resize action occurs on the server array.

`Regexp` - (Optional) The regexp that helps the system determine an item's \"age\" in the queue. Example: created_at: (\\d\\d\\d\\d-\\d\\d-\\d\\d \\d\\d:\\d\\d:\\d\\d UTC).

`QueueSize` - (Required) Defines the ratio of worker instances per items in the queue. Example: If there are 50 items in the queue and \"Items per instance\" is set to 10, the server array will resize to 5 worker instances (50/10). Default = 1.

`Schedule` - (Optional).

`Day` - (Required) Specifies the day when an alert-based array resizes. One of "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday".

`MaxCount` - (Required) The maximum number of servers that must be operational at all times in the server array. NOTE: Any changes that are made to the min/max count in the server array schedule will overwrite the array's default min/max count settings.

`MinCount` - (Required) The minimum number of servers that must be operational at all times in the server array. NOTE: Any changes that are made to the min/max count in the server array schedule will overwrite the array's default min/max count settings.

`Time` - (Required) Specifies the time when an alert-based array resizes.

`Instance` - (Required) See [rightscale_instance](https://github.com/terraform-providers/terraform-provider-rightscale/blob/master/website/docs/r/cm_instance.markdown).


## See Also

* [rightscale_server_array](https://www.terraform.io/docs/providers/rightscale/r/server_array.html) in the _Terraform Provider Documentation_