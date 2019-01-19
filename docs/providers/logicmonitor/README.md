# LogicMonitor Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logicmonitor**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_id` - (Required) LogicMonitor API id.
* `api_key` - (Required) LogicMonitor API key.
* `company` - (Required) LogicMonitor company name.


## Supported Resources

* [Terraform::LogicMonitor::CollectorGroup](CollectorGroup.md)
* [Terraform::LogicMonitor::Collector](Collector.md)
* [Terraform::LogicMonitor::DeviceGroup](DeviceGroup.md)
* [Terraform::LogicMonitor::Device](Device.md)