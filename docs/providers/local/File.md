# Terraform::Local::File

Generates a local file with the given content.

~> **Note** When working with local files, Terraform will detect the resource
as having been deleted each time a configuration is applied on a new machine
where the file is not present and will generate a diff to re-create it. This
may cause "noise" in diffs in environments where configurations are routinely
applied by many different users or within automation systems.

## Properties

TBC

## See Also

* [local_file](https://www.terraform.io/docs/providers/local/r/file.html) in the _Terraform Provider Documentation_