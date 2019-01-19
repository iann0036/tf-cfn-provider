# Terraform::Heroku::PipelineCoupling

Provides a [Heroku Pipeline Coupling](https://devcenter.heroku.com/articles/pipelines)
resource.

A pipeline is a group of Heroku apps that share the same codebase. Once a
pipeline is created using [`Terraform::Heroku::Pipeline`](./pipeline.html), and apps are added
to different stages using `Terraform::Heroku::PipelineCoupling`, you can promote app slugs
to the downstream stages.

## Properties

`App` - (Required) The name of the app for this coupling.

`Pipeline` - (Required) The ID of the pipeline to add this app to.

`Stage` - (Required) The stage to couple this app to. Must be one of `review`, `development`, `staging`, or `production`.


## Return Values

### Fn::GetAtt

`Id` - The UUID of this pipeline coupling.

`App` - The name of the application.

`AppId` - The ID of the application.

`Pipeline` - The UUID of the pipeline.

`Stage` - The stage for this coupling.

## See Also

* [heroku_pipeline_coupling](https://www.terraform.io/docs/providers/heroku/r/pipeline_coupling.html) in the _Terraform Provider Documentation_