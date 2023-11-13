# Input instructions - Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show instructions.

You can also use a [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which contains a  [`setHelperText`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHelperText(java.lang.CharSequence)) method to provide instructions. To show instructions, you need to set [`setHelperTextEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHelperTextEnabled(boolean)) to `true`.

```kotlin
input.setHelperTextEnabled(true)
input.setHelperText("Your password should be at least 8 characters.")
```
