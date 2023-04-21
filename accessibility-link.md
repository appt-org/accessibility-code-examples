# Accessibility link

Links should be accessible for users of assistive technologies. When accessibility is not taken into account, users might not be able to find or activate links.

## WCAG

Relates to 2.4.4

## Android

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

## iOS

On iOS, links should contain the [`link`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535719-link) attribute. This attribute can be added through the [`addAttribute`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1417080-addattribute) method of [`NSMutableAttributedString`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring)

To create text links, you can show the `attributed string` by using the the [`attributedText`](https://developer.apple.com/documentation/uikit/uilabel/1620542-attributedtext) property of [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel).

```swift
guard let url = URL(string: "https://appt.org") else { return }
let link = "Appt"

let attributedString = NSMutableAttributedString(string: "Learn more about \(link)")

let range = attributedString.mutableString.range(of: link)
attributedString.addAttribute(.link, value: url, range: range)

let label = UILabel()
label.attributedText = attributedString
```

## Flutter

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

## React Native

In React Native, links should have their [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole) set to `link`. You can use  [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) or [`accessibilityHint`](https://reactnative.dev/docs/accessibility#accessibilityhint) to provide additional context.

To create text links, you can embed a [`Text`](https://reactnative.dev/docs/text) component inside a [`Pressable`](https://reactnative.dev/docs/pressable) component.

The [`Linking API`](https://reactnative.dev/docs/linking) can be used to open links.

```jsx
<Pressable
  onPress={async () => {
    const supported = await Linking.canOpenURL(url);
    if (supported) {
      await Linking.openURL(url);
    }
  }}
  accessibilityRole="link"
  accessibilityLabel="Appt"
  accessibilityHint="External link"
>
  <Text>Appt</Text>
</Pressable>
```

## Xamarin

In Xamarin, you need to follow four steps to create links:

1. Set the `TextColor` and `TextDecoration` properties of the [`Label`](/en-us/dotnet/api/xamarin.forms.label) or [`Span`](/en-us/dotnet/api/xamarin.forms.span).
2. Add a [`TapGestureRecognizer`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer) to the [`GestureRecognizers`](/en-us/dotnet/api/xamarin.forms.gestureelement.gesturerecognizers#xamarin-forms-gestureelement-gesturerecognizers) collection of the [`Label`](/en-us/dotnet/api/xamarin.forms.label) or [`Span`](/en-us/dotnet/api/xamarin.forms.span), whose [`Command`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer.command#xamarin-forms-tapgesturerecognizer-command) property binds to a `ICommand`, and whose [`CommandParameter`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer.commandparameter#xamarin-forms-tapgesturerecognizer-commandparameter) property contains the URL to open.
3. Define the `ICommand` that will be executed by the [`TapGestureRecognizer`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer).
4. Write the code that will be executed by the `ICommand`.

For more information, see [Xamarin Hyperlinks](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label#hyperlinks), it includes information how you can create your own [Hyperlink class](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label#creating-a-reusable-hyperlink-class).

```xml
<Label>
    <Label.FormattedText>
        <FormattedString>
            <Span Text="Read more about " />
            <Span Text="Appt"
                  TextColor="Blue"
                  TextDecorations="Underline">
                <Span.GestureRecognizers>
                    <TapGestureRecognizer Command="{Binding TapCommand}"
                                          CommandParameter="https://appt.org" />
                </Span.GestureRecognizers>
            </Span>
        </FormattedString>
    </Label.FormattedText>
</Label>
```
