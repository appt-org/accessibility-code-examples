# Accessibility order - .NET MAUI

Using the SemanticOrderView
The SemanticOrderView provides the ability to control the order of VisualElements for screen readers and improve the Accessibility of an application. This can be particularly useful when building user interfaces in orders differing from the order in which users and screen readers will navigate them. For more information see [`SemanticOrderView`](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/maui/views/semantic-order-view)

```xml
<ContentPage
    xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:toolkit="http://schemas.microsoft.com/dotnet/2022/maui/toolkit"
    x:Class="CommunityToolkit.Maui.Sample.Pages.Views.SemanticOrderViewPage"
    Title="Semantic Order View">
    <ContentPage.Content>
            <toolkit:SemanticOrderView x:Name="SemanticOrderView">
                <Grid RowDefinitions="*,2*,*">
                
                    <Label Grid.Row="0" x:Name="DescriptionLabel" Text="Label for description, first label in xaml file" />
                    <Label Grid.Row="1" x:Name="TitleLabel" Text="Title, second label in xaml file" FontSize="30" />
                    <Label Grid.Row="2" Text="This label not in a11yTree on iOS" />

                </Grid>
            </toolkit:SemanticOrderView>
    </ContentPage.Content>
</ContentPage>
```
```csharp
using System.Collections.Generic;

namespace CommunityToolkit.Maui.Sample.Pages.Views;

public partial class SemanticOrderViewPage : ContentPage
{
    public SemanticOrderViewPage()
    {
        InitializeComponent();

        this.SemanticOrderView.ViewOrder = new List<View> { TitleLabel, DescriptionLabel };
    }
}
```
**N.B.** On iOS only the labels mentioned in the ViewOrder (see ctor) will be in the accessibilitytree and in that order. So the label with no name will not be accessible. If you want the last label to be accessible it must have a name in xaml and must be added to the ViewOrder property of de SemanticOrderView.

On Android all the labels are in the accessibilitytree and the order is: TitleLabel, DescriptionLabel and then the label with no name.

For this to work you need the NuGet package CommunityToolkit.Maui see for [`Documentation`](https://docs.microsoft.com/dotnet/communitytoolkit/maui) and after installing the package read the ReadMe.txt