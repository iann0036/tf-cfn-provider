# Terraform::AWS::DatasyncAgent

Manages an AWS DataSync Agent deployed on premises.

~> **NOTE:** One of `activation_key` or `ip_address` must be provided for resource creation (agent activation). Neither is required for resource import. If using `ip_address`, Terraform must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_datasync_agent](https://www.terraform.io/docs/providers/aws/r/datasync_agent.html) in the _Terraform Provider Documentation_