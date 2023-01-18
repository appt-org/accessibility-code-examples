# Accessibility language

When content is written in multiple languages, foreign words should ideally be indicated in their respective language. For example, you can indicate a French quote in a Dutch piece of content. This enables assistive technologies to use the right pronunciation.

## WCAG

Relates to 3.1.1

## Android

On Android, you can use [`LocaleSpan`](https://developer.android.com/reference/android/text/style/LocaleSpan) to speak content in a specific language. Multiple `LocaleSpan`'s can be embedded inside a [`SpannableString`](https://developer.android.com/reference/android/text/SpannableString) to speak content in multiple languages.

```kotlin
val locale = Locale.forLanguageTag("nl-NL")
val localeSpan = LocaleSpan(locale)

val string = SpannableString("Appt")
string.setSpan(localeSpan, 0, string.length, Spanned.SPAN_INCLUSIVE_INCLUSIVE)

element.setText(string)
```

## iOS

On iOS, the [`accessibilitySpeechLanguage`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage) key of [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring) can be used to speak content in a specific language. Multiple `NSAttributedString`'s can be embedded inside a [`NSMutableAttributedString`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring) to speak content in multiple languages.

In addition, the [`accessibilityLanguage`](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage) attribute of the [`UIAccessibility`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibility) protocol can be used to set a single language for an element. Many objects implement this protocol, such as [`UIApplication`](https://developer.apple.com/documentation/uikit/uiapplication/) and [`UIView`](https://developer.apple.com/documentation/uikit/uiview/).

```swift
element.attributedText = NSAttributedString(
    string: "Appt", 
    attributes: [.accessibilitySpeechLanguage: "nl_NL"]
)

application.accessibilityLanguage = "nl_NL"
view.accessibilityLanguage = "nl_NL"
```

## Flutter

With Flutter, the `locale` parameter of [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) or [`TextSpan`](https://api.flutter.dev/flutter/painting/TextSpan-class.html) can be used to specify the locale for a piece of text. Multiple `TextSpan` elements can be combined to speak content in multiple languages.

```dart
/// Text implementation
Text(
  'Appt',
  locale: Locale.fromSubtags(languageCode: 'nl'),
);

/// TextSpan implementation
TextSpan(
  text: 'Appt',
  locale: Locale.fromSubtags(languageCode: 'nl'),
);
```

## React Native

In React Native, there is limited support to change the accessibility language. The [`accessibilityLanguage`](https://reactnative.dev/docs/text#accessibilitylanguage-ios) prop of [`Text`](https://reactnative.dev/docs/text) only works on iOS. Multiple `Text` elements can be combined to speak content in multiple languages.

```jsx
<Text>
  <Text accessibilityLanguage="nl-NL">Appt</Text>
  <Text>is an accessibility platform.</Text>
</Text>
```

## Xamarin

Unfortunately, Xamarin Forms does not have support for changing the accessibility language. When you use HTML such as `<span lang="nl">Appt</span>` inside a [`Label`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label), the [`lang`](https://www.w3schools.com/tags/att_global_lang.asp) attribute is not used. You can create a component with a custom renderer with native Android and iOS logic. If you have done this, please contribute code.

```csharp
Not available, contribute!
```
