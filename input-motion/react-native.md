# Motion input - React Native

In React Native, packages like [`expo-sensors`](https://docs.expo.dev/versions/latest/sdk/sensors/) can be used to detect motion.

An event through sensors should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```jsx
import { Accelerometer } from 'expo-sensors';

export default function App() {
  const _subscribe = () => {
    setSubscription(
      Accelerometer.addListener(accelerometerData => {
        // Provide alternative
      })
    );
  };
}
```
