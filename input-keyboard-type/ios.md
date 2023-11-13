# Input keyboard type - iOS

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
