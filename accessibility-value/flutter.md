# Accessibility value - Flutter

With Flutter, you can set an accessibility value by using the `value` or `attributedValue` property of [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html).

When using the semantically correct element, you usually do not need to modify the accessibility value. For example, [`Slider`](https://api.flutter.dev/flutter/material/Slider-class.html), [`Switch`](https://api.flutter.dev/flutter/material/Switch-class.html) and [`CheckBox`](https://api.flutter.dev/flutter/material/Checkbox-class.html), and others automatically assign accessibiluty values.

It is also possible to set an `increasedValue` and `decreasedValue` or `attributedDecreasedValue` and `attributedIncreasedValue` to indicate what the value will become when the user decreases or increases the value.

Some widgets include additional methods, such as [`semanticFormatterCallback`](https://api.flutter.dev/flutter/material/Slider/semanticFormatterCallback.html).

```dart
Semantics(
  value: 'Custom',
  increasedValue: 'Custom + 1',
  decreasedValue: 'Custom - 1',
  child: Widget(),
);      
```
