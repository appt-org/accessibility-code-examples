# Localization - React Native

In React Native, there is no standard for loading resources in your desired language. Various packages are available to help you achieve this. You can use [expo-localization](https://docs.expo.dev/versions/latest/sdk/localization) in combination with [i18n-js](https://github.com/fnando/i18n-js) to get the device locale and set translations for your app.

```jsx
import * as Localization from 'expo-localization';
import i18n from 'i18n-js';

// Set the key-value pairs for the different languages you want to support.
i18n.translations = {
  en: { welcome: 'Appt accessibility' },
  nl: { welcome: 'Appt toegankelijkheid' },
};

// Set the locale once at the beginning of your app.
i18n.locale = Localization.locale;
```
