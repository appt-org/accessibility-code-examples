# Accessibility label - Xamarin

In Xamarin Forms, you can set an accessibility label by using the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property.

If another element is used to display the label, the [`AutomationProperties.LabeledBy`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieslabeledby) property be used to link a label. Unfortunately, `LabeledBy` only works on Android.

As an alternative, you can link a label by setting [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree) to `false` and setting [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) the `value` of the label.

```xml
<Control 
  AutomationProperties.Name="Appt" />
```
