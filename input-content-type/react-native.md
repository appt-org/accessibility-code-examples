# Input content type - React Native

In React Native,there are different properties for Android and iOS to set the content type. For Android, you can use the [`autoComplete`](https://reactnative.dev/docs/textinput#autocomplete-android) property. For iOS, you can use the [`textContentType`](https://reactnative.dev/docs/textinput#textcontenttype-ios) property.

Available values for `autoComplete` on Android:

- `birthdate-day`
- `birthdate-full`
- `birthdate-month`
- `birthdate-year`
- `cc-csc`
- `cc-exp`
- `cc-exp-day`
- `cc-exp-month`
- `cc-exp-year`
- `cc-number`
- `email`
- `gender`
- `name`
- `name-family`
- `name-given`
- `name-middle`
- `name-middle-initial`
- `name-prefix`
- `name-suffix`
- `password`
- `password-new`
- `postal-address`
- `postal-address-country`
- `postal-address-extended`
- `postal-address-extended-postal-code`
- `postal-address-locality`
- `postal-address-region`
- `postal-code`
- `street-address`
- `sms-otp`
- `tel`
- `tel-country-code`
- `tel-national`
- `tel-device`
- `username`
- `username-new`
- `off`

Available values for `textContentType` on iOS:

- `none`
- `URL`
- `addressCity`
- `addressCityAndState`
- `addressState`
- `countryName`
- `creditCardNumber`
- `emailAddress`
- `familyName`
- `fullStreetAddress`
- `givenName`
- `jobTitle`
- `location`
- `middleName`
- `name`
- `namePrefix`
- `nameSuffix`
- `nickname`
- `organizationName`
- `postalCode`
- `streetAddressLine1`
- `streetAddressLine2`
- `sublocality`
- `telephoneNumber`
- `username`
- `password`
- `newPassword`
- `oneTimeCode`

```jsx
<TextInput
    autoComplete='email'
    textContentType='emailAdress'
/>
```
