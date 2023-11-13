# Text truncation - Flutter

In Flutter, you can avoid text truncation by removing all instances of [`maxLines`](https://api.flutter.dev/flutter/widgets/Text/maxLines.html) from your app. You should also set [`overflow`](https://api.flutter.dev/flutter/widgets/Text/overflow.html) to [`TextOverflow.visible`](https://api.flutter.dev/flutter/painting/TextOverflow.html#visible)  where needed. Lastly, avoid using fixed values for any heights or widths.

```dart
Text(
    'Avoid text truncation',
    maxLines: REMOVE,
    overflow: TextOverflow.visible
)
```
