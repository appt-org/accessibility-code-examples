# Accessibility focus - Flutter

Flutter does not have built-in support for changing accessibility focus. See [Flutter issue #59594](https://github.com/flutter/flutter/issues/59594) for more information.

You could implement your own [`platform channels`](https://docs.flutter.dev/development/platform-integration/platform-channels) to call the native Android and iOS methods to move accessibility focus.

Do not use `FocusNode` or `Semantics.focused`, these methods should only be used for keyboard or input focus.

```dart
Not available, contribute!
```
