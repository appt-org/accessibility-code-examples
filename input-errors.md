# Input errors

Users should be notified when they make input errors. Show a clear error message when data has been entered incorrectly. Furthermore, provide suggestions that help users to fix the error. It is important that error messages are also posted to users of assistive technologies.

## WCAG

Relates to 3.3.1, 3.3.3

## Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show an error message. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which makes showing error messages easier. Set [`setErrorEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setErrorEnabled(boolean)) to `true` and then set the error message by using the [`setError`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#seterror) method.

```kotlin
textView.setVisibility(View.VISIBLE)
textView.text = "Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000"

input.setErrorEnabled(true)
input.setError("Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000")
```

## iOS

On iOS, we recommend using an [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) to indicate an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You could also use a third party library to displaying instructions. Unfortunately, accessibility is often not considered in the implementations.

```swift
errorLabel.isHidden = false
errorLabel.text = "Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000"
```

## Flutter

With Flutter, you can set an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) on a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html) to indicate an error. Set the `errorText` property to the error message that should be displayed. To remove the error, set the `errorText` to `null`. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```dart
bool _hasError = false;

TextField(
  decoration: InputDecoration(
    labelText: 'Date of birth',
    helperText: _hasError ? 'Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000' : null,
  ),
);
```

## React Native

In React Native we recommend using a [`Text`](https://reactnative.dev/docs/text) component to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use a package for displaying errors, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`HelperText`](https://callstack.github.io/react-native-paper/docs/components/HelperText/) component which can be used for displaying errors. The type should be set to `error` for errors.

```jsx
<Text>Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000</Text>

<View>
  <TextInput label="Date of birth" value={text} onChangeText={onChangeText} />
  <HelperText type="error" visible={hasErrors()}>
    Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000
  </HelperText>
</View>
```

## Xamarin

In Xamarin.Forms, we recommend using a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```xml
<Label
    Text="Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000"
    IsVisible="{Binding IsValid}" />
```
