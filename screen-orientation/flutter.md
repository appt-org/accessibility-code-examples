# Screen orientation - Flutter

With Flutter, multiple screen orientations are enabled by default.

Orientation can be locked by using the [`setPreferredOrientations`](https://api.flutter.dev/flutter/services/SystemChrome/setPreferredOrientations.html) method of [`SystemChrome`](https://api.flutter.dev/flutter/services/SystemChrome-class.html). Make sure to pass all [`DeviceOrientation`](https://api.flutter.dev/flutter/services/DeviceOrientation.html) values, or simply remove the code from your app.

By using an [`OrientationBuilder`](https://api.flutter.dev/flutter/widgets/OrientationBuilder-class.html) it is possible to make adjustments based on the orientation of the screen.

```dart
// Allow all orientations
SystemChrome.setPreferredOrientations([
  DeviceOrientation.portraitUp,
  DeviceOrientation.portraitDown,
  DeviceOrientation.landscapeRight,
  DeviceOrientation.landscapeLeft
]);

// Listen to orientation changes
OrientationBuilder(
  builder: (context, orientation) {
    return GridView.count(
      // Grid with 2 columns in portrait and 3 columns in landscape
      crossAxisCount: orientation == Orientation.portrait ? 2 : 3,
    );
  },
),
```
