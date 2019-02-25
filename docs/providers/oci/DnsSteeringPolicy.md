# Terraform::OCI::DnsSteeringPolicy

This resource provides the Steering Policy resource in Oracle Cloud Infrastructure Dns service.

Creates a new steering policy in the specified compartment.

## Properties

`Answers` - (Optional) The set of all answers that can potentially issue from the steering policy.
* `IsDisabled` - (Optional) Whether or not an answer should be excluded from responses, e.g. because the corresponding server is down for maintenance. Note, however, that such filtering is not automatic and will only take place if a rule implements it.
* `Name` - (Required) A user-friendly name for the answer, unique within the steering policy.
* `Pool` - (Optional) The freeform name of a group of one or more records (e.g., a data center or a geographic region) in which this one is included.
* `Rdata` - (Required) The record's data, as whitespace-delimited tokens in type-specific presentation format.
* `Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`IsDisabled` - (Optional) Whether or not an answer should be excluded from responses, e.g. because the corresponding server is down for maintenance. Note, however, that such filtering is not automatic and will only take place if a rule implements it.
* `Name` - (Required) A user-friendly name for the answer, unique within the steering policy.
* `Pool` - (Optional) The freeform name of a group of one or more records (e.g., a data center or a geographic region) in which this one is included.
* `Rdata` - (Required) The record's data, as whitespace-delimited tokens in type-specific presentation format.
* `Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`Name` - (Required) A user-friendly name for the answer, unique within the steering policy.
* `Pool` - (Optional) The freeform name of a group of one or more records (e.g., a data center or a geographic region) in which this one is included.
* `Rdata` - (Required) The record's data, as whitespace-delimited tokens in type-specific presentation format.
* `Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`Pool` - (Optional) The freeform name of a group of one or more records (e.g., a data center or a geographic region) in which this one is included.
* `Rdata` - (Required) The record's data, as whitespace-delimited tokens in type-specific presentation format.
* `Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`Rdata` - (Required) The record's data, as whitespace-delimited tokens in type-specific presentation format.
* `Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`Rtype` - (Required) The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`CompartmentId` - (Required) The OCID of the compartment containing the steering policy.

`DefinedTags` - (Optional) (Updatable) Usage of predefined tag keys. These predefined keys are scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

`DisplayName` - (Required) (Updatable) A user-friendly name for the steering policy. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"bar-key": "value"}`.

`HealthCheckMonitorId` - (Optional) (Updatable) The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `Rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `Rdata` not matching any monitored endpoint will be assumed healthy.

`Rules` - (Optional) The pipeline of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.

`Cases` - (Optional)
* `AnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`AnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`CaseCondition` - (Applicable when rule_type=FILTER | HEALTH | LIMIT | PRIORITY | WEIGHTED)
* `Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`Count` - (Required when rule_type=LIMIT)
* `DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`DefaultAnswerData` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED) Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.
* `AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`AnswerCondition` - (Applicable when rule_type=FILTER | PRIORITY | WEIGHTED)
* `ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`ShouldKeep` - (Applicable when rule_type=FILTER) Keep the answer if the value is `True`.
* `Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`Value` - (Required when rule_type=PRIORITY | WEIGHTED)
* `DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`DefaultCount` - (Applicable when rule_type=LIMIT) Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.
* `Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`Description` - (Optional) Your description of the rule's purpose and/or behavior.
* `RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`RuleType` - (Required) The type of a rule determines its sorting/filtering behavior.
* FILTER rules filter the list of answers (e.g., to remove those with hosts that are down for maintenance). Answers remain if and only if their associated data is `True`.
* HEALTH rules remove answers from the list if their `Rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.
* WEIGHTED rules probabilistically move answers with greater associated integer data to the beginning of the list.
* PRIORITY rules sort answers by associated integer data, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value.
* LIMIT rules filter away answers that are too far down the list. Parameter "count" specifies how many answers to keep.

`Template` - (Required) (Updatable) The common pattern (or lack thereof) to which the steering policy adheres. This value restricts the possible configurations of rules, but thereby supports specifically tailored interfaces. Values other than "CUSTOM" require the rules to begin with an unconditional FILTER that keeps answers contingent upon `answer.isDisabled != true`, followed _if and only if the policy references a health check monitor_ by an unconditional HEALTH rule, and require the last rule to be an unconditional LIMIT. What must precede the LIMIT rule is determined by the template value:
* FAILOVER requires exactly an unconditional PRIORITY rule that ranks answers by pool. Each answer pool must have a unique priority value assigned to it. Answer data must be defined in the `DefaultAnswerData` property for the rule and the `Cases` property must not be defined.
* LOAD_BALANCE requires exactly an unconditional WEIGHTED rule that shuffles answers by name. Answer data must be defined in the `DefaultAnswerData` property for the rule and the `Cases` property must not be defined.
* ROUTE_BY_GEO requires exactly one PRIORITY rule that ranks answers by pool using the geographical location of the client as a condition. Within that rule you may only use `Query.client.geoKey` in the `caseCondition` expressions for defining the cases. For each case in the PRIORITY rule each answer pool must have a unique priority value assigned to it. Answer data can only be defined within cases and `DefaultAnswerData` cannot be used in the PRIORITY rule.
* ROUTE_BY_ASN requires exactly one PRIORITY rule that ranks answers by pool using the ASN of the client as a condition. Within that rule you may only use `Query.client.asn` in the `caseCondition` expressions for defining the cases. For each case in the PRIORITY rule each answer pool must have a unique priority value assigned to it. Answer data can only be defined within cases and `DefaultAnswerData` cannot be used in the PRIORITY rule.
* ROUTE_BY_IP requires exactly one PRIORITY rule that ranks answers by pool using the IP subnet of the client as a condition. Within that rule you may only use `Query.client.address` in the `caseCondition` expressions for defining the cases. For each case in the PRIORITY rule each answer pool must have a unique priority value assigned to it. Answer data can only be defined within cases and `DefaultAnswerData` cannot be used in the PRIORITY rule.
* CUSTOM allows an arbitrary configuration of rules.

`Ttl` - (Optional) (Updatable) The Time To Live for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.


## Return Values

### Fn::GetAtt

`Ttl` - The Time To Live for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.

`TimeCreated` - The date and time the resource was created in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

`HealthCheckMonitorId` - The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `Rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `Rdata` not matching any monitored endpoint will be assumed healthy.

`DefaultCount` - Defines a default count if `Cases` is not defined for the rule or a matching case does not define `Count`. `defaultCount` is **not** applied if `Cases` is defined and there are no matching cases.

`Id` - The OCID of the resource.

`DisplayName` - A user-friendly name for the steering policy. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`CompartmentId` - The OCID of the compartment containing the steering policy.

`DefinedTags` - Usage of predefined tag keys. These predefined keys are scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

`Self` - The canonical absolute URL of the resource.

`DefaultAnswerData` - Defines a default set of answer conditions and values that are applied to an answer when `Cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `DefaultAnswerData` is **not** applied if `Cases` is defined and there are no matching cases.

`FreeformTags` - Simple key-value pair that is applied without any predefined name, type, or scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"bar-key": "value"}`.

`State` - The current state of the resource.

`Template` - The common pattern (or lack thereof) to which the steering policy adheres. This value restricts the possible configurations of rules, but thereby supports specifically tailored interfaces. Values other than "CUSTOM" require the rules to begin with an unconditional FILTER that keeps answers contingent upon `answer.isDisabled != true`, followed _if and only if the policy references a health check monitor_ by an unconditional HEALTH rule, and require the last rule to be an unconditional LIMIT. What must precede the LIMIT rule is determined by the template value:.

`Description` - Your description of the rule's purpose and/or behavior.

`Rules` - The pipeline of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.

`IsDisabled` - Whether or not an answer should be excluded from responses, e.g. because the corresponding server is down for maintenance. Note, however, that such filtering is not automatic and will only take place if a rule implements it.

`Answers` - The set of all answers that can potentially issue from the steering policy.

`Rdata` - The record's data, as whitespace-delimited tokens in type-specific presentation format.

`ShouldKeep` - Keep the answer if the value is `True`.

`Pool` - The freeform name of a group of one or more records (e.g., a data center or a geographic region) in which this one is included.

`RuleType` - The type of a rule determines its sorting/filtering behavior.

`Name` - A user-friendly name for the answer, unique within the steering policy.

`Rtype` - The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

## See Also

* [oci_dns_steering_policy](https://www.terraform.io/docs/providers/oci/r/dns_steering_policy.html) in the _Terraform Provider Documentation_