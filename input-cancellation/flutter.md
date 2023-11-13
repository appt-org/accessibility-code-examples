# Input cancellation - Flutter

On Flutter, be careful when using a [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html) Avoid using events such as `onDown`, like `onTapDown` and `onLongPressDown`, because users will not be able to cancel their interaction. Use `onAction` events such `onTap` or `onLongPress` instead, because these have built-in support for cancellation.

```dart
@override
Widget build(BuildContext context) {
    return new GestureDetector(
        onDown: ... // Use onTap instead
    );
}
```
