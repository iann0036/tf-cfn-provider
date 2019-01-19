# Terraform::AWS::BudgetsBudget

Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.

## Properties

`AccountId` - (Optional) The ID of the target account for budget. Will use current user's account_id by default if omitted.

`Name` - (Optional) The name of a budget. Unique within accounts.

`NamePrefix` - (Optional) The prefix of the name of a budget. Unique within accounts.

`BudgetType` - (Required) Whether this budget tracks monetary cost or usage.

`CostFilters` - (Optional) Map of [CostFilters](#CostFilters) key/value pairs to apply to the budget.

`CostTypes` - (Optional) Object containing [CostTypes](#CostTypes) The types of cost included in a budget, such as tax and subscriptions..

`LimitAmount` - (Required) The amount of cost or usage being measured for a budget.

`LimitUnit` - (Required) The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.

`TimePeriodEnd` - (Optional) The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.

`TimePeriodStart` - (Required) The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.

`TimeUnit` - (Required) The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.


## Return Values

### Fn::GetAtt

`Id` - id of resource.

## See Also

* [aws_budgets_budget](https://www.terraform.io/docs/providers/aws/r/budgets_budget.html) in the _Terraform Provider Documentation_