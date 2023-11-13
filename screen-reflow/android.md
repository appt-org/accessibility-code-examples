# Reflow - Android

On Android, all elements should be placed in a scrollable layout, such as a [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView) or [`RecyclerView`](https://developer.android.com/jetpack/androidx/releases/recyclerview). Never use fixed values for any heights or widths.

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Content should scroll!" />
</ScrollView>
```
