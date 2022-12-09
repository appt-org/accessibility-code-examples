# Input error

Users should be notified when they make input errors. Show a clear error message when data has been entered incorrectly. It is important that error messages are also posted to users of assistive technologies.

## Android

On Android, we recommend using a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show an error message. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which makes showing error messages easier. Set [`setErrorEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setErrorEnabled(boolean)) to `true` and then set the error message by using the [`setError`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#seterror) method.

```kotlin
textView.setVisibility(View.VISIBLE)
textView.text = "You are required to fill in your name"

input.setErrorEnabled(true)
input.setError("You are required to fill in your name")
```

## iOS

On iOS, we recommend using an [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) to indicate an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

There are also third party libraries available for displaying error messages. Unfortunately, accessibility is often not considered in the implementations.

```swift
errorLabel.isHidden = false
errorLabel.text = "You are required to fill in your name"
```

## Flutter

With Flutter, you can set an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) on a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html) to indicate an error. Set the `errorText` property to the error message that should be displayed. To remove the error, set the `errorText` to `null`. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```dart
String? errorText;

void nameIsNotEmpty(String? email) {
  setState(() {
    if (name == null || name.isEmpty) {
      errorText = 'You are required to fill in your name';
    }
    errorText = null;
  });
}

@override
Widget build(BuildContext context) {
  return TextField(
    onChanged: nameIsNotEmpty,
    decoration: InputDecoration(
        labelText: 'Enter your name',
        hintText: 'This is a required field',
        errorText: errorText
    ),
  );
}
```

## React Native

In React Native we recommend using a [`Text`](https://reactnative.dev/docs/text) component to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use a third party library such as [`HelperText`](https://callstack.github.io/react-native-paper/helper-text.html), which makes it easier to display error states.

```jsx
<Text>You are required to fill in your name</Text>

<View>
  <TextInput label="Email" value={text} onChangeText={onChangeText} />
  <HelperText type="error" visible={hasErrors()}>
    E-mail address is invalid!
  </HelperText>
</View>
```

## Xamarin

In Xamarin.Forms, we recommend using a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

```xml
<Label
    Text="{Binding ErrorText}"
    IsVisible="{Binding IsValid}" />
```
