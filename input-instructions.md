# Input instructions

When a label might not describe the requested input sufficiently, you should add additional instructions. For example, if passwords are required to be at least 8 characters, indicate this to users.

## WCAG

Relates to 3.3.2

## Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show instructions.

You can also use a [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which contains a  [`setHelperText`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHelperText(java.lang.CharSequence)) method to provide instructions. To show instructions, you need to set [`setHelperTextEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHelperTextEnabled(boolean)) to `true`.

```kotlin
input.setHelperTextEnabled(true)
input.setHelperText("Your password should be at least 8 characters.")
```

## iOS

On iOS, we recommend using an [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) to indicate an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You could also use a third party library to displaying instructions. Unfortunately, accessibility is often not considered in the implementations.

```swift
helpLabel.isHidden = false
helpLabel.text = "Your password should be at least 8 characters."
```

## Flutter

In Flutter, you can use an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) to show instructions for a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html). You need to provide a `string` for the [`helperText`](https://api.flutter.dev/flutter/material/InputDecoration/helperText.html) property.

```dart
TextField(
  decoration: InputDecoration(
    helperText: 'Your password should be at least 8 characters.',
  ),
);
```

## React Native

In React Native, there is no default component to combine an input field with a label. We recommend combining [`Text`](https://reactnative.dev/docs/text) with a [`TextInput`](https://reactnative.dev/docs/textinput) component.

You can also use a package for displaying instructions, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`HelperText`](https://callstack.github.io/react-native-paper/docs/components/HelperText/) component which can be used for displaying instructions. The type should be set to `info` for instructions.

```jsx
<Text>Your password should be at least 8 characters.</Text>

<View>
  <TextInput label="Password" value={text} onChangeText={onChangeText} />
  <HelperText type="info">
    Your password should be at least 8 characters.
  </HelperText>
</View>
```

## Xamarin

In Xamarin.Forms, we recommend using a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to display instructions.

```xml
<Label Text="Your password should be at least 8 characters." />
```
