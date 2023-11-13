# Localization - Android

On Android, you can use the [`createConfigurationContext`](https://developer.android.com/reference/android/content/Context#createConfigurationContext(android.content.res.Configuration)) method to load resources in the correct locale. This is especially important for users of screen readers.

```kotlin
val locales = LocaleList.forLanguageTags("nl-NL")
val configuration = baseContext.resources.configuration
configuration.setLocales(locales)
val context = createConfigurationContext(configuration)

element.text = context.resources.getString(R.string.appt)
```
