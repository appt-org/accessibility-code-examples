# Accessibility announcement - Flutter

With Flutter, you can post an accessibility message by using the [`SemanticsService`](https://api.flutter.dev/flutter/semantics/SemanticsService-class.html) object. Use the [`announce`](https://api.flutter.dev/flutter/semantics/SemanticsService/announce.html) method to post an accessibility announcement.

```dart
SemanticsService.announce('Appt announcement', TextDirection.ltr);
```
