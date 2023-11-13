# Text spacing - Flutter

With Flutter, it is possible to set spacing in text with [`TextStyle`](https://api.flutter.dev/flutter/painting/TextStyle-class.html). This can be done globally in the [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html) or within a [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) via the `style` parameter.

With the `TextStyle` class you can use the following attributes for spacing in the text:

- [`height`](https://api.flutter.dev/flutter/painting/TextStyle/height.html): set spacing between lines.
- [`letterSpacing`](https://api.flutter.dev/flutter/painting/TextStyle/letterSpacing.html): set extra spacing between letters.
- [`wordSpacing`](https://api.flutter.dev/flutter/painting/TextStyle/wordSpacing.html): adds extra spacing to whitespace.

```dart
TextStyle(
  height: 1.5,
  letterSpacing: 3.0,
  wordSpacing: 5.0
);
```
