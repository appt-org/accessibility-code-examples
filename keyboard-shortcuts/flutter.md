# Keyboard shortcuts - Flutter

With Flutter, you can use the [`RawKeyboard`](https://api.flutter.dev/flutter/services/RawKeyboard-class.html) listener to implement shortcuts in your app. The `RawKeyboard` listener yields a [`RawKeyUpEvent`](https://api.flutter.dev/flutter/services/RawKeyUpEvent-class.html) of a [`RawKeyDownEvent`](https://api.flutter.dev/flutter/services/RawKeyDownEvent-class.html). The `data` attribute has a `isModifierPressed()` method that can be used to determine whether a modifier key has been pressed.

```dart
RawKeyboard.instance.addListener((keyEvent) {
  if (keyEvent is RawKeyUpEvent) {
    if (keyEvent.logicalKey == LogicalKeyboardKey.keyF &&
        keyEvent.data.isModifierPressed(ModifierKey.controlModifier)) {
      find();
    }
  }
});

void find() {
    // Logic
}
```
