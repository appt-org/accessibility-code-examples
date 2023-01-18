# Accessibility dialog

A dialog overlays the screen and offers one or more actions to proceed. Dialogs should always include a close button to make them accessible for users of assistive technologies. Furthermore, the focus of assistive technologies should be trapped inside the dialog while it's visible.

## WCAG

Relates to 1.4.13, 2.1.2, 3.3.4

## Android

On Android, you can [show a dialog](https://developer.android.com/guide/topics/ui/dialogs) by using [`AlertDialog`](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog), [`BottomSheetDialog`](https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialog) or [`DialogFragment`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment). You should always add a close button by using the [`setNegativeButton`](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog.Builder#setNegativeButton(int,android.content.DialogInterface.OnClickListener)) method. The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```kotlin
val builder = AlertDialog.Builder(this)
builder.setTitle("Confirm Appt membership?")
builder.setMessage("Your bank account will be billed.")

builder.setPositiveButton("Proceed") { dialog, which ->
  // Proceed
}

builder.setNegativeButton("Cancel") { dialog, which ->
  // Cancel
}

builder.show()
```

## iOS

On iOS, you can [show alerts](https://developer.apple.com/design/human-interface-guidelines/ios/views/alerts/) by using [`UIAlertController`](https://developer.apple.com/documentation/uikit/uialertcontroller). Set the `style` to [`alert`](https://developer.apple.com/documentation/uikit/uialertcontroller/style/alert) to display a  dialog. You should always add a close action in the [`cancel`](https://developer.apple.com/documentation/uikit/uialertaction/style/cancel) style. The focus of assistive technologies is automatically trapped inside the alert while it's visible.

```swift
let alert = UIAlertController(
  title: "Confirm Appt membership?", 
  message: "Your bank account will be billed.", 
  preferredStyle: .alert
)

alert.addAction(UIAlertAction(title: "Proceed", style: .default, handler: { action in
  // Proceed
}))

alert.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: { action in
  // Cancel
}))

present(alert, animated: true)
```

## Flutter

With Flutter, you can use [`SimpleDialog`](https://api.flutter.dev/flutter/material/SimpleDialog-class.html), [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html) or [`CupertinoAlertDialog`](https://api.flutter.dev/flutter/cupertino/CupertinoAlertDialog-class.html) to show alerts. An `AlertDialog` is styled liked an Android dialog. A `CupertinoAlertDialog` is styled like an iOS dialog. You should always supply a close action in the `actions` array. The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```dart
showDialog(
  context: context,
  builder: (context) => AlertDialog(
    title: Text('Confirm Appt membership?'),
    content: Text('Your bank account will be billed.'),
    actions: [
      TextButton(
        onPressed: confirmTransaction,
        child: const Text('Proceed'),
      ),
      TextButton(
        onPressed: () => Navigator.pop(context),
        child: const Text('Cancel'),
      )
    ],
  ),
);
```

## React Native

In React Native, you can use [`Alert`](https://reactnative.dev/docs/alert) to show a dialog. On [Android](https://reactnative.dev/docs/alert#android) you can add a neutral, negative and positive button, this is based on the amount of buttons that are set. On iOS it's possible to set the [AlertButtonStyle](https://reactnative.dev/docs/alert#alertbuttonstyle-ios) for each button. You should always include a button to close the dialog. The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```jsx
Alert.alert(
  "Confirm Appt membership?",
  "Your bank account will be billed.",
  [
    {
      text: "Cancel",
      onPress: () => {
        // Cancel
      },
      style: "cancel"
    },
    {
      text: "Proceed",
      onPress: () => {
        // Proceed
      },
    },
  ],
  {
      cancelable: true,
      onDismiss: () => console.log("Dismissed alert"),
  }
);
```

## Xamarin

In Xamarin Forms you can use the [`DisplayAlert`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.displayalert?view=xamarin-forms) method to show an alert. The last parameter of the method is the text of cancel button and it is required to supply it. Therefore, a cancel button is always shown! The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```csharp
var accept = await App.Current.MainPage.DisplayAlert(
  "Confirm Appt membership?", 
  "Your bank account will be billed.",
  "Proceed",
  "Cancel"
);

if (accept) {
    // Proceed
} else {
    // Cancel
}
```
