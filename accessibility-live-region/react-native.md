# Accessibility live region - React Native

On React Native, the [`accessibilityLiveRegion`](https://reactnative.dev/docs/accessibility#accessibilityliveregion-android) prop can be used to indicate a live region. The value can be set to `asssertive` to interrupt ongoing speech to for immediate announcements on change. The `polite` value can be used to queue announcements. The `none` value can be used to disable announcements on change.

```jsx
<Text accessibilityLiveRegion="assertive|polite|none">
  Appt live region
</Text>
```
