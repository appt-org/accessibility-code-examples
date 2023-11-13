# Adjustable timing - Flutter

In Flutter, a [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html) is often used display temporary messages. The display duration might be too short for people to read or hear the message.

We recommend displaying messages by using an [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html). Or, when using a `Snackbar`, you can set the duration to "`infinite`". Don't forget to add a close button for both options.

Also make sure that the use of time limits, e.g. by using [`Future.delayed()`](https://api.flutter.dev/flutter/dart-async/Future/Future.delayed.html), can be extended.

```dart
ScaffoldMessenger.of(context).showSnackBar(SnackBar(
  duration: const Duration(days: 1),
  content: Text('Appt'),
  action: SnackBarAction(
    label: 'Close',
    onPressed: () {
      ScaffoldMessenger.of(context).hideCurrentSnackBar();
    },
  ),
));
```
