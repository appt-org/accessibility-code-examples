# Dark mode

Dark mode darkens background colours and provides a more comfortable viewing experience in low light. This is essential for many visually impaired people since a light background colour can be painful or even impossible to look at for an extended period of time. But also people who have problems with their concentration, for example due to a brain disorder, benefit greatly from dark mode.

## WCAG

Relates to 1.4.3, 1.4.11

## Android

On Android, you can detect dark mode by checking if the [`uiMode`](https://developer.android.com/reference/android/content/res/Configuration#uiMode) configuration contains [`UI_MODE_NIGHT_MASK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_NIGHT_MASK).

By adding `-night` resources to your project you can let Android automatically pick the right resources. For example, add a `colors.xml` file inside a `values-night` folder to specify night mode colors.

```kotlin
fun Context.isInNightMode(): Boolean {
    val nightModeFlags = resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK
    return nightModeFlags == Configuration.UI_MODE_NIGHT_YES
}
```

## iOS

On iOS, you can detect dark mode by checking if the [`userInterfaceStyle`](https://developer.apple.com/documentation/uikit/uitraitcollection/1651063-userinterfacestyle) has been set to [`.dark`](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle/dark).

You can provide dark mode resources to let iOS automatically use the right resources. For example, inside `Assets.xcassets` you can add a `Dark` version for colors and images.

```swift
func isInDarkMode() -> Bool{
    if #available(iOS 12.0, *) {
        if UIScreen.main.traitCollection.userInterfaceStyle == .dark {
            return true
        }
    }
    return false
}
```

## Flutter

With Flutter, you can detect dark mode by checking if the [`platformBrightness`](https://api.flutter.dev/flutter/widgets/MediaQueryData/platformBrightness.html) has been set to [`Brightness.dark`](https://api.flutter.dev/flutter/dart-ui/Brightness.html#values).

When defining an `App`, you can define a `darkTheme` to letter Flutter automatically use dark mode resources.

```dart
import 'dart:ui';
import 'package:flutter/widgets.dart';

/// Dark mode extension
extension DarkMode on BuildContext {
  bool get isDarkMode {
    return MediaQuery.of(this).platformBrightness == Brightness.dark;
  }
}

/// Define dark theme
MaterialApp(
  themeMode: ThemeMode.system,
  theme: ThemeData(
    brightness: Brightness.light,
    primaryColor: Colors.red,
  ),
  darkTheme: ThemeData(
    brightness: Brightness.dark,
  ),
);
```

## React Native

With React Native, you can detect dark mode by checking if the [`Appearance.getColorScheme()`](https://reactnative.dev/docs/appearance#getcolorscheme) method returns `dark`.

When defining a [`ThemeProvider`](https://reactnativeelements.com/docs/customization/themprovider) you can return a different theme when dark mode is active.

```jsx
import { useColorScheme } from 'react-native';
import { ThemeProvider } from 'styled-components';

const darkTheme = {
    primary: "#f967e9",
};
    
const lighTheme = {
    primary: "#cc00b9"
};

const App: React.FC = () => {
    const scheme = useColorScheme();
    return (
    <ThemeProvider theme={scheme === 'dark' ? darkTheme : lightTheme}>
        {props.children}
    </ThemeProvider>
    );
}

export default App;
```

## Xamarin

With Xamarin, you can detect dark mode by checking if the [`RequestedTheme`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.application.requestedtheme?view=xamarin-forms) property equals [`OSAppTheme.Dark`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.osapptheme?view=xamarin-forms#fields).

In `XAML` you can use [`AppThemeBinding`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/xaml/markup-extensions/consuming#appthemebinding-markup-extension) to define different resources for dark mode.

```csharp
using Xamarin.Essentials;

OSAppTheme theme = Application.Current.RequestedTheme;
if (theme == OSAppTheme.Dark) {
    // Dark mode
}
```

```xml
<ContentPage>
    <StackLayout>
        <Label Text="This text is black in light mode and white in dark mode."
               TextColor="{AppThemeBinding Light=Black, Dark=White}" />
        <Image Source="{AppThemeBinding Light=logo_light.png, Dark=logo_dark.png}" />
    </StackLayout>
</ContentPage>
```
