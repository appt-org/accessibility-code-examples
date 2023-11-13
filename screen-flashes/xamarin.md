# Frequent flashes - Xamarin

In Xamarin.Forms, flashing content might be a result of using [`Timer`](https://learn.microsoft.com/en-us/dotnet/api/System.Threading.Timer?view=net-7.0) or [`ViewExtensions`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.viewextensions?view=xamarin-forms) for animations. By default, each animation will take 250 milliseconds. Make sure your animations does not result in more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```csharp
Not available, contribute!
```
