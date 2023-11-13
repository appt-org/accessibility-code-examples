# Input cancellation - Android

On Android, you should avoid using the [`ACTION_DOWN`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN) event of [`OnTouchListener`](https://developer.android.com/reference/android/view/View.OnTouchListener), because users will not be able to cancel their interaction. Actions should only be activated through an [`ACTION_UP`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP) event. Use an [`OnClickListener`](https://developer.android.com/reference/android/view/View.OnClickListener) instead, because it has built-in support for cancellation.

```kotlin
webView.setOnTouchListener { _, event ->
    if (event == MotionEvent.ACTION_DOWN) {
        // Use OnClickListener instead
    }
}
```
