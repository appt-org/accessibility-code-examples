# Accessibility dialog - Flutter

With Flutter, you can use [`SimpleDialog`](https://api.flutter.dev/flutter/material/SimpleDialog-class.html), [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html) or [`CupertinoAlertDialog`](https://api.flutter.dev/flutter/cupertino/CupertinoAlertDialog-class.html) to show alerts. An `AlertDialog` is styled liked an Android dialog. A `CupertinoAlertDialog` is styled like an iOS dialog. You should always supply a close action in the `actions` array. The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```dart
showDialog(
  context: context,
  builder: (context) => AlertDialog(
    title: Text('Confirm Appt membership?'),
    content: Text('Your bank account will be billed.'),
    actions: [
      TextButton(
        onPressed: confirmTransaction,
        child: const Text('Proceed'),
      ),
      TextButton(
        onPressed: () => Navigator.pop(context),
        child: const Text('Cancel'),
      )
    ],
  ),
);
```
