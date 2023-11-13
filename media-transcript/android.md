# Transcript - Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to display written text. Don't forget to put it in a [ScrollView](https://developer.android.com/reference/android/widget/ScrollView), to make the text scrollable.

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Appt transcript" />
</ScrollView>
```
