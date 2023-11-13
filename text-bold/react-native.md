# Bold text - React Native

On React Native, the [`isBoldTextEnabled()`](https://reactnative.dev/docs/next/accessibilityinfo#isboldtextenabled-ios) method of [`AccessibilityInfo`](https://reactnative.dev/docs/next/accessibilityinfo) can be used to check whether the user prefers bold text.

Note: it only checks the preference on iOS. Android is not yet supported.

```jsx
import { AccessibilityInfo } from "react-native";

if (AccessibilityInfo.isBoldTextEnabled()) {
    // Use bold text
}
```
