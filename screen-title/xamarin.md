# Screen title - Xamarin

With Xamarin Forms, we recommend setting an appropriate [`Title`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.title?view=xamarin-forms#xamarin-forms-page-title) for each [`ContentPage`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.contentpage?view=xamarin-forms).

```xml
<ContentPage
    x:Class="NewPage"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    Title="{Binding PageTitle}">
    <ContentView>
        ...
    </ContentView>
</ContentPage>
```

```csharp
public NewPage()
{
    SetBinding(Page.TitleProperty, new Binding("Appt homescreen")); 
}
```
