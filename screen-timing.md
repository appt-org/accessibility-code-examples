# Adjustable timing

Everyone, including people with disabilities, should have adequate time to interact with your app. People with disabilities may require more time to interact with your app. If certain functions are time-dependent, it will be difficult for some users to finish in time. If content is shown for a limited time, users might not finish reading in time. It should be possible for users to increase time limits, or ideally, disable all time limits.

## WCAG

Relates to 2.2.1

## Android

On Android, a [`Toast`](https://developer.android.com/reference/android/widget/Toast) is often used display temporary messages. The display duration might be too short for people to read or hear the message.

We recommend displaying messages by using an [`AlertDialog`](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog) or [`Snackbar`](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar) with the duration set to [`LENGTH_INDEFINITE`](https://developer.android.com/reference/com/google/android/material/snackbar/BaseTransientBottomBar#LENGTH_INDEFINITE). Don't forget to add a close button.

Also check whether [`Executors`](https://developer.android.com/reference/java/util/concurrent/Executors), [`Handler`](https://developer.android.com/reference/android/os/Handler) or [`Timer`](https://developer.android.com/reference/java/util/Timer) are used somewhere. If there are any time limits, make sure they can be extended.

```kotlin
val snackbar = Snackbar
    .make(view, "Appt", Snackbar.LENGTH_INDEFINITE)
    .setAction("Close") {
        // Close
    }
snackbar.show()
```

## iOS

On iOS,  third-party code libraries are sometimes used to display a temporary message, also known as a `Toast`. The display duration might be too short for people to read or hear the message.

We recommend showing messages by using an [`UIAlertController`](https://developer.apple.com/documentation/uikit/uialertcontroller). Don't forget to add a close button.

Also check whether [`DispatchQueue`](https://developer.apple.com/documentation/dispatch/dispatchqueue) is used somewhere. If there are time limits, make sure they can be extended.

```swift
let alert = UIAlertController(
  title: nil, 
  message: "Appt", 
  preferredStyle: .alert
)

alert.addAction(UIAlertAction(title: "Close", style: .default, handler: { action in
  // Close
}))

present(alert, animated: true)
```

## Flutter

In Flutter, a [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html) is often used display temporary messages. The display duration might be too short for people to read or hear the message.

We recommend displaying messages by using an [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html). Or, when using a `Snackbar`, you can set the duration to "`infinite`". Don't forget to add a close button for both options.

Also make sure that the use of time limits, e.g. by using [`Future.delayed()`](https://api.flutter.dev/flutter/dart-async/Future/Future.delayed.html), can be extended.

```dart
ScaffoldMessenger.of(context).showSnackBar(SnackBar(
  duration: const Duration(days: 1),
  content: Text('Appt'),
  action: SnackBarAction(
    label: 'Close',
    onPressed: () {
      ScaffoldMessenger.of(context).hideCurrentSnackBar();
    },
  ),
));
```

## React Native

In React Native, the [`react-native-root-toast`](https://github.com/magicismight/react-native-root-toast) is often used to display temporary messages. The display duration might be too short for people to read or hear the message.

We recommend use the `SnackBar` in `react-native-paper` instead. Set the `duration` to [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) to keep it visible. Don't forget to add a close button.

Also make sure that the use of time limits, e.g. by using [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout), can be extended.

```jsx
import { Button, Snackbar } from 'react-native-paper';

<Snackbar
    visible={visible}
    onDismiss={onDismissSnackBar}
    duration={Number.MAX_SAFE_INTEGER}
    action={{
        label: 'Close',
        onPress: () => {
            // Close
        },
    }}>
    Appt
</Snackbar>
```

## Xamarin

In Xamarin, the `SnackBar` view from the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) is often used to display temporary messages. The display duration might be too short for people to read or hear the message.

When using `SnackBar`, set the `Duration` to `Int32.MaxValue`. Or, use [`DisplayAlert`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.displayalert?view=xamarin-forms) method to show an alert instead.

Also make sure that the use of time limits, e.g. by using [`Timer`](https://learn.microsoft.com/en-us/dotnet/api/System.Threading.Timer?view=net-7.0), can be extended.

```csharp
var result = await page.DisplaySnackBarAsync("Appt", "Close", async () =>
    { /* Action */ },
    Int32.MaxValue
);
```
