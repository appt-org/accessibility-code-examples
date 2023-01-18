# Text element

Always use text elements to display text, unless this is not possible due to styling, such as text logo's. Text elements give users the flexibility to adapt the size and font to their preference. The font size inside an image often scales to a limited extent, or not at all. Make sure not to constrain the height of text elements as it will cut off the text when font-scaling is applied.

## WCAG

Relates to 1.4.5

## Android

On Android, you should use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) or an equivalent element to display text.

```xml
<TextView android:text="Appt" />
```

## iOS

On iOS, you should use [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) or [`UITextView`](https://developer.apple.com/documentation/uikit/uitextview) or an equivalent element to display text.

```swift
let label = UILabel()
label.text = "Appt"
```

## Flutter

 With Flutter, you should use [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) or [`RichText`](https://api.flutter.dev/flutter/widgets/RichText-class.html) or an equivalent element to display text.

```dart
Text('Appt')
```

## React Native

With React Native, you should use [`Text`](https://reactnative.dev/docs/text) or an equivalent element to display text.

```jsx
<Text>Appt</Text>
```

## Xamarin

With Xamarin, you should use [`Label`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) or an equivalent element to display text.

```xml
<Label Text="Appt"/>
```
