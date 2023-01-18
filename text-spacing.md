# Text spacing

Content should adapt to increased spacing between lines, words, letters, and paragraphs. This helps users with effectively reading text.

## WCAG

Relates to 1.4.12

## Android

On Android, you can use the following attribute to increase text spacing:

- [`letterSpacing`](https://developer.android.com/reference/android/widget/TextView#attr_android:letterSpacing): set spacing between letters
- [`lineHeight`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineHeight): set spacing between lines
- [`lineSpacingExtra`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineSpacingExtra): increase spacing between lines
- [`lineSpacingMultiplier`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineSpacingMultiplier): multiply spacing between lines
- [`marginBottom`](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams#attr_android:layout_marginBottom): set spacing between paragraphs

```xml
<TextView
    android:text="Appt"
    android:letterSpacing="3sp"
    android:lineHeight="20sp"
    android:lineSpacingExtra="5sp"
    android:lineSpacingMultiplier="1.5"
    android:layout_marginBottom="20dp"/>
```

## iOS

On iOS, you can use [`NSMutableParagraphStyle`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle) for paragraphs:

- [`lineSpacing`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1528742-linespacing): set spacing between lines
- [`lineHeightMultiple`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524596-lineheightmultiple): multiply distance between lines by a number
- [`paragraphSpacing`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1532528-paragraphspacing): set spacing between paragraphs

To adjust the spacing between letters you can use the [`NSKernAttributeName`](https://developer.apple.com/documentation/uikit/nskernattributename) attribute.

```swift
let style = NSMutableParagraphStyle()
style.lineSpacing = 20
style.lineHeightMultiple = 1.5
style.paragraphSpacing = 20

let attributedString = NSAttributedString(string: "Appt", attributes: [
    .paragraphStyle:  style,
    .kern: 3.0
])
element.attributedText = attributedString
```

## Flutter

With Flutter, it is possible to set spacing in text with [`TextStyle`](https://api.flutter.dev/flutter/painting/TextStyle-class.html). This can be done globally in the [`ThemeData`](https://api.flutter.dev/flutter/material/ThemeData-class.html) or within a [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) via the `style` parameter.

With the `TextStyle` class you can use the following attributes for spacing in the text:

- [`height`](https://api.flutter.dev/flutter/painting/TextStyle/height.html): set spacing between lines.
- [`letterSpacing`](https://api.flutter.dev/flutter/painting/TextStyle/letterSpacing.html): set extra spacing between letters.
- [`wordSpacing`](https://api.flutter.dev/flutter/painting/TextStyle/wordSpacing.html): adds extra spacing to whitespace.

```dart
TextStyle(
  height: 1.5,
  letterSpacing: 3.0,
  wordSpacing: 5.0
);
```

## React Native

React Native has a couple of attributes to adjust text spacing:

- [`letterSpacing`](https://reactnative.dev/docs/text-style-props#letterspacing): set spacing between letters
- [`lineHeight`](https://reactnative.dev/docs/text-style-props#lineheight): set spacing between lines
- [`paddingVertical`](https://reactnative.dev/docs/layout-props#paddingvertical): set spacing between paragraphs

```jsx
<Text style={{
  letterSpacing: 3,
  lineHeight: 32,
  paddingVertical: 6
}}>Appt</Text>
```

## Xamarin

Xamarin Forms has a couple of attributes to adjust text spacing:

- [`CharacterSpacing`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.characterspacing?view=xamarin-forms): set spacing between characters.
- [`LineHeight`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.lineheight?view=xamarin-forms): set spacing between lines.
- [`Padding`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.padding?view=xamarin-forms): set padding between paragraphs

You can also make a `CustomRenderer` to use even more properties from native Android and iOS elements. For more information see:

- [Xamarin Forms Custom Renderers](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/)
- [Custom Renderer for Android](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/entry#creating-the-custom-renderer-on-android)
- [Custom Renderer for iOS](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/entry#creating-the-custom-renderer-on-ios)

```xml
<Label CharacterSpacing="3" LineHeight="32" Margin="10" Padding="10" />
```
