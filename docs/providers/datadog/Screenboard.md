# Terraform::Datadog::Screenboard

Provides a Datadog screenboard resource. This can be used to create and manage Datadog screenboards.

## Properties

`Title` - (Required) The name of the screenboard.
- `Height` - (Optional) The screenboard's height.
- `Width` - (Optional) The screenboard's width.
- `ReadOnly` - (Optional) The read-only status of the screenboard. Default is false.
- `Shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`Height` - (Optional) The screenboard's height.
- `Width` - (Optional) The screenboard's width.
- `ReadOnly` - (Optional) The read-only status of the screenboard. Default is false.
- `Shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`Width` - (Optional) The screenboard's width.
- `ReadOnly` - (Optional) The read-only status of the screenboard. Default is false.
- `Shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`ReadOnly` - (Optional) The read-only status of the screenboard. Default is false.
- `Shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`Shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`Widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

`TemplateVariable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.


## See Also

* [datadog_screenboard](https://www.terraform.io/docs/providers/datadog/r/screenboard.html) in the _Terraform Provider Documentation_