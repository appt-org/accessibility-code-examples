# Input keyboard type - Xamarin

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
