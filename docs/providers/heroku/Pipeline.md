# Terraform::Heroku::Pipeline

Provides a [Heroku Pipeline](https://devcenter.heroku.com/articles/pipelines)
resource.

A pipeline is a group of Heroku apps that share the same codebase. Once a
pipeline is created, and apps are added to different stages using
[`Terraform::Heroku::PipelineCoupling`](./pipeline_coupling.html), you can promote app
slugs to the next stage.

## Properties

`Name` - (Required) The name of the pipeline.


## Return Values

### Fn::GetAtt

`Id` - The UUID of the pipeline.

`Name` - The name of the pipeline.

## See Also

* [heroku_pipeline](https://www.terraform.io/docs/providers/heroku/r/pipeline.html) in the _Terraform Provider Documentation_