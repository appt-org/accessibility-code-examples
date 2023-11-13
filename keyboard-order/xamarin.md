# Keyboard order - Xamarin

Xamarin Forms supports changing the keyboard order through the [`TabIndex`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.tabindex?view=xamarin-forms) property. The default value is 0. The lower the value, the higher the priority.

The [`IsTabStop`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.istabstop?view=xamarin-forms) property can be used to exclude elements from tabbed navigation.

Read more about [Keyboard Accessibility in Xamarin.Forms](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/keyboard).

The code example below shows how exclude the label from receiving keyboard focus, and how to reach the save button before reaching the cancel button.

```xml
<Label Text="Appt" IsTabStop="True" />
<Button x:Name="cancelButton" TabIndex="20" />
<Button x:Name="saveButton" TabIndex="10"/>
```
