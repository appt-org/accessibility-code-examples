# Accessibility dialog - .NET MAUI

In .NET MAUI you can use the [`DisplayAlert`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.page.displayalert?view=net-maui-8.0) method to show an alert. The last parameter of the method is the text of cancel button and it is required to supply it. Therefore, a cancel button is always shown! The focus of assistive technologies is automatically trapped inside the dialog while it is visible.

The code sample below shows how to show a dialog.

```csharp
var accept = await App.Current.MainPage.DisplayAlert(
  "Confirm Appt membership?", 
  "Your bank account will be billed.",
  "Proceed",
  "Cancel"
);

if (accept) {
    // Proceed
} else {
    // Cancel
}
```
