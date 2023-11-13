# Input label - Android

On Android, you can link labels to controls by using the [`labelFor`](https://developer.android.com/reference/android/view/View#setLabelFor(int)) attribute. We recommend using a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to show labels for input fields.

You can also use [`TextInputLayout`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout), which allows you to create an input field with a label. The [`hint`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHint(java.lang.CharSequence)) property at the `TextInputLayout` level is used as visual `label`. The [`hintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setHintEnabled(boolean)) and [`expandedHintEnabled`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setExpandedHintEnabled(boolean)) properties must be set to `true` to always show the label.

```xml
<TextView android:text="Name" android:labelFor="@+id/field"/>
<EditText id="@+id/field" hint="Enter your name"/>

<com.google.android.material.textfield.TextInputLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:hintEnabled="true"
    app:expandedHintEnabled="true"
    android:hint="Name">

    <com.google.android.material.textfield.TextInputEditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name"/>
</com.google.android.material.textfield.TextInputLayout>
```
