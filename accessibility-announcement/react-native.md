# Accessibility announcement - React Native

In React Native, you can post an accessibility message by using the [`AccessibilityInfo`](https://reactnative.dev/docs/accessibilityinfo) API. Use the [`announceForAccessibility`](https://reactnative.dev/docs/accessibilityinfo#announceforaccessibility) method to post a message to assistive technologies.

```jsx
AccessibilityInfo.announceForAccessibility('Appt announcement');
```
