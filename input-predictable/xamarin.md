# Input predictable - Xamarin

In Xamarin, be careful when using [`TextChanged`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.inputview.textchanged?view=xamarin-forms) callbacks. Do not trigger a change of context when text changes.

```csharp
entry.TextChanged += OnEntryTextChanged;

void OnEntryTextChanged(object sender, TextChangedEventArgs args)
{
  // Do not change context
}
```
