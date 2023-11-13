# Dark mode - Flutter

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
