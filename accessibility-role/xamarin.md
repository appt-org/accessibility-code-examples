# Accessibility role - Xamarin

Xamarin Forms does not have built-in support for setting an accessibility role.

By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour.

The [`SemanticEffect`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Effects/Semantic/SemanticEffect.shared.cs) file inside the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) defines various methods to set accessibility roles.

```xml
<controls:CustomFontLabel
    xct:SemanticEffect.HeadingLevel="1"
    xct:SemanticEffect.Description="Button" />
```
