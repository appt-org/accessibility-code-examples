# Accessibility role - Flutter

For some widgets in Flutter, the role is assignd automatically. This happens, for example, with Flutter's buttons and text fields. If this is not the case, you can use [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate a role. The [`Semantics constructor`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html) contains all available options, such as `button`, `header`, `link` and `image`, among others.

```dart
Semantics(
  button: true,
  header: true,
  link: true,
  image: true,
  child: Widget(...)
);
```
