# Input keyboard type - Android

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
