# Accessibility focus indicator - Android

On Android, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings of Android.

You can use a [`ColorStateList`](https://developer.android.com/guide/topics/resources/color-list-resource) to change colors based on the element state. An element moves into the [`state_focused`](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable#attr_android:state_focused) whenever it receives focus.

The code sample below shows how to change the background color of a button on focus.

```xml
<!-- selector.xml -->
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@color/focused" android:state_focused="true" />
    <item android:drawable="@color/default" />
</selector>

<!-- layout.xml -->
<Button
    android:id="@+id/button"
    android:background="@drawable/selector">
</Button>
```
