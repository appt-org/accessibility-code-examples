# Adjustable timing - Android

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
