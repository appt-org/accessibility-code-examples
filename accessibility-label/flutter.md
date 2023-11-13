# Accessibility label - Flutter

In Flutter, the [`semanticsLabel`](https://api.flutter.dev/flutter/widgets/Text/semanticsLabel.html) property is used as accessibility name.

You can also use the [`attributedLabel`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/attributedLabel.html) property for greater control over pronunciation. For example, spell out each character with [`SpellOutStringAttribute`](https://api.flutter.dev/flutter/dart-ui/SpellOutStringAttribute-class.html) or set a language using [`LocaleStringAttribute`](https://api.flutter.dev/flutter/dart-ui/LocaleStringAttribute-class.html).

For even more control, you can use the [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget. For example, if you want to ignore the semantics of underlaying widgets, you can set the [`excludeSemantics`](https://api.flutter.dev/flutter/widgets/Semantics/excludeSemantics.html) attribute to `true`.

```dart
Control(
  semanticsLabel: 'Appt'
)

Semantics(
  label: 'Appt',
  attributedLabel: AttributedString('Appt', attributes: [
    SpellOutStringAttribute(range: const TextRange(start: 0, end: 3))
  ]),
  excludeSemantics: true;
);
```
