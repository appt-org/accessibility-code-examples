# Add accessibility label

It is essential to add accessibility labels to help users of assistive technologies to identify elements on the screen.

## Android

On Android, you can use the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) property to add an accessibility label.

You can also pass any kind of [`Span`](https://developer.android.com/guide/topics/text/spans) for greater control. For example, set a language by using [`LocaleSpan`](https://developer.android.com/reference/android/text/style/LocaleSpan).

```kotlin
element.contentDescription = "Appt"

// LocaleSpan
val locale = Locale.forLanguageTag("nl-NL")
val localeSpan = LocaleSpan(locale)

val string = SpannableString("Appt")
string.setSpan(localeSpan, 0, string.length, Spanned.SPAN_INCLUSIVE_INCLUSIVE)

element.contentDescription = localeSpan
```

## iOS

On iOS, you can use the [`accessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) property to add an accessibility label.

You can also use the [`attributedAccessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/2865944-accessibilityattributedlabel) property for greater control. For example, spell out each character with [`.accessibilitySpeechPunctuation`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620201-accessibilityspeechpunctuation) or set a language using [`.accessibilitySpeechLanguage`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage).

```swift
element.accessibilityLabel = "Appt"

element.attributedAccessibilityLabel = NSAttributedString(
  string: "Appt", 
  attributes: [.accessibilitySpeechLanguage: "nl-NL"]
)
```

## Flutter

With Flutter, you can add an accessibility label by using the [`label`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/label.html) property provided by the [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget.

You can also use the [`attributedLabel`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/attributedLabel.html) property for greater control. For example, spell out each character with [`SpellOutStringAttribute`](https://api.flutter.dev/flutter/dart-ui/SpellOutStringAttribute-class.html) or set a language using [`LocaleStringAttribute`](https://api.flutter.dev/flutter/dart-ui/LocaleStringAttribute-class.html).

```dart
Semantics(
  label: 'Appt',
  attributedLabel: AttributedString('Appt', [...]);
);
```

## React Native

In React Native you can add an accessibility label by using the [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) prop.

```jsx
<Image
  source={require("appt.png")}
  accessible
  accessibilityLabel="Appt"
/>
```

## Xamarin

In Xamarin Forms you can add an accessibility label by using the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property.

```xml
<Image 
  AutomationProperties.Name="Appt" />
```
