# Keyboard shortcuts - Android

On Android, you can use the [`dispatchKeyEvent`](https://developer.android.com/reference/android/view/View#dispatchKeyEvent(android.view.KeyEvent)) and [`onKeyUp`](https://developer.android.com/reference/android/app/Activity#onKeyUp(int,%20android.view.KeyEvent)) methods to activate shortcuts. Both methods give you a reference to a [`KeyEvent`](https://developer.android.com/reference/android/view/KeyEvent) object. Use the [`isShiftPressed`](https://developer.android.com/reference/android/view/KeyEvent#isShiftPressed()) or [`isCtrlPressed`](https://developer.android.com/reference/android/view/KeyEvent#isCtrlPressed()) method to make sure that shortcuts are not activated by accident.

```kotlin
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
    return when (keyCode) {
        KeyEvent.KEYCODE_F -> {
            if (event.isCtrlPressed) {
                find()
                true
            }
        }
        else -> super.onKeyUp(keyCode, event)
    }
}

private fun find() {
    // Logic
}
```
