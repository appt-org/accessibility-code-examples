# Accessibility value - Xamarin

Xamarin Forms elements such as [`Button`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/button) and [`Entry`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/entry) automatically include an accessibility value. When you make custom elements you have to set these properties yourself.

However, there is no dedicated property to set an accessibility value. You can embed the value inside the label by using [`MultiBinding`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/data-binding/multibinding) inside the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property.

```xml
<Label
    <AutomationProperties.Name>
        <MultiBinding StringFormat="{}{0}, {1}">
            <Binding Source="The value is: " />
            <Binding Source="{BindingValue}" />
        </MultiBinding>
    </AutomationProperties.Name>
</Label>
```
