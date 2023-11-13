# Keyboard order - Android

On Android, you can use several `focus` properties to modify the keyboard focus order.

- [`android:nextFocusForward`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusForward): set the next element to move focus to.
- [`android:nextFocusUp`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusUp): specify which element should receive focus when navigating up
- [`android:nextFocusDown`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusDown): specify which element should receive focus when navigating down
- [`android:nextFocusLeft`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusLeft): specify which element should receive focus when navigating to the left
- [`android:nextFocusRight`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusRight): specify which element should receive focus when navigating to the right

```xml
<View
    android:id="@+id/notFocusable"
    android:focusable="false"/>

<EditText
    android:id="@+id/field1"
    android:focusable="true"
    android:nextFocusForward="@+id/field2"
    android:nextFocusDown="@+id/field3"
    android:nextFocusRight="@+id/field2"/>

<EditText
    android:id="@+id/field2"
    android:focusable="true"
    android:nextFocusForward="@+id/field3"
    android:nextFocusDown="@+id/field4"/>

<EditText
    android:id="@+id/field3"
    android:focusable="true"
    android:nextFocusForward="@+id/field4"/>

<EditText
    android:id="@+id/field4"
    android:focusable="true"/>
```
