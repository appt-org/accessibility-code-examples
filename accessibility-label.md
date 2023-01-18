# Accessibility label

An accessibility label helps users of assistive technologies to identify elements on the screen. The accessibility label is conveyed to assistive technologies. Accessibility labels are announced by the screen reader and presented visually by voice control.

## WCAG

Relates to 1.1.1

## Android

On Android, you can use the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) attribute to set an accessibility label.

You can also pass any kind of [`Span`](https://developer.android.com/guide/topics/text/spans) for greater control over pronunciation. For example, you can set a language by using [`LocaleSpan`](https://developer.android.com/reference/android/text/style/LocaleSpan).

If another element is used to display the label, you can link the label by using the [`labelFor`](https://developer.android.com/reference/android/view/View#setLabelFor(int)) attribute.

```kotlin
// Set accessibility label
element.contentDescription = "Appt"

// Set accessibility label in Dutch language
val locale = Locale.forLanguageTag("nl-NL")
val localeSpan = LocaleSpan(locale)

val string = SpannableString("Appt")
string.setSpan(localeSpan, 0, string.length, Spanned.SPAN_INCLUSIVE_INCLUSIVE)

element.contentDescription = localeSpan

// Link visual label to field
textView.setLabelFor(R.id.editText)
```

## iOS

On iOS, you can use the [`accessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) property to set an accessibility label.

You can also use the [`attributedAccessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/2865944-accessibilityattributedlabel) property for greater control over pronunciation. For example, spell out each character with [`.accessibilitySpeechPunctuation`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620201-accessibilityspeechpunctuation) or set a language using [`.accessibilitySpeechLanguage`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage).

The accessibility label should be as short as possible, while still being intuitive. When long labels cannot be avoided, you should use [`accessibilityUserInputLabels`](https://developer.apple.com/documentation/objectivec/nsobject/3197989-accessibilityuserinputlabels) to provide alternative labels. The primary label is first in the array, optionally followed by alternative labels in descending order of importance.

If another element is used to display the label, you can link the label by setting [`isAccessibilityElement`](https://developer.apple.com/documentation/objectivec/nsobject/1615141-isaccessibilityelement) to `false` and setting [`accessibilityLabel`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619577-accessibilitylabel) to the `value` of the label.

```swift
// Set accessibility label
element.accessibilityLabel = "Appt"

// Set accessibility label with Dutch speech engine
element.attributedAccessibilityLabel = NSAttributedString(
  string: "Appt", 
  attributes: [.accessibilitySpeechLanguage: "nl-NL"]
)

// Set accessibility label for controls
element.accessibilityUserInputLabels = ["Appt", "Alternative"]

// Link visual label
label.isAccessibilityElement = false
element.accessibilityLabel = label.text
```

## Flutter

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

## React Native

In React Native, you can set an accessibility label by using the [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) prop.

```jsx
<Control
  accessibilityLabel="Appt" />
```

## Xamarin

In Xamarin Forms, you can set an accessibility label by using the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property.

If another element is used to display the label, the [`AutomationProperties.LabeledBy`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieslabeledby) property be used to link a label. Unfortunately, `LabeledBy` only works on Android.

As an alternative, you can link a label by setting [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree) to `false` and setting [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) the `value` of the label.

```xml
<Control 
  AutomationProperties.Name="Appt" />
```
