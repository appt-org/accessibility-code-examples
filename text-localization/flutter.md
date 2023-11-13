# Localization - Flutter

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
