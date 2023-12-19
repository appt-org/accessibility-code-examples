# Accessibility group - .NET MAUI

On .NET MAUI you can group items together either by setting **AutomationProperties.IsInAccessibleTree** to true or by setting **SemanticProperties.Description**.

```xml
<HorizontalStackLayout
    x:Name="MenuButtonLayout"
    AutomationId="MenuButton"
    AutomationProperties.IsInAccessibleTree="True"
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
If you only use ***IsInaccessibleTree="True"*** then on iOS it will read "Button". On Android however it will read "Menu image, menu label, double tap to activate".

After replacing ***AutomationProperties.IsInAccessibleTree="True"*** with ***SemanticProperties.Description="Menu container"*** it will read on iOS: "Menu container, Button" and on Android: "Menu container, double tap to activate".
