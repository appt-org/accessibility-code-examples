# Accessibility dialog - Xamarin

In Xamarin Forms you can use the [`DisplayAlert`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.displayalert?view=xamarin-forms) method to show an alert. The last parameter of the method is the text of cancel button and it is required to supply it. Therefore, a cancel button is always shown! The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

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
