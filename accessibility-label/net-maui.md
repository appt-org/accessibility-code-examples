# Accessibility label - .NET MAUI

In .NET MAUI, you can set an accessibility label by using the [`SemanticProperties.Description`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.semanticproperties.descriptionproperty#microsoft-maui-controls-semanticproperties-descriptionproperty) property.

```xml
<Control 
  SemanticProperties.Description="Appt" />
```

As an alternative, you can link a label by setting [`IsInAccessibleTree`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.automationproperties.isinaccessibletreeproperty#microsoft-maui-controls-automationproperties-isinaccessibletreeproperty) to `false` and setting [`SemanticProperties.Description`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.semanticproperties.descriptionproperty#microsoft-maui-controls-semanticproperties-descriptionproperty) the `value` of the label.

```xml
<Image
    Source="appt.png"
    SemanticProperties.Description="{Binding Source={x:Reference Welcome}, Path=Text}"
    HeightRequest="200"
    HorizontalOptions="Center" />

<Label
    x:Name="Welcome"
    AutomationProperties.IsInAccessibleTree="False"
    Text="Welcome to Appt"
    FontSize="18"
    HorizontalOptions="Center" />
```

**Note**: `SemanticProperties.Description` will supersede the value of `AutomationProperties.IsInAccessibleTree`.

In the sample below, the text from `SemanticProperties.Description` will be spoken despite of the value of `AutomationProperties.IsInAccessibleTree`.

```xml
<Label
    x:Name="Welcome"
    AutomationProperties.IsInAccessibleTree="False"
    SemanticProperties.Description="Welcome to Appt (will be sproken)"
    Text="Welcome to Appt"
    FontSize="18"
    HorizontalOptions="Center" />
```
