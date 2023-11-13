# Input predictable - Flutter

In Flutter, be careful when using [`onChanged`](https://api.flutter.dev/flutter/material/TextField/onChanged.html) callbacks. Do not trigger a change of context when text changes.

```dart
TextField(
  onChanged: (text) {
    // Do not change context
  },
),
```
