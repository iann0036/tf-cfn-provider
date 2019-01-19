# Terraform::RightScale::CwfProcess

Use this resource to create or destroy RightScale [CloudWorkFlow processes](http://docs.rightscale.com/ss/reference/rcl/).

Creating the CWF process runs it synchronously and returns the output values (if any). If the CWF process fails, the Terraform script fails too.

Destroying the resource deletes the corresponding CWF process. Destroying a running process causes it to end in error.

It is NOT possible to update a CWF process.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Status` - Process status, one of "completed", "failed", "canceled" or "aborted".

`Error` - Process execution error if any.

`Outputs` - Process outputs if any. This is a TypeMap, one particular output can be accessed via `outputs["$var"]`, see "Example Usage" section.

## See Also

* [rightscale_cwf_process](https://www.terraform.io/docs/providers/rightscale/r/cwf_process.html) in the _Terraform Provider Documentation_