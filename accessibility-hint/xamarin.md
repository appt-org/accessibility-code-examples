# Accessibility hint - Xamarin

In Xamarin Forms you can set an accessibility hint by using the [`AutomationProperties.HelpText`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieshelptext) property.

```xml
<Button
  AutomationProperties.HelpText="Opens the Appt website" />
```

```csharp
AutomationProperties.SetHelpText(button, "Opens the Appt website");
```
