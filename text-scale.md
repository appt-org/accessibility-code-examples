# Scale text

Apps should scale text to the size specified by users in the system settings. This is especially important for visually impaired users because they might not be able to read the text otherwise.

## WCAG

Relates to 1.4.4

## Android

On Android, you can use [Scale-independent Pixels](https://developer.android.com/guide/topics/resources/more-resources.html#Dimension) to scale text. This unit ensures that the user's preferences are taken into account when determining the font size. We recommend to define the [`textSize`](https://developer.android.com/reference/android/widget/TextView#attr_android:textSize) in your styles to make sure it's the same everywhere.

```xml
<style name="Widget.TextView">
    <item name="android:textSize">18sp</item>
</style>
```

## iOS

On iOS, you can use [Dynamic Font Size](https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically) to scale text. By using this function, the font size is adjusted to the preferences of the user. If you're using your own font, you can use the [`scaledFont`](https://developer.apple.com/documentation/uikit/uifontmetrics/2877385-scaledfont) method from [`UIFontMetrics`](https://developer.apple.com/documentation/uikit/uifontmetrics) to calculate the font size.

```swift
import UIKit

extension UIFont {

    static func font(name: String, size: CGFloat, style: TextStyle) -> UIFont {
        guard let font = UIFont(name: name, size: size) else {
            fatalError("Font \(name) does not exist")
        }
        return UIFontMetrics(forTextStyle: style).scaledFont(for: font)
    }
    
    static func openSans(weight: UIFont.Weight, size: CGFloat, style: TextStyle) -> UIFont {
        if UIAccessibility.isBoldTextEnabled {
            return font(name: "OpenSans-Bold", size: size, style: style)
        }
        
        switch weight {
            case .regular:
                return font(name: "OpenSans-Regular", size: size, style: style)
            case .semibold:
                return font(name: "OpenSans-SemiBold", size: size, style: style)
            case .bold:
                return font(name: "OpenSans-Bold", size: size, style: style)
            default:
                fatalError("Font weight \(weight) is not supported")
        }
    }
}
```

## Flutter

Flutter automatically scales the text on the screen to the text size set by the user. We recommend using [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html) to use the same text sizes and fonts everywhere.

Try to avoid using the `textScaleFactor` property because it overrides the text scale factor preferred by the user. The default factor is `1.0`, but can go as high as `4.0` for some users. Restricting the number means that some users might not be able to read the text.

There are valid use cases to restrict the `textScaleFactor` to a certain number. You can use [`MediaQuery`](https://api.flutter.dev/flutter/widgets/MediaQuery-class.html) to override the value globally. You can also override it for a single use case by using the property inside a [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) widget.

```dart
MediaQuery(
  data: MediaQuery.of(context).copyWith(
    textScaleFactor: 1.0, // Override scale for all widgets
  ),
  child: ...,
);

Text(
  'Appt', 
  textScaleFactor: 1.0, // Override scale for a single widget
);
```

## React Native

React Native automatically scales text depending on the font size preferences of the user settings. In addition, all dimensions in React Native are unitless, and represent density-independent pixels.

Try to avoid using properties such as [`maxFontSizeMultiplier`](https://reactnative.dev/docs/text#maxfontsizemultiplier), [`allowFontScaling`](https://reactnative.dev/docs/text#allowfontscaling), [`adjustsFontSizeToFit`](https://reactnative.dev/docs/text#adjustsfontsizetofit) and [`numberOfLines`](https://reactnative.dev/docs/text#numberoflines). Using these properties may cause text to be unscalable or become inaccessible.

When inheriting a project you may find previous developers have disabled font-scaling with the following code: `Text.defaultProps.allowFontScaling = false;`. This is accessibility anti-pattern and should be rolled back.

The code example below shows how to have a scaling font size.

```jsx
<Text style={{ fontSize: 16 }}>
    Appt
</Text>
```

## Xamarin

In Xamarin Forms you make styles for the scalable fonts that you use in your app. 

First, accessibility scaling should be enabled for named font sizes. This can be done by pass `True` to the the [`SetEnableAccessibilityScalingForNamedFontSizes`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.platformconfiguration.iosspecific.application.setenableaccessibilityscalingfornamedfontsizes?view=xamarin-forms#xamarin-forms-platformconfiguration-iosspecific-application-setenableaccessibilityscalingfornamedfontsizes(xamarin-forms-bindableobject-system-boolean)) method of the [`Application`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.platformconfiguration.iosspecific.application?view=xamarin-forms). This can also be done in XAML by using `ios:Application.EnableAccessibilityScalingForNamedFontSizes="true"`.

Secondly, you have to register the font and it's properties with the assembly. Afterwards, the fonts can be used in your app and they will automatically scale depending on the users' font size preference.

For more information, see [Understand named font sizes](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/fonts#understand-named-font-sizes), [Named font size scaling](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/platform/ios/named-font-size-scaling) and [Dynamic Styles](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/styles/xaml/dynamic).

The code examples below shows how to enable font size scaling and how to use dynamic styles.

```csharp
using Xamarin.Forms;

[assembly: ExportFont("Lobster-Regular.ttf", Alias="Lobster")]
[assembly: ExportFont("Lobster-Bold.ttf", Alias="LobsterBold")]

namespace Project
{
    public partial class App : Xamarin.Forms.Application
    {
        On<Xamarin.Forms.PlatformConfiguration.iOS>().SetEnableAccessibilityScalingForNamedFontSizes(true);
    }
}
```

```xml
<Application
    xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
    ios:Application.EnableAccessibilityScalingForNamedFontSizes="true">
</Application>

<Style TargetType="Entry">
    <Setter Property="FontFamily" Value="Lobster" />
</Style>

<Style
    x:Key="LabelRegular"
    ApplyToDerivedTypes="True"
    BaseResourceKey="BodyStyle"
    TargetType="Label">
    <Setter Property="TextColor" Value="Black" />
    <Setter Property="FontFamily" Value="Lobster" />
    <Setter Property="FontSize" Value="{DynamicResource Body}" />
    <!--  For Android you have to set FontSize property -->
</Style>

<Style
    x:Key="LabelBold"
    ApplyToDerivedTypes="True"
    BaseResourceKey="LabelRegular"
    TargetType="Label">
    <Setter Property="FontFamily" Value="LobsterBold" />
    <Setter Property="FontAttributes">
</Style>
```
