# Accessibility hint - .NET MAUI

In .NET MAUI, an accessibility hint is set by using the [`SemanticProperties.Hint`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.semanticproperties.hintproperty?view=net-maui-8.0#microsoft-maui-controls-semanticproperties-hintproperty) property.

```xml
<Control 
  SemanticProperties.Hint="Opens the Appt website" />
```

**Warning:**
The `Hint` property conflicts with the `Entry.Placeholder` property on Android, which both map to the same platform property. Therefore, setting a different Hint value to the Entry.Placeholder value isn't recommended.