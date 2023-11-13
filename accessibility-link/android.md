# Accessibility link - Android

On Android, links should be embedded inside an [`URLSpan`](https://developer.android.com/reference/android/text/style/URLSpan.html).

To create text links, you can show the `span` in using the [`setText`](https://developer.android.com/reference/android/widget/TextView#setText(java.lang.CharSequence)) method of [`TextView`](https://developer.android.com/reference/android/widget/TextView). To support assistive technologies on lower version of Android, you need to call the [`ViewCompat.enableAccessibleClickableSpanSupport()`](https://developer.android.com/reference/androidx/core/view/ViewCompat#enableAccessibleClickableSpanSupport(android.view.View)) method.

The helper method [`ViewCompat.addLinks()`](https://developer.android.com/reference/android/text/util/Linkify#addLinks(android.text.Spannable,%20int)) is also useful to automatically create accessible links.

Warning: you have to remove the [`android:autoLink`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoLink) attribute from your XML to make your `URLSpan`'s clickable.

```kotlin
val textView = TextView(this)

val url = "https://appt.org"
val link = "Appt"

val spannableString = SpannableString("Learn more about $link")

val index = spannableString.indexOf(link)
spannableString.setSpan(URLSpan(url), index, index + link.length, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE)

textView.text = spannableString
textView.movementMethod = LinkMovementMethod.getInstance()

ViewCompat.enableAccessibleClickableSpanSupport(textView)
```
