# Accessibility focusable - .NET MAUI

In .NET MAUI, the [`IsInAccessibleTree`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.automationproperties.isinaccessibletreeproperty?view=net-maui-8.0#microsoft-maui-controls-automationproperties-isinaccessibletreeproperty) property indicates whether assistive technologies can focus on an element.

Also, the [`ExcludedWithChildren`] (https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.automationproperties.excludedwithchildrenproperty?view=net-maui-8.0#microsoft-maui-controls-automationproperties-excludedwithchildrenproperty) property determines if an element and its children can be focused by assistive technologies.

```xml
<Image 
  AutomationProperties.IsInAccessibleTree="false" />

<StackLayout AutomationProperties.ExcludedWithChildren="true">
...
</StackLayout>
```
