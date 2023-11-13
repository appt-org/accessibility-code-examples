# Accessibility dialog - Android

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
