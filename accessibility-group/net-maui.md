# Accessibility group - .NET MAUI

In .NET MAUI you can group items together by setting `AutomationProperties.IsInAccessibleTree` to `true`. You also need to set a `SemanticProperties.Description` for the grouped elements.

```xml
<HorizontalStackLayout
    x:Name="MenuButtonLayout"
    AutomationId="MenuButton"
    AutomationProperties.IsInAccessibleTree="True"
    SemanticProperties.Description="Menu container"
    Padding="0,0,5,0">
    <Image
        x:Name="MenuImage"
        HeightRequest="20"
        HorizontalOptions="Start"
        SemanticProperties.Description="Menu image"
        Source="dotnet_bot.png"
        WidthRequest="20" />

    <Label
        x:Name="MenuLabel"
        Margin="5,0,0,0"
        Text="Menu label"
        VerticalTextAlignment="Center" />
    <HorizontalStackLayout.GestureRecognizers>
        <TapGestureRecognizer Tapped="TapGestureRecognizer_OnTapped" />
    </HorizontalStackLayout.GestureRecognizers>
</HorizontalStackLayout>
```

When you only use `IsInaccessibleTree="True"` the following descriptions will be read by the screen reader:

- iOS: "Button"
- Android: "Menu image, menu label, double tap to activate"

When you also provide `SemanticProperties.Description="Menu container"`, the descriptions will be:

- iOS: "Menu container, Button"
- Android: "Menu container, double tap to activate"
