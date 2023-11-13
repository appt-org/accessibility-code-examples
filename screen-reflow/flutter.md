# Reflow - Flutter

In Flutter, all elements should be placed in a scalable widget, such as [`SingleChildScrollView`](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) or [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html). These widgets ensures that underlying widgets will become scrollable, in case they do not fit on the screen.

```dart
SingleChildScrollView(
  child: Text(
    'Content should scroll!',
    softWrap: true,
    overflow: TextOverflow.visible,
  ),
)
```
