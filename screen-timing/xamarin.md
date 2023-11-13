# Adjustable timing - Xamarin

In Xamarin, the `SnackBar` view from the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) is often used to display temporary messages. The display duration might be too short for people to read or hear the message.

When using `SnackBar`, set the `Duration` to `Int32.MaxValue`. Or, use [`DisplayAlert`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.displayalert?view=xamarin-forms) method to show an alert instead.

Also make sure that the use of time limits, e.g. by using [`Timer`](https://learn.microsoft.com/en-us/dotnet/api/System.Threading.Timer?view=net-7.0), can be extended.

```csharp
var result = await page.DisplaySnackBarAsync("Appt", "Close", async () =>
    { /* Action */ },
    Int32.MaxValue
);
```
