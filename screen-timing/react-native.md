# Adjustable timing - React Native

In React Native, the [`react-native-root-toast`](https://github.com/magicismight/react-native-root-toast) is often used to display temporary messages. The display duration might be too short for people to read or hear the message.

We recommend use the `SnackBar` in `react-native-paper` instead. Set the `duration` to [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) to keep it visible. Don't forget to add a close button.

Also make sure that the use of time limits, e.g. by using [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout), can be extended.

```jsx
import { Button, Snackbar } from 'react-native-paper';

<Snackbar
    visible={visible}
    onDismiss={onDismissSnackBar}
    duration={Number.MAX_SAFE_INTEGER}
    action={{
        label: 'Close',
        onPress: () => {
            // Close
        },
    }}>
    Appt
</Snackbar>
```
