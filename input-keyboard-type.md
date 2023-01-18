# Input keyboard type

Setting the keyboard type for input fields helps user entering data. For example, if users need to enter a number, it helps to show a numeric keyboard. If users need to enter an e-mail address, it helps if the at-key (`@`) is shown. You should always set an appropriate keyboard type.

## WCAG

Relates to 1.3.5

## Android

On Android, you can set a keyboard type by using the [`android:inputType`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:inputType) property. You can combine values with each other.

The following constants are defined:

- `date`: for entering a date
- `datetime`: for entering a date and time
- `none`: to disable input
- `number`: for entering a number
- `numberDecimal`: for entering decimal numbers
- `numberPassword`: for entering a numeric password
- `numberSigned`: for entering a positive or negative number
- `phone`: for entering a telephone number
- `text`: for entering normal text
- `textAutoComplete`: to enable automatic completion
- `textAutoCorrect`: to enable automatic correction
- `textCapCharacters`: to automatically convert characters to uppercase
- `textCapSentences`: to automatically capitalize sentences
- `textCapWords`: to automatically capitalize words
- `textEmailAddress`: for entering an email address
- `textEmailSubject`: for entering the subject of an email
- `textFilter`: for entering text to filter with
- `textImeMultiLine`: to force entering multiple lines of text
- `textLongMessage`: for entering a long message
- `textMultiLine`: for entering multiple lines of text
- `textNoSuggestions`: to disable suggestions
- `textPassword`: for entering a password
- `textPersonName`: for entering a name
- `textPhonetic`: for entering phonetic text
- `textPostalAddress`: for entering a postal address
- `textShortMessage`: for entering a short message
- `textUri`: for entering a URL
- `textVisiblePassword`: for entering a visible password
- `textWebEditText`: for entering text in a web form
- `textWebEmailAddress`: for entering an email address in a web form
- `textWebPassword`: for entering a password in a web form
- `time`: for entering a time

Example of using `inputType`:

```xml
<EditText
    android:inputType="text|textMultiLine|textCapSentences" />
```

## iOS

On iOS, you can set a keyboard type by using the [`keyboardType`](https://developer.apple.com/documentation/uikit/uitextinputtraits/1624457-keyboardtype) property.

The following types are defined:

- [`asciiCapable`](https://developer.apple.com/documentation/uikit/uikeyboardtype/asciicapable): a keyboard that displays standard ASCII characters
- [`asciiCapableNumberPad`](https://developer.apple.com/documentation/uikit/uikeyboardtype/asciicapablenumberpad): a number pad that outputs only ASCII digits
- [`decimalPad`](https://developer.apple.com/documentation/uikit/uikeyboardtype/decimalpad): a keyboard with numbers and a decimal point
- [`default`](https://developer.apple.com/documentation/uikit/uikeyboardtype/default): the default keyboard
- [`emailAddress`](https://developer.apple.com/documentation/uikit/uikeyboardtype/emailaddress): a keyboard for entering email addresses
- [`namePhonePad`](https://developer.apple.com/documentation/uikit/uikeyboardtype/namephonepad): a keypad for entering a person’s name or phone number
- [`numberPad`](https://developer.apple.com/documentation/uikit/uikeyboardtype/numberpad): a numeric keypad for PIN entry
- [`numbersAndPunctuation`](https://developer.apple.com/documentation/uikit/uikeyboardtype/numbersandpunctuation): a keyboard for numbers and punctuation
- [`phonePad`](https://developer.apple.com/documentation/uikit/uikeyboardtype/phonepad): a keypad for entering telephone numbers
- [`URL`](https://developer.apple.com/documentation/uikit/uikeyboardtype/url): a keyboard for URL entry
- [`twitter`](https://developer.apple.com/documentation/uikit/uikeyboardtype/twitter): a keyboard for Twitter text entry, with easy access to the at '`@`' and hash '`#`' characters
- [`webSearch`](https://developer.apple.com/documentation/uikit/uikeyboardtype/websearch): a keyboard for web search terms and URL entry

Example of using `keyboardType`:

```swift
usernameField.keyboardType = .numberPad
```

## Flutter

In Flutter, you can set a keyboard type by using the [`keyboardType`](https://api.flutter.dev/flutter/material/TextField/keyboardType.html) property.

The following values are defined in [`TextInputType`](https://api.flutter.dev/flutter/services/TextInputType-class.html):

- [`datetime`](https://api.flutter.dev/flutter/services/TextInputType/datetime-constant.html): Keyboard optimized for entering date and time, iOS displays default keyboard.
- [`emailAddress`](https://api.flutter.dev/flutter/services/TextInputType/emailAddress-constant.html): Keyboard optimized for entering e-mail addresses.
- [`multiline`](https://api.flutter.dev/flutter/services/TextInputType/multiline-constant.html): Optimized for multiline text input, by having an enter key.
- [`name`](https://api.flutter.dev/flutter/services/TextInputType/name-constant.html): Keyboard optimized for inputting a person's name
- [`none`](https://api.flutter.dev/flutter/services/TextInputType/none-constant.html): Prevents the OS from displaying a keyboard.
- [`number`](https://api.flutter.dev/flutter/services/TextInputType/number-constant.html): Optimized for unsigned numerical input.
- [`phone`](https://api.flutter.dev/flutter/services/TextInputType/phone-constant.html): Number keyboard with '`*`' and '`#`'.
- [`streetAddress`](https://api.flutter.dev/flutter/services/TextInputType/streetAddress-constant.html): Optimized for entering addresses, iOS displays default keyboard.
- [`text`](https://api.flutter.dev/flutter/services/TextInputType/text-constant.html): Optimized for text input.
- [`url`](https://api.flutter.dev/flutter/services/TextInputType/url-constant.html): Optimized keyboard for entering URLs with '`/`' and '`.`'.
- [`visiblePassword`](https://api.flutter.dev/flutter/services/TextInputType/visiblePassword-constant.html): Keyboard with letters and numbers.

Example of using `keyboardType`:

```dart
TextField( 
  keyboardType: TextInputType.emailAddress,
)
```

## React Native

In React Native, you can set a keyboard type by using the [`keyboardType`](https://reactnative.dev/docs/textinput#keyboardtype) property.

The following values work across platforms:

- `default`
- `number-pad`
- `decimal-pad`
- `numeric`
- `email-address`
- `phone-pad`
- `url`

The following values work on iOS only:

- `ascii-capable`
- `numbers-and-punctuation`
- `name-phone-pad`
- `twitter`
- `web-search`

The following values work on Android only:

- `visible-password`

```jsx
<TextInput keyboardType="email-address" />
```

## Xamarin

In Xamarin.Forms, you can set a keyboard type by using the [`Keyboard`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.inputview.keyboard?view=xamarin-forms#xamarin-forms-inputview-keyboard) property.

The following [`Keyboard properties`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard?view=xamarin-forms#properties) are defined:

- [`Chat`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.chat?view=xamarin-forms#xamarin-forms-keyboard-chat): keyboard for chatting, includes `emoji`
- [`Default`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.default?view=xamarin-forms#xamarin-forms-keyboard-default): default keyboard
- [`Email`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.email?view=xamarin-forms#xamarin-forms-keyboard-email): keyboard for entering an e-mail, includes `@`
- [`Numeric`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.numeric?view=xamarin-forms#xamarin-forms-keyboard-numeric): keyboard for entering numbers, includes `,` and `.`
- [`Plain`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.plain?view=xamarin-forms#xamarin-forms-keyboard-plain): keyboard for entering plain text
- [`Telephone`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.telephone?view=xamarin-forms#xamarin-forms-keyboard-telephone): keyboard for entering phone numbers, includes `plus` and `hash`
- [`Text`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.text?view=xamarin-forms#xamarin-forms-keyboard-text): keyboard for entering text, includes `enter`
- [`Url`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.keyboard.url?view=xamarin-forms#xamarin-forms-keyboard-url): keyboard for entering url's, includes `/`

```xml
<Editor Keyboard="Email" />
```
