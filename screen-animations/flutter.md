# Reduced animations - Flutter

With Flutter, you can use [`MediaQuery.of(context)`](https://api.flutter.dev/flutter/widgets/MediaQuery/of.html) to retrieve the value of [`disableAnimations`](https://api.flutter.dev/flutter/widgets/MediaQueryData/disableAnimations.html). If the value is `true`, you could choose to disable (non-essential) animations in your app.

```dart
if (MediaQuery.of(this).disableAnimations) {
    // Disable animations
}
```
