# Input errors - Xamarin

In Xamarin.Forms, we recommend using a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```xml
<Label
    Text="Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000"
    IsVisible="{Binding IsValid}" />
```
