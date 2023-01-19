# Localization

Assistive technologies, such as the screen reader, use the locale for the pronunciation of utterances. It is important to explictly set a locale for your app. An incorrect locale leads to unclear pronunciation. Also, setting a locale can help with displaying characters correctly.

## WCAG

Relates to 3.1.2

## Android

On Android, you can use the [`createConfigurationContext`](https://developer.android.com/reference/android/content/Context#createConfigurationContext(android.content.res.Configuration)) method to load resources in the correct locale. This is especially important for users of screen readers.

```kotlin
val locales = LocaleList.forLanguageTags("nl-NL")
val configuration = baseContext.resources.configuration
configuration.setLocales(locales)
val context = createConfigurationContext(configuration)

element.text = context.resources.getString(R.string.appt)
```

## iOS

On iOS, you can set the locale of an app via the [`CFBundleDevelopmentRegion`](http://cfbundledevelopmentregion) property.  We suggest using `Base internationalization` to separate user-facing strings from `.storyboard` and `.xib files`. You can load a specific [`Bundle`](https://developer.apple.com/documentation/foundation/bundle) to load assets in the desired language.

For more information, see [Adding Support for Languages and Regions](https://developer.apple.com/documentation/xcode/adding-support-for-languages-and-regions).

```swift
extension String {
    func localized(_ language: String) -> String {
        guard let path = Bundle.main.path(forResource: language, ofType: "lproj"),
              let bundle = Bundle(path: path) else {
          return localized(Bundle.main)
        }
        return NSLocalizedString(self, tableName: nil, bundle: bundle, value: "", comment: "")
    }
}
```

## Flutter

With Flutter, you can use the various methods to load resources in your desired locale. This is especially important for users of screen readers. The example below shows a simple implementation to handle this without using any dependencies.

```dart
/// This is the main widget of the application
class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();

  static _MyAppState of(BuildContext context) => context.findAncestorStateOfType<_MyAppState>();
}

class _MyAppState extends State<MyApp> {
  /// Private variable holding the current localization
  Locale _locale;

  /// Calling this method will initialize a re-draw of the entire widget tree.
  void setLocale(Locale value) {
    setState(() {
      _locale = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      locale: _locale,
      home: LanguageButtons(),
    );
  }
}

class LanguageButtons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextButton(
          child: Text("Set locale to Dutch"),
          onPressed: () => MyApp.of(context).setLocale(Locale.fromSubtags(languageCode: 'nl')),
        ),
        TextButton(
          child: Text("Set locale to English"),
          onPressed: () => MyApp.of(context).setLocale(Locale.fromSubtags(languageCode: 'en')),
        ),
      ],
    );
  }
}
```

## React Native

In React Native, there is no standard for loading resources in your desired language. Various packages are available to help you achieve this. You can use [expo-localization](https://docs.expo.dev/versions/latest/sdk/localization) in combination with [i18n-js](https://github.com/fnando/i18n-js) to get the device locale and set translations for your app.

```jsx
import * as Localization from 'expo-localization';
import i18n from 'i18n-js';

// Set the key-value pairs for the different languages you want to support.
i18n.translations = {
  en: { welcome: 'Appt accessibility' },
  nl: { welcome: 'Appt toegankelijkheid' },
};

// Set the locale once at the beginning of your app.
i18n.locale = Localization.locale;
```

## Xamarin

With Xamarin, you can use [`CultureInfo`](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo?view=net-6.0) to set a language. For more information, see [String and Image localization in Xamarin Forms](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/localization/text?pivots=windows).

```csharp
using System.Globalization;
using System.Threading;

CultureInfo ci = CultureInfo.GetCultureInfo(DependencyService.Get<IGeneralPreferences>().Language);

CultureInfo.DefaultThreadCurrentCulture = ci;
CultureInfo.DefaultThreadCurrentUICulture = ci;
AppResources.Culture = ci;
CultureInfo.CurrentUICulture = ci;
Thread.CurrentThread.CurrentUICulture = ci;
Thread.CurrentThread.CurrentCulture = ci;
```
