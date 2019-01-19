# Terraform::AWS::SwfDomain

Provides an SWF Domain resource.

## Properties

`Name` - (Optional, Forces new resource) The name of the domain. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - (Optional, Forces new resource) The domain description.

`WorkflowExecutionRetentionPeriodInDays` - (Required, Forces new resource) Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.


## Return Values

### Fn::GetAtt

`Id` - The name of the domain.

## See Also

* [aws_swf_domain](https://www.terraform.io/docs/providers/aws/r/swf_domain.html) in the _Terraform Provider Documentation_