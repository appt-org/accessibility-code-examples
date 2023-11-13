# Text spacing - Xamarin

Xamarin Forms has a couple of attributes to adjust text spacing:

- [`CharacterSpacing`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.characterspacing?view=xamarin-forms): set spacing between characters.
- [`LineHeight`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.lineheight?view=xamarin-forms): set spacing between lines.
- [`Padding`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.padding?view=xamarin-forms): set padding between paragraphs

You can also make a `CustomRenderer` to use even more properties from native Android and iOS elements. For more information see:

- [Xamarin Forms Custom Renderers](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/)
- [Custom Renderer for Android](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/entry#creating-the-custom-renderer-on-android)
- [Custom Renderer for iOS](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/entry#creating-the-custom-renderer-on-ios)

```xml
<Label CharacterSpacing="3" LineHeight="32" Margin="10" Padding="10" />
```
