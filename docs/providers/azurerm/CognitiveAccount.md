# Terraform::AzureRM::CognitiveAccount

Manages a Cognitive Services Account.

## Properties

`Name` - (Required) Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Kind` - (Required) Specifies the type of Cognitive Service Account that should be created. Possible values are `Academic`, `Bing.Autosuggest`, `Bing.Autosuggest.v7`, `Bing.CustomSearch`, `Bing.Search`, `Bing.Search.v7`, `Bing.Speech`, `Bing.SpellCheck`, `Bing.SpellCheck.v7`, `ComputerVision`, `ContentModerator`, `CustomSpeech`, `Emotion`, `Face`, `LUIS`, `Recommendations`, `SpeakerRecognition`, `Speech`, `SpeechServices`, `SpeechTranslation`, `TextAnalytics`, `TextTranslation` and `WebLM`. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Required) Specifies the Name of the Sku. Possible values are `F0`, `S0`, `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `P0`, `P1` and `P2`.

`Tier` - (Required) Specifies the Tier of the Sku. Possible values include `Free`, `Standard` and `Premium`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Cognitive Service Account.

`Endpoint` - The endpoint used to connect to the Cognitive Service Account.

`PrimaryAccessKey` - A primary access key which can be used to connect to the Cognitive Service Account.

`SecondaryAccessKey` - The secondary access key which can be used to connect to the Cognitive Service Account.

## See Also

* [azurerm_cognitive_account](https://www.terraform.io/docs/providers/azurerm/r/cognitive_account.html) in the _Terraform Provider Documentation_