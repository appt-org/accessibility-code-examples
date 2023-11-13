# Input keyboard type - Flutter

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
