# Input label - Xamarin

In Xamarin, you can use the [`AutomationProperties.LabeledBy`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieslabeledby) property to link a label to an input field. However, `LabeledBy` only works on Android.

You can also link a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to an [`Entry`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/entry) by setting [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree) to `false` on the label, and setting [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property to the value of the label.

```xml
<Label x:Name="label" 
       Text="Name" 
       AutomationProperties.IsInAccessibleTree="false" />

<Entry AutomationProperties.Name="{x:Reference label}"
       AutomationProperties.LabeledBy="{x:Reference label}" />
```
