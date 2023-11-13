# Element focus change - Xamarin

In Xamarin.Forms, you can use the [`Focused`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.focused?view=xamarin-forms) event to listen to focus changes. The method is called when the element receives focus.

Be careful when the `Focused` callback: do not trigger any context change because they might confuse users.

```csharp
Element.Focused += (sender, arguments) => {
    // Do not change context
};
```
