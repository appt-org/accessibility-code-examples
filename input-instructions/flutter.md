# Input instructions - Flutter

In Flutter, you can use an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) to show instructions for a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html). You need to provide a `string` for the [`helperText`](https://api.flutter.dev/flutter/material/InputDecoration/helperText.html) property.

```dart
TextField(
  decoration: InputDecoration(
    helperText: 'Your password should be at least 8 characters.',
  ),
);
```
