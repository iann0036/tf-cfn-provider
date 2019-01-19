# Terraform::Panos::DagTags

This resource allows you to add and remove dynamic address group tags.

The `ip` field should be unique in the `panos_dag_tags` block, and there
should only be one `panos_dag_tags` block defined in a given plan.

**Note** - Tags are only removed during `terraform destroy`.  Updating an
applied terraform plan to have alternative tags will leave behind the
old tags from the previously published plan(s).

## Properties

TBC

## See Also

* [panos_dag_tags](https://www.terraform.io/docs/providers/panos/r/dag_tags.html) in the _Terraform Provider Documentation_