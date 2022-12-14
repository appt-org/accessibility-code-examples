# Input label

Input fields should have labels so that users know what input data is expected. These labels should stay visible while users are entering data. A placeholder which disappears while entering data does not count as a label.

## Android

On Android, we recommend using a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show labels for input fields.

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which allows you to create an input field with a label. The [`hint`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHint(java.lang.CharSequence)) property is used as a label. The [`hintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHintEnabled(boolean)) and [`expandedHintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setExpandedHintEnabled(boolean)) properties must be set to `true` to always show the label.

```xml
<TextView android:text="Name">

<com.google.android.material.textfield.TextInputLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:hintEnabled="true"
    app:expandedHintEnabled="true">

    <com.google.android.material.textfield.TextInputEditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Name"/>
</com.google.android.material.textfield.TextInputLayout>
```

## iOS

On iOS, there is no default component to combine an input field with a label. We recommend combining [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) with a [`UITextField`](https://developer.apple.com/documentation/uikit/uitextfield). Set `isAccessibilityElement` to `false` for the label, and set the text of the label as `accessibilityLabel` for the field.

```swift
label.text = "Name"
label.isAccessibilityElement = false
field.accessibilityLabel = label.text
```

## Flutter

In Flutter, you can use an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) to show a label for a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html). You need to provide a [`Text`](https://docs.flutter.dev/development/ui/widgets/text) widget for the `label` property.

```dart
TextField(
    decoration: InputDecoration(
        label: Text('Name')
    ),
);
```

## React Native

In React Native, there is no default component to combine an input field with a label. We recommend combining [`Text`](https://reactnative.dev/docs/text) with a [`TextInput`](https://reactnative.dev/docs/textinput) component.

You can also use a package for displaying instructions, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`TextInput`](https://callstack.github.io/react-native-paper/text-input.html) component with a `label` property.

```jsx
import { TextInput } from 'react-native-paper';

const InputWithLabelComponent = () => {
  return (
    <TextInput
      label="Name"
      value={name}
    />
  );
};
```

## Xamarin

In Xamarin, you can combine a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) and [`Entry`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/entry) by using the [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree)  and [`AutomationProperties.LabeledBy`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieslabeledby) properties.

```xml
<Label x:Name="label" Text="Name" />
<Entry AutomationProperties.IsInAccessibleTree="true"
       AutomationProperties.LabeledBy="{x:Reference label}" />
```
