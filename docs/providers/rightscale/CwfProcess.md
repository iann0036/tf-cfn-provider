# Terraform::RightScale::CwfProcess

Use this resource to create or destroy RightScale [CloudWorkFlow processes](http://docs.rightscale.com/ss/reference/rcl/).

Creating the CWF process runs it synchronously and returns the output values (if any). If the CWF process fails, the Terraform script fails too.

Destroying the resource deletes the corresponding CWF process. Destroying a running process causes it to end in error.

It is NOT possible to update a CWF process.

## Properties

`Source` - (Required) Source code to be executed, written in [RCL (RightScale CloudWorkFlow Language)](http://docs.rightscale.com/ss/reference/rcl/v2/index.html). Several functions can be defined but the entry function should be called `main`. Example: ```hcl source = <<EOF define adder($n1, $n2) return $res do $res = $n1 + $n2 end define main($a, $b) return $result do call adder($a, $b) retrieve $tmp $result = "The total is " + $tmp end EOF ```.

`Parameters` - Parameters for the RCL function. It consists of an array of values corresponding to the values being passed to the function defined in the "source" field in order of declaration. The values are defined as string maps with the "kind" and "value" keys. "kind" contains the type of the value being passed, could be one of "array", "boolean", "collection", "datetime", "declaration", "null", "number", "object", "string". The "value" key contains the value For example: ```hcl parameters = [ { "kind" = "string" "value" = "db-slave-" }, { "kind" = "number" "value" = "42" } ] ``` Note that the "value" key should always be a string (regardless of the type specified in "kind"). These are several examples on how to pass arrays: ```hcl parameters = [ { "kind"  = "array" "value" = "[ 22.3, 9.7, 10 ]" }, { "kind"  = "array" "value" = "[ \"It\", \" works!\" ]" }, { "kind"  = "array" "value" = "${jsonencode(var.zones)}" }, ] ```.


## Return Values

### Fn::GetAtt

`Status` - Process status, one of "completed", "failed", "canceled" or "aborted".

`Error` - Process execution error if any.

`Outputs` - Process outputs if any. This is a TypeMap, one particular output can be accessed via `outputs["$var"]`, see "Example Usage" section.

## See Also

* [rightscale_cwf_process](https://www.terraform.io/docs/providers/rightscale/r/cwf_process.html) in the _Terraform Provider Documentation_