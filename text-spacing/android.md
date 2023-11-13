# Text spacing - Android

On Android, you can use the following attribute to increase text spacing:

- [`letterSpacing`](https://developer.android.com/reference/android/widget/TextView#attr_android:letterSpacing): set spacing between letters
- [`lineHeight`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineHeight): set spacing between lines
- [`lineSpacingExtra`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineSpacingExtra): increase spacing between lines
- [`lineSpacingMultiplier`](https://developer.android.com/reference/android/widget/TextView#attr_android:lineSpacingMultiplier): multiply spacing between lines
- [`marginBottom`](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams#attr_android:layout_marginBottom): set spacing between paragraphs

```xml
<TextView
    android:text="Appt"
    android:letterSpacing="3sp"
    android:lineHeight="20sp"
    android:lineSpacingExtra="5sp"
    android:lineSpacingMultiplier="1.5"
    android:layout_marginBottom="20dp"/>
```
