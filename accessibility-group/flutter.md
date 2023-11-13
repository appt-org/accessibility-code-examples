# Accessibility group - Flutter

On Flutter, there are multiple types of semantics to group accessibility elements. The [`excludeSemantics`](https://api.flutter.dev/flutter/widgets/Semantics/excludeSemantics.html) property can be used to override the semantics of all children. You can achieve similar behavior by using [`BlockSemantics`](https://api.flutter.dev/flutter/widgets/BlockSemantics-class.html).

```dart
Semantics(
  label: 'Appt group',
  excludeSemantics: true,
  child: Column(
        children: [
            Text('Appt'),
            Text('is a platform for accessibility')
        ]
    )
);
```
