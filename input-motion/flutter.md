# Motion input - Flutter

With Flutter, packages like [`sensors_plus`](https://pub.dev/packages/sensors_plus) can be used to detect movement.

An event through sensors should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```dart
import 'package:sensors_plus/sensors_plus.dart';

accelerometerEvents.listen((AccelerometerEvent event) {
  // Provide alternative
});
```
