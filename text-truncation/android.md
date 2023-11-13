# Text truncation - Android

On Android, you can avoid text truncation by removing all instances of [`android:maxLines`](https://developer.android.com/reference/android/widget/TextView#attr_android:maxLines) from your app. You should also avoid using fixed values for any heights or widths and instead use [`wrap_content`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#WRAP_CONTENT) where possible.

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Avoid text truncation" 
    android:maxLines="REMOVE" />
```
