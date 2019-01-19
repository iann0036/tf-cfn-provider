# Terraform::AWS::EcsTaskDefinition

Manages a revision of an ECS task definition to be used in `aws_ecs_service`.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - Full ARN of the Task Definition (including both `family` and `revision`).

`Family` - The family of the Task Definition.

`Revision` - The revision of the task in a particular family.

## See Also

* [aws_ecs_task_definition](https://www.terraform.io/docs/providers/aws/r/ecs_task_definition.html) in the _Terraform Provider Documentation_