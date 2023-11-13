# Accessibility label - Android

On Android, you can use the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) attribute to set an accessibility label.

You can also pass any kind of [`Span`](https://developer.android.com/guide/topics/text/spans) for greater control over pronunciation. For example, you can set a language by using [`LocaleSpan`](https://developer.android.com/reference/android/text/style/LocaleSpan).

If another element is used to display the label, you can link the label by using the [`labelFor`](https://developer.android.com/reference/android/view/View#setLabelFor(int)) attribute.

```kotlin
// Set accessibility label
element.contentDescription = "Appt"

// Set accessibility label in Dutch language
val locale = Locale.forLanguageTag("nl-NL")
val localeSpan = LocaleSpan(locale)

val string = SpannableString("Appt")
string.setSpan(localeSpan, 0, string.length, Spanned.SPAN_INCLUSIVE_INCLUSIVE)

element.contentDescription = localeSpan

// Link visual label to field
textView.setLabelFor(R.id.editText)
```
