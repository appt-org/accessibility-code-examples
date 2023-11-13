# Scale text - Xamarin

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
