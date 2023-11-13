# Input predictable - Android

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
