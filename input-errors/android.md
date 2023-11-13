# Input errors - Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show an error message. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which makes showing error messages easier. Set [`setErrorEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setErrorEnabled(boolean)) to `true` and then set the error message by using the [`setError`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#seterror) method.

```kotlin
textView.setVisibility(View.VISIBLE)
textView.text = "Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000"

input.setErrorEnabled(true)
input.setError("Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000")
```
