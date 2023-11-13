# Accessibility live region - Xamarin

Xamarin Forms does not have built-in support to indicate an accessibility live region. By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour. The [`A11YEffect`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect.md), [`A11YEffect for Android`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_Android.md) and [`A11YEffect for iOS`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_iOS.md) files show how to implement an `effect` to replicate an accessibility live region.

```xml
<controls:CustomFontLabel
    effects:A11YEffect.ControlType="{OnPlatform iOS=LiveUpdate, Android=LiveUpdate}" />
```
