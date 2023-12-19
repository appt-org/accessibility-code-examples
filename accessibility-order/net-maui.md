# Accessibility order - .NET MAUI

In .NET MAUI, you can use a `SemanticOrderView` to control the order of `VisualElements` for screen readers. This can be particularly useful when building user interfaces in orders differing from the order in which users and screen readers will navigate them. 

For more information check out the [`SemanticOrderView documentation`](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/maui/views/semantic-order-view).

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
        <Label Grid.Row="2" Text="This label is excluded in the accessibility tree on iOS" />
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

**Note:**

- The SemanticOrderView is part of the [`CommunityToolkit.Maui package``](https://docs.microsoft.com/dotnet/communitytoolkit/maui).

- On iOS, only the labels listed in the `ViewOrder` will be in the accessibility tree, in the specified order. A label without a `Name` will not be accessible. If you want the last label to be accessible it must have a name in `xaml` and must be added to the `ViewOrder` property of the `SemanticOrderView`.

- On Android, all labels are included in the accessibility tree. The order is: `TitleLabel`, `DescriptionLabel` and lastly the label without a name.
