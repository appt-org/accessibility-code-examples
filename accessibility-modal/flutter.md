# Accessibility modal - Flutter

On Flutter, the [`ModelBarrier`](https://api.flutter.dev/flutter/widgets/ModalBarrier-class.html) class takes accessibility into account. The [`barrierDismissable`](https://api.flutter.dev/flutter/widgets/ModalRoute/barrierDismissible.html) and [`barrierLabel`](https://api.flutter.dev/flutter/widgets/ModalRoute/barrierLabel.html) are used by assistive technologies. When `barrierDismissable` is set to false, the focus of assistive technologies is trapped inside the modal. The value of  `barrierLabel` is announced upon entering the modal.

```dart
showDialog(
    context: context,
    barrierDismissible: false,
    barrierLabel: 'Label'
    builder: (context) {
        return SimpleDialog(
            title: Text('Appt')
        );
    },
);
```
