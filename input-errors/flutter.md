# Input errors - Flutter

With Flutter, you can set an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) on a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html) to indicate an error. Set the `errorText` property to the error message that should be displayed. To remove the error, set the `errorText` to `null`. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```dart
bool _hasError = false;

TextField(
  decoration: InputDecoration(
    labelText: 'Date of birth',
    helperText: _hasError ? 'Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000' : null,
  ),
);
```
