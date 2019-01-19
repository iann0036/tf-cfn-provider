# Terraform::Circonus::Worksheet

The ``Terraform::Circonus::Worksheet`` resource creates and manages a
[Circonus Worksheet](https://login.circonus.com/resources/api/calls/worksheet).

## Properties

`Title` - (Required) The title of the worksheet.

`Description` - (Optional) Description of what the worksheet is for.

`Favourite` - (Optional) Mark (star) this worksheet as a favorite. Default is `false`.

`Notes` - (Optional) A place to store notes about this worksheet.

`Graphs` - (Optional) A list of graphs that compose this worksheet.

`SmartQueries` - (Optional) The smart queries that will be displayed on this worksheet. See below for details on how to configure a `smart_query`.

`Tags` - (Optional) A list of tags assigned to this worksheet.


## See Also

* [circonus_worksheet](https://www.terraform.io/docs/providers/circonus/r/worksheet.html) in the _Terraform Provider Documentation_