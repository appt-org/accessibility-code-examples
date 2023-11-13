# Accessibility state - Flutter

With Flutter, you can use [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate the accessibility state. The [`Semantics constructor`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html) contains all available options, such as `checked`, `enabled`, `hidden`, `selected` and `toggled`, among others.

```dart
Semantics(
  checked: true,
  enabled: true,
  hidden: true,
  selected: true,
  toggled: true,
  child: Widget(...)
);
```
