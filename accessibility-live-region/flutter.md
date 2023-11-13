# Accessibility live region - Flutter

On Flutter, the [`liveRegion`](https://api.flutter.dev/flutter/semantics/SemanticsConfiguration/liveRegion.html) property can be used in [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate a live region. By default, the live region is `polite`: it queues announcements.

```dart
Semantics(
  liveRegion: true,
  child: Text('Appt live region')
);
```
