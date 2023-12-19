# Accessibility value - .NET MAUI

.NET MAUI elements such as [`Button`](https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/button) and [`Entry`](https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/entry) automatically include an accessibility value. When you create custom elements you have to set these properties yourself.

However, there is no dedicated property to set an accessibility value. You can embed the value inside the label by using [`MultiBinding`](https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/data-binding/multibinding) inside the [`SemanticProperties.Description`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.semanticproperties.descriptionproperty#microsoft-maui-controls-semanticproperties-descriptionproperty) property.

```xml
<Label>
  <SemanticProperties.Description>
    <MultiBinding StringFormat="{}{0}, {1}">
      <Binding Source="The value is: " />
      <Binding Source="{BindingValue}" />
    </MultiBinding>
  </SemanticProperties.Description>
</Label>
```
