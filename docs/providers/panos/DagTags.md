# Terraform::Panos::DagTags

This resource allows you to add and remove dynamic address group tags.

The `ip` field should be unique in the `Terraform::Panos::DagTags` block, and there
should only be one `Terraform::Panos::DagTags` block defined in a given plan.

**Note** - Tags are only removed during `terraform destroy`.  Updating an
applied terraform plan to have alternative tags will leave behind the
old tags from the previously published plan(s).

## Properties

`Vsys` - (Optional) The vsys to put the DAG tags in (default: `vsys1`).

`Register` - (Required) A set that includes `ip`, the IP address to be tagged
and `tags`, a list of tags to associate with the given IP.


## See Also

* [panos_dag_tags](https://www.terraform.io/docs/providers/panos/r/dag_tags.html) in the _Terraform Provider Documentation_