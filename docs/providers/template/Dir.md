# Terraform::Template::Dir

Renders a directory containing templates into a separate directory of
corresponding rendered files.

`Terraform::Template::Dir` is similar to [`templateFile`](../d/file.html) but it walks
a given source directory and treats every file it encounters as a template,
rendering it to a corresponding file in the destination directory.

~> **Note** When working with local files, Terraform will detect the resource
as having been deleted each time a configuration is applied on a new machine
where the destination dir is not present and will generate a diff to create
it. This may cause "noise" in diffs in environments where configurations are
routinely applied by many different users or within automation systems.

## Properties

`SourceDir` - (Required) Path to the directory where the files to template reside.

`DestinationDir` - (Required) Path to the directory where the templated files will be written.

`Vars` - (Optional) Variables for interpolation within the template. Note that variables must all be primitives. Direct references to lists or maps will cause a validation error.


## See Also

* [template_dir](https://www.terraform.io/docs/providers/template/r/dir.html) in the _Terraform Provider Documentation_