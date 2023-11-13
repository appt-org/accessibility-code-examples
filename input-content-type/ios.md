# Input content type - iOS

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
