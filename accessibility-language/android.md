# Accessibility language - Android

On Android, you can use [`LocaleSpan`](https://developer.android.com/reference/android/text/style/LocaleSpan) to speak content in a specific language. Multiple `LocaleSpan`'s can be embedded inside a [`SpannableString`](https://developer.android.com/reference/android/text/SpannableString) to speak content in multiple languages.

```kotlin
val locale = Locale.forLanguageTag("nl-NL")
val localeSpan = LocaleSpan(locale)

val string = SpannableString("Appt")
string.setSpan(localeSpan, 0, string.length, Spanned.SPAN_INCLUSIVE_INCLUSIVE)

element.setText(string)
```
