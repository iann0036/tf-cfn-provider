# Terraform::AWS::DatasyncAgent

Manages an AWS DataSync Agent deployed on premises.

~> **NOTE:** One of `ActivationKey` or `IpAddress` must be provided for resource creation (agent activation). Neither is required for resource import. If using `IpAddress`, Terraform must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.

## Properties

`Name` - (Required) Name of the DataSync Agent.

`ActivationKey` - (Optional) DataSync Agent activation key during resource creation. Conflicts with `IpAddress`. If an `IpAddress` is provided instead, Terraform will retrieve the `ActivationKey` as part of the resource creation.

`IpAddress` - (Optional) DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `ActivationKey`. DataSync Agent must be accessible on port 80 from where Terraform is running.

`Tags` - (Optional) Key-value pairs of resource tags to assign to the DataSync Agent.


## See Also

* [aws_datasync_agent](https://www.terraform.io/docs/providers/aws/r/datasync_agent.html) in the _Terraform Provider Documentation_