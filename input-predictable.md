# Input predictable

Whenever a user provides input, there should be no change of `context`. Example of changing context include, but are not limited to: automatically submitting data, opening a new screen or moving to another element. Input should have predictable effects.

## WCAG

Relates to 3.2.2

## Android

On Android, be careful when using [`TextWatcher`](https://developer.android.com/reference/android/text/TextWatcher) methods. Do not trigger a change of context when text changes.

```kotlin
private val textWatcher = object : TextWatcher {
  override fun afterTextChanged(s: Editable?) {
    // Ignored
  }

  override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
    // Ignored
  }

  override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
    // Do not change context
  }
}
```

## iOS

With iOS, be careful when using [`UITextFieldDelegate`](https://developer.apple.com/documentation/uikit/uitextfielddelegate) methods. Do not trigger a change of context when text changes.

```swift
extension ApptViewController: UITextFieldDelegate {
  func textField(_ textField: UITextField,
                  shouldChangeCharactersIn range: NSRange,
                  replacementString string: String) -> Bool {
      // Do not change context
      return true
  }
}
```

## Flutter

In Flutter, be careful when using [`onChanged`](https://api.flutter.dev/flutter/material/TextField/onChanged.html) callbacks. Do not trigger a change of context when text changes.

```dart
TextField(
  onChanged: (text) {
    // Do not change context
  },
),
```

## React Native

In React Native, be careful when using [`onChange`](https://reactnative.dev/docs/next/textinput#onchange) or [`onChangeText`](https://reactnative.dev/docs/textinput#onchangetext) callbacks. Do not trigger a change of context when text changes.

```jsx
<TextInput 
  onChangeText={ /* Do not change context */ }
/>
```

## Xamarin

In Xamarin, be careful when using [`TextChanged`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.inputview.textchanged?view=xamarin-forms) callbacks. Do not trigger a change of context when text changes.

```csharp
entry.TextChanged += OnEntryTextChanged;

void OnEntryTextChanged(object sender, TextChangedEventArgs args)
{
  // Do not change context
}
```
