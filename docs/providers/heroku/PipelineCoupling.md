# Terraform::Heroku::PipelineCoupling

Provides a [Heroku Pipeline Coupling](https://devcenter.heroku.com/articles/pipelines)
resource.

A pipeline is a group of Heroku apps that share the same codebase. Once a
pipeline is created using [`heroku_pipeline`](./pipeline.html), and apps are added
to different stages using `heroku_pipeline_coupling`, you can promote app slugs
to the downstream stages.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The UUID of this pipeline coupling.

`App` - The name of the application.

`AppId` - The ID of the application.

`Pipeline` - The UUID of the pipeline.

`Stage` - The stage for this coupling.

## See Also

* [heroku_pipeline_coupling](https://www.terraform.io/docs/providers/heroku/r/pipeline_coupling.html) in the _Terraform Provider Documentation_