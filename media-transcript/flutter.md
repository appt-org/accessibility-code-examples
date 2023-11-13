# Transcript - Flutter

With Flutter, you can use [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) to display written text. Make sure to wrap the `Text` widget in a [`SingleChildScrollView`](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) and to set the overflow parameter to `TextOverflow.visible`. Also, the `softwrap` parameter needs to be set to true to prevent the text from overflowing outside its container.

```dart
SingleChildScrollView(
  child: Text(
    'Appt transcript',
    softWrap: true,
    overflow: TextOverflow.visible,
  ),
)
```
