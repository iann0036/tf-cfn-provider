# LogicMonitor Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logicmonitor**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_id` - (Required) LogicMonitor API id. This can also be set via the `LM_API_ID` environment variable.
* `api_key` - (Required) LogicMonitor API key. This can also be set via the `LM_API_KEY` environment variable.
* `company` - (Required) LogicMonitor company name. This can also be set via the `LM_COMPANY` environment variable.


## Supported Resources

* [Terraform::LogicMonitor::CollectorGroup](docs/providers/logicmonitor/CollectorGroup.md)
* [Terraform::LogicMonitor::Collector](docs/providers/logicmonitor/Collector.md)
* [Terraform::LogicMonitor::DeviceGroup](docs/providers/logicmonitor/DeviceGroup.md)
* [Terraform::LogicMonitor::Device](docs/providers/logicmonitor/Device.md)