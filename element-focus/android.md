# Element focus change - Android

On Android, you can use an [`OnFocusChangeListener`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener) to listen to focus changes. The [`onFocusChange`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener#onFocusChange(android.view.View,%20boolean)) method is called when the element receives focus.

Be careful when using the `onFocusChange` method: do not trigger any context change because they might confuse users.

```kotlin
webView.setOnFocusChangeListener { view, focused ->
    if (focused) {
        // Do not change context
    }
}
```
