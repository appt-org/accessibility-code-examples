# Input label

Input fields should have labels so that users know what input data is expected. These labels should stay visible while users are entering data. A placeholder which disappears while entering data does not count as a label.

## WCAG

Relates to 3.3.2

## Android

On Android, you can link labels to controls by using the [`labelFor`](https://developer.android.com/reference/android/view/View#setLabelFor(int)) attribute. We recommend using a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show labels for input fields.

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which allows you to create an input field with a label. The [`hint`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHint(java.lang.CharSequence)) property at the `TextInputLayout` level is used as visual `label`. The [`hintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHintEnabled(boolean)) and [`expandedHintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setExpandedHintEnabled(boolean)) properties must be set to `true` to always show the label.

```xml
<TextView android:text="Name" android:labelFor="@+id/field"/>
<EditText id="@+id/field" hint="Enter your name"/>

<com.google.android.material.textfield.TextInputLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:hintEnabled="true"
    app:expandedHintEnabled="true"
    android:hint="Name">

    <com.google.android.material.textfield.TextInputEditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name"/>
</com.google.android.material.textfield.TextInputLayout>
```

## iOS

On iOS, there is no attribute to link a label to an input field. We recommend combining [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) with a [`UITextField`](https://developer.apple.com/documentation/uikit/uitextfield). Set `isAccessibilityElement` to `false` for the label, and set the text of the label as `accessibilityLabel` for the field.

```swift
label.text = "Name"
label.isAccessibilityElement = false
field.accessibilityLabel = label.text
```

## Flutter

In Flutter, there is no attribute to link a label to an input field. You can use an [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html) to show a label for a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html). You need to provide a [`Text`](https://docs.flutter.dev/development/ui/widgets/text) widget for the `label` property.

```dart
TextField(
    decoration: InputDecoration(
        label: Text('Name')
    ),
);
```

## React Native

In React Native, there is no attribute to link a label to an input field. We recommend combining [`Text`](https://reactnative.dev/docs/text) with a [`TextInput`](https://reactnative.dev/docs/textinput) component.

You can also use a package for displaying instructions, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`TextInput`](https://callstack.github.io/react-native-paper/docs/components/TextInput/) component with a `label` property.

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

In Xamarin, you can use the [`AutomationProperties.LabeledBy`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieslabeledby) property to link a label to an input field. However, `LabeledBy` only works on Android.

You can also link a [`Label`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label) to an [`Entry`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/entry) by setting [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree) to `false` on the label, and setting [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property to the value of the label.

```xml
<Label x:Name="label" 
       Text="Name" 
       AutomationProperties.IsInAccessibleTree="false" />

<Entry AutomationProperties.Name="{x:Reference label}"
       AutomationProperties.LabeledBy="{x:Reference label}" />
```
