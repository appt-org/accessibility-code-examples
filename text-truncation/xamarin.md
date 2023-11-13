# Text truncation - Xamarin

When using Xamarin.Forms, you can avoid text truncation by removing all instances of [`MaxLines`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.maxlines?view=xamarin-forms) from your app.

```xml
<Label
    Text="Avoid text truncation"
    MaxLines="REMOVE" />
```
