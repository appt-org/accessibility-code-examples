# Dark mode - Xamarin

With Xamarin, you can detect dark mode by checking if the [`RequestedTheme`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.application.requestedtheme?view=xamarin-forms) property equals [`OSAppTheme.Dark`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.osapptheme?view=xamarin-forms#fields).

In `XAML` you can use [`AppThemeBinding`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/xaml/markup-extensions/consuming#appthemebinding-markup-extension) to define different resources for dark mode.

```csharp
using Xamarin.Essentials;

OSAppTheme theme = Application.Current.RequestedTheme;
if (theme == OSAppTheme.Dark) {
    // Dark mode
}
```

```xml
<ContentPage>
    <StackLayout>
        <Label Text="This text is black in light mode and white in dark mode."
               TextColor="{AppThemeBinding Light=Black, Dark=White}" />
        <Image Source="{AppThemeBinding Light=logo_light.png, Dark=logo_dark.png}" />
    </StackLayout>
</ContentPage>
```
