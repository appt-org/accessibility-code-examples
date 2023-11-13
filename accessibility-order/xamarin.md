# Accessibility order - Xamarin

Xamarin Forms supports changing the accessibility order through the [`TabIndex`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.tabindex?view=xamarin-forms) property. The default value is 0. The lower the value, the higher the priority. For example, to reach the save button before reaching the cancel button, the cancel button's `TabIndex` needs to be higher than the save button.

```xml
<Label Text="Appt" />
<Button x:Name="cancelButton" TabIndex="20" />
<Button x:Name="saveButton" TabIndex="10"/>
```
