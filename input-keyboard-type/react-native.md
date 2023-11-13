# Input keyboard type - React Native

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
