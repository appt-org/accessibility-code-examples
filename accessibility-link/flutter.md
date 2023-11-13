# Accessibility link - Flutter

In Flutter, links should have the semantic property [`link`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/link.html). 

To create text links, you can use the [`RichText`](https://api.flutter.dev/flutter/widgets/RichText-class.html) widget. You can pass multiple [`TextSpan`](https://api.flutter.dev/flutter/painting/TextSpan-class.html) widgets as it's children.

The [`url_launcher`](https://pub.dev/packages/url_launcher) package can be used to open links.

```dart
RichText(
    text: TextSpan(
        children: [
            TextSpan(
                text: 'Learn more about ',
            ),
            Semantics(
                link: true,
                label: 'Appt',
                hint: 'External link',
                child: TextSpan(
                    text: 'Appt',
                    style: TextStyle(
                        decoration: TextDecoration.underline, 
                        color: Colors.blue
                    ),
                    recognizer: TapGestureRecognizer()..onTap = () {
                        final url = Uri.parse('https://appt.org')
                        launchUrl(url)
                    },
                ),
            ),
        ],
    ),
);
```
