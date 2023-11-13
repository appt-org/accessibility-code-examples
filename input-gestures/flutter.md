# Input gestures - Flutter

In Flutter, the [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html) class is a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```dart
double _baseScaleFactor = 1;
double _scaleFactor = 1;

GestureDetector(
  onScaleStart: (details) {
    _baseScaleFactor = _scaleFactor;
  },
  onScaleUpdate: (details) {
    setState(() {
      _scaleFactor = _baseScaleFactor * details.scale;
      // Provide alternative
    });
  },
  child: ...
  ),
);
```
