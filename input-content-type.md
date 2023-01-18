# Input content type

Setting the content type for input fields helps user entering data. For example, an e-mail address and password can be autofilled by a password manager. When the content type has not been set, this might not be possible to do automatically.

## WCAG

Relates to 1.3.5

## Android

On Android, you can set a content type by using the [`android:optimizeForAutoFill`](https://developer.android.com/reference/android/R.styleable#View_autofillHints) property.

The following values are defined:

- [`creditCardExpirationDate`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE): auto-fillcredit card expiration date
- [`creditCardExpirationDay`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY): credit card expiration day
- [`creditCardExpirationMonth`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH): credit card expiration month
- [`creditCardExpirationYear`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR): credit card expiration year
- [`creditCardNumber`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_NUMBER): credit card number
- [`creditCardSecurityCode`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE): credit card security code
- [`emailAddress`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_EMAIL_ADDRESS): email address
- [`name`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_NAME): name
- [`password`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_PASSWORD): password
- [`phone`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_PHONE): phone number
- [`postalAddress`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_POSTAL_ADDRESS): postal address
- [`postalCode`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_POSTAL_CODE): postal code
- [`username`](https://developer.android.com/reference/android/view/View#AUTOFILL_HINT_USERNAME): username

Example of using `autofillHints`:

```xml
<EditText
    android:autofillHints="emailAddress" />
```

## iOS

On iOS, you can set a content type by using the [`textContentType`](https://developer.apple.com/documentation/uikit/uitextinputtraits/1649656-textcontenttype) property.

The following values are defined in [`UITextContentType`](https://developer.apple.com/documentation/uikit/uitextcontenttype):

- [`addressCity`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649648-addresscity): entering a city
- [`addressCityAndState`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649657-addresscityandstate): entering a city and state
- [`addressState`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649654-addressstate): entering a state
- [`countryName`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649650-countryname): entering a country
- [`creditCardNumber`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1778267-creditcardnumber): entering a credit card number
- [`dateTime`](https://developer.apple.com/documentation/uikit/uitextcontenttype/3750919-datetime): entering a date, time, or duration
- [`emailAddress`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649660-emailaddress): entering an email address
- [`familyName`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649662-familyname): entering a family name, or last name
- [`flightNumber`](https://developer.apple.com/documentation/uikit/uitextcontenttype/3750920-flightnumber): entering an airline flight number
- [`fullStreetAddress`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649661-fullstreetaddress): entering a street address that fully identifies a location
- [`givenName`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649659-givenname): entering a first name
- [`jobTitle`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649667-jobtitle): entering a job title
- [`location`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649646-location): entering a location
- [`middleName`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649653-middlename): entering a middle name
- [`name`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649669-name): entering a name
- [`namePrefix`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649647-nameprefix): entering a prefix or title
- [`nameSuffix`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649665-namesuffix): entering a suffix
- [`newPassword`](https://developer.apple.com/documentation/uikit/uitextcontenttype/2980929-newpassword): entering a new password
- [`nickname`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649652-nickname): entering a nickname
- [`oneTimeCode`](https://developer.apple.com/documentation/uikit/uitextcontenttype/2980930-onetimecode): entering a one-time code
- [`organizationName`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649666-organizationname): entering an organization name
- [`password`](https://developer.apple.com/documentation/uikit/uitextcontenttype/2865813-password): entering a password
- [`postalCode`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649649-postalcode): entering a postal code
- [`shipmentTrackingNumber`](https://developer.apple.com/documentation/uikit/uitextcontenttype/3750921-shipmenttrackingnumber): entering a parcel tracking number
- [`streetAddressLine1`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649663-streetaddressline1): entering the first line of an address
- [`streetAddressLine2`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649658-streetaddressline2): entering the second line of an address
- [`sublocality`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649655-sublocality): entering a sublocality
- [`telephoneNumber`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649664-telephonenumber): entering a telephone number
- [`URL`](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649651-url): entering a URL
- [`username`](https://developer.apple.com/documentation/uikit/uitextcontenttype/2866088-username): entering a username

Example of using `textContentType`:

```swift
emailField.textContentType = .emailAddress
```

## Flutter

In Flutter, you can set a content type by using the [`autoFillHints`](https://api.flutter.dev/flutter/services/AutofillHints-class.html) property. 

It's important to note that constants are platform dependent and don't work the same everywhere, or even at all.

The following constants are defined:

- [`addressCity`](services/AutofillHints/addressCity-constant.html): The input field expects an address locality (city/town).
- [`addressCityAndState`](services/AutofillHints/addressCityAndState-constant.html): The input field expects a city name combined with a state name.
- [`addressState`](services/AutofillHints/addressState-constant.html): The input field expects a region/state.
- [`birthday`](services/AutofillHints/birthday-constant.html): The input field expects a person's full birth date.
- [`birthdayDay`](services/AutofillHints/birthdayDay-constant.html): The input field expects a person's birth day(of the month).
- [`birthdayMonth`](services/AutofillHints/birthdayMonth-constant.html): The input field expects a person's birth month.
- [`birthdayYear`](services/AutofillHints/birthdayYear-constant.html): The input field expects a person's birth year.
- [`countryCode`](services/AutofillHints/countryCode-constant.html): The input field expects an [ISO 3166-1-alpha-2](https://www.iso.org/standard/63545.html) country code.
- [`countryName`](services/AutofillHints/countryName-constant.html): The input field expects a country name.
- [`creditCardExpirationDate`](services/AutofillHints/creditCardExpirationDate-constant.html): The input field expects a credit card expiration date.
- [`creditCardExpirationDay`](services/AutofillHints/creditCardExpirationDay-constant.html): The input field expects a credit card expiration day.
- [`creditCardExpirationMonth`](services/AutofillHints/creditCardExpirationMonth-constant.html): The input field expects a credit card expiration month.
- [`creditCardExpirationYear`](services/AutofillHints/creditCardExpirationYear-constant.html): The input field expects a credit card expiration year.
- [`creditCardFamilyName`](services/AutofillHints/creditCardFamilyName-constant.html): The input field expects the holder's last/family name as given on a credit card.
- [`creditCardGivenName`](services/AutofillHints/creditCardGivenName-constant.html): The input field expects the holder's first/given name as given on a credit card.
- [`creditCardMiddleName`](services/AutofillHints/creditCardMiddleName-constant.html): The input field expects the holder's middle name as given on a credit card.
- [`creditCardName`](services/AutofillHints/creditCardName-constant.html): The input field expects the holder's full name as given on a credit card.
- [`creditCardNumber`](services/AutofillHints/creditCardNumber-constant.html): The input field expects a credit card number.
- [`creditCardSecurityCode`](services/AutofillHints/creditCardSecurityCode-constant.html): The input field expects a credit card security code.
- [`creditCardType`](services/AutofillHints/creditCardType-constant.html): The input field expects the type of a credit card, for example "Visa".
- [`email`](services/AutofillHints/email-constant.html): The input field expects an email address.
- [`familyName`](services/AutofillHints/familyName-constant.html): The input field expects a person's last/family name.
- [`fullStreetAddress`](services/AutofillHints/fullStreetAddress-constant.html): The input field expects a street address that fully identifies a location.
- [`gender`](services/AutofillHints/gender-constant.html): The input field expects a gender.
- [`givenName`](services/AutofillHints/givenName-constant.html): The input field expects a person's first/given name.
- [`impp`](services/AutofillHints/impp-constant.html): The input field expects a URL representing an instant messaging protocol endpoint.
- [`jobTitle`](services/AutofillHints/jobTitle-constant.html): The input field expects a job title.
- [`language`](services/AutofillHints/language-constant.html): The input field expects the preferred language of the user.
- [`location`](services/AutofillHints/location-constant.html): The input field expects a location, such as a point of interest, an address,or another way to identify a location.
- [`middleInitial`](services/AutofillHints/middleInitial-constant.html): The input field expects a person's middle initial.
- [`middleName`](services/AutofillHints/middleName-constant.html): The input field expects a person's middle name.
- [`name`](services/AutofillHints/name-constant.html): The input field expects a person's full name.
- [`namePrefix`](services/AutofillHints/namePrefix-constant.html): The input field expects a person's name prefix or title, such as "Dr.".
- [`nameSuffix`](services/AutofillHints/nameSuffix-constant.html): The input field expects a person's name suffix, such as "Jr.".
- [`newPassword`](services/AutofillHints/newPassword-constant.html): The input field expects a newly created password for save/update.
- [`newUsername`](services/AutofillHints/newUsername-constant.html): The input field expects a newly created username for save/update.
- [`nickname`](services/AutofillHints/nickname-constant.html): The input field expects a nickname.
- [`oneTimeCode`](services/AutofillHints/oneTimeCode-constant.html): The input field expects a SMS one-time code.
- [`organizationName`](services/AutofillHints/organizationName-constant.html): The input field expects an organization name corresponding to the person, address, or contact information in the other fields associated with this field.
- [`password`](services/AutofillHints/password-constant.html): The input field expects a password.
- [`photo`](services/AutofillHints/photo-constant.html): The input field expects a photograph, icon, or other image corresponding to the company, person, address, or contact information in the other fields associated with this field.
- [`postalAddress`](services/AutofillHints/postalAddress-constant.html): The input field expects a postal address.
- [`postalAddressExtended`](services/AutofillHints/postalAddressExtended-constant.html): The input field expects an auxiliary address details.
- [`postalAddressExtendedPostalCode`](services/AutofillHints/postalAddressExtendedPostalCode-constant.html): The input field expects an extended ZIP/POSTAL code.
- [`postalCode`](services/AutofillHints/postalCode-constant.html): The input field expects a postal code.
- [`streetAddressLevel1`](services/AutofillHints/streetAddressLevel1-constant.html): The first administrative level in the address. This is typically the province in which the address is located. In the United States, this would be the state. In Switzerland, the canton. In the United Kingdom, the post town.
- [`streetAddressLevel2`](services/AutofillHints/streetAddressLevel2-constant.html): The second administrative level, in addresses with at least two of them. In countries with two administrative levels, this would typically be the city, town, village, or other locality in which the address is located.
- [`streetAddressLevel3`](services/AutofillHints/streetAddressLevel3-constant.html): The third administrative level, in addresses with at least three administrative levels.
- [`streetAddressLevel4`](services/AutofillHints/streetAddressLevel4-constant.html): The finest-grained administrative level, in addresses which have four levels.
- [`streetAddressLine1`](services/AutofillHints/streetAddressLine1-constant.html): The input field expects the first line of a street address.
- [`streetAddressLine2`](services/AutofillHints/streetAddressLine2-constant.html): The input field expects the second line of a street address.
- [`streetAddressLine3`](services/AutofillHints/streetAddressLine3-constant.html): The input field expects the third line of a street address.
- [`sublocality`](services/AutofillHints/sublocality-constant.html): The input field expects a sublocality.
- [`telephoneNumber`](services/AutofillHints/telephoneNumber-constant.html): The input field expects a telephone number.
- [`telephoneNumberAreaCode`](services/AutofillHints/telephoneNumberAreaCode-constant.html): The input field expects a phone number's area code, with a country -internal prefix applied if applicable.
- [`telephoneNumberCountryCode`](services/AutofillHints/telephoneNumberCountryCode-constant.html): The input field expects a phone number's country code.
- [`telephoneNumberDevice`](services/AutofillHints/telephoneNumberDevice-constant.html): The input field expects the current device's phone number, usually for Sign Up / OTP flows.
- [`telephoneNumberExtension`](services/AutofillHints/telephoneNumberExtension-constant.html): The input field expects a phone number's internal extension code.
- [`telephoneNumberLocal`](services/AutofillHints/telephoneNumberLocal-constant.html): The input field expects a phone number without the country code and area code components.
- [`telephoneNumberLocalPrefix`](services/AutofillHints/telephoneNumberLocalPrefix-constant.html): The input field expects the first part of the component of the telephone number that follows the area code, when that component is split into two components.
- [`telephoneNumberLocalSuffix`](services/AutofillHints/telephoneNumberLocalSuffix-constant.html): The input field expects the second part of the component of the telephone number that follows the area code, when that component is split into two components.
- [`telephoneNumberNational`](services/AutofillHints/telephoneNumberNational-constant.html): The input field expects a phone number without country code.
- [`transactionAmount`](services/AutofillHints/transactionAmount-constant.html): The amount that the user would like for the transaction (e.g. when entering a bid or sale price).
- [`transactionCurrency`](services/AutofillHints/transactionCurrency-constant.html): The currency that the user would prefer the transaction to use, in [ISO 4217 currency code](https://www.iso.org/iso-4217-currency-codes.html).
- [`url`](services/AutofillHints/url-constant.html): The input field expects a URL.
- [`username`](services/AutofillHints/username-constant.html): The input field expects a username or an account name.

```dart
TextFormField(
    autofillHints: [AutofillHints.email]
)
```

## React Native

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

## Xamarin

Xamarin.Forms does not support content types for input fields. You can create your own [autofill effect](https://mikalaidaronin.info/blog/posts/xamarin-forms-password-autofill/). Unfortunately, the [pull request for adding it to XamarinCommunitToolkit](https://github.com/xamarin/XamarinCommunityToolkit/issues/702) has been closed.

```csharp
Not available, contribute!
```
