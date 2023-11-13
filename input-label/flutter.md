# Input label - Flutter

In Flutter, there is no attribute to link a label to an input field. You can use an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) to show a label for a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html). You need to provide a [`Text`](https://docs.flutter.dev/development/ui/widgets/text) widget for the `label` property.

```dart
TextField(
    decoration: InputDecoration(
        label: Text('Name')
    ),
);
```
