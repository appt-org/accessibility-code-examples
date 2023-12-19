# Accessibility name - .NET MAUI

In .NET MAUI, the [`SemanticProperties.Description`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.semanticproperties.descriptionproperty#microsoft-maui-controls-semanticproperties-descriptionproperty) property is used as accessibility name.

```xml
<Control 
  SemanticProperties.Description="Appt" />
```

**Warning:**

1. Avoid setting the `Description` attached property on a `Label`. This will stop the `Text` property being spoken by the screen reader. This is because the visual text should ideally match the text read aloud by the screen reader.
2. Avoid setting the `Description` attached property on an `Entry` or `Editor` on Android. Doing so will stop TalkBack actions functioning. Instead, use the `Placeholder` property or the `Hint` attached property.
3. On iOS, if you set the `Description` property on any control that has children the screen reader will be unable to reach the children. This is because iOS doesn't provide accessibility features that allow the navigation from a parent element into a child element.
