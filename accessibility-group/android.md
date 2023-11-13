# Accessibility group - Android

On Android you can group elements by using the [`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable) and [`android:screenReaderFocusable`](https://developer.android.com/reference/android/view/View#attr_android:screenReaderFocusable) attributes. Sometimes you also need the [`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility) attribute. Don't for get to set an [`android:contentDescription`](https://developer.android.com/reference/android/view/View#attr_android:contentDescription) for the group.

Keep in mind that [`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable) is not only used by assistive technologies, but also by other means of interaction.

```xml
<LinearLayout
    android:focusable="true"
    android:screenReaderFocusable="true"
    android:contentDescription="Appt group">

    <TextView
        android:focusable="false"
        android:importantForAccessibility="no"/>

    <ImageView
        android:focusable="false"
        android:importantForAccessibility="no"/>
</LinearLayout>
```
