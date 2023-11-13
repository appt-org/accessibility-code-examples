# Accessibility action - Flutter

With Flutter, you can use [`CustomSemanticsAction`](https://api.flutter.dev/flutter/semantics/CustomSemanticsAction/CustomSemanticsAction.html) to add custom actions for assistive technologies. To implement specific functionality for assistive technologies it is also possible to add `onTap`, `onLongPress` or other callbacks to the `Semantics` widget. When you do this, it is important to make sure the child nodes do not implement a touch listener, or to use `excludeSemantics` to ignore these with the assistive technologies.

```dart
Semantics(
    customSemanticsActions: <CustomSemanticsAction, VoidCallback>{
        CustomSemanticsAction(label: 'Increment'): _incrementCounter,
    },
    onTap: () {
        _incrementCounter
    },
    excludeSemantics: true,
    child: TextButton(...)
);
```
