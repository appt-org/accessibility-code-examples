# Accessibility language - Flutter

With Flutter, the `locale` parameter of [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) or [`TextSpan`](https://api.flutter.dev/flutter/painting/TextSpan-class.html) can be used to specify the locale for a piece of text. Multiple `TextSpan` elements can be combined to speak content in multiple languages.

```dart
/// Text implementation
Text(
  'Appt',
  locale: Locale.fromSubtags(languageCode: 'nl'),
);

/// TextSpan implementation
TextSpan(
  text: 'Appt',
  locale: Locale.fromSubtags(languageCode: 'nl'),
);
```
