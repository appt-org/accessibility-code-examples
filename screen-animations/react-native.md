# Reduced animations - React Native

In React Native, you can use [`AccessibilityInfo`](https://reactnative.dev/docs/accessibilityinfo) to check get the value of [`isReduceMotionEnabled`](https://reactnative.dev/docs/accessibilityinfo#isreducemotionenabled). If the value is `true`, you could choose to disable (non-essential) animations in your app.

```jsx
import { AccessibilityInfo } from "react-native";

if (AccessibilityInfo.isReduceMotionEnabled()) {
    // Disable animations
}
```
