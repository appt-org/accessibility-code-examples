# Scale text - Flutter

Flutter automatically scales the text on the screen to the text size set by the user. We recommend using [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html) to use the same text sizes and fonts everywhere.

Try to avoid using the `textScaleFactor` property because it overrides the text scale factor preferred by the user. The default factor is `1.0`, but can go as high as `4.0` for some users. Restricting the number means that some users might not be able to read the text.

There are valid use cases to restrict the `textScaleFactor` to a certain number. You can use [`MediaQuery`](https://api.flutter.dev/flutter/widgets/MediaQuery-class.html) to override the value globally. You can also override it for a single use case by using the property inside a [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) widget.

```dart
MediaQuery(
  data: MediaQuery.of(context).copyWith(
    textScaleFactor: 1.0, // Override scale for all widgets
  ),
  child: ...,
);

Text(
  'Appt', 
  textScaleFactor: 1.0, // Override scale for a single widget
);
```
