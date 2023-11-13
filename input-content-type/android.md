# Input content type - Android

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
