# Terraform::AWS::GameliftGameSessionQueue

Provides an Gamelift Game Session Queue resource.

## Properties

`Name` - (Required) Name of the session queue.

`TimeoutInSeconds` - (Required) Maximum time a game session request can remain in the queue.

`Destinations` - (Optional) List of fleet/alias ARNs used by session queue for placing game sessions.

`PlayerLatencyPolicy` - (Optional) One or more policies used to choose fleet based on player latency. See below.


## Return Values

### Fn::GetAtt

`Arn` - Game Session Queue ARN.

## See Also

* [aws_gamelift_game_session_queue](https://www.terraform.io/docs/providers/aws/r/gamelift_game_session_queue.html) in the _Terraform Provider Documentation_