# Keyboard shortcuts - React Native

React Native does not support binding custom key events for shortcuts. The package [`react-native-keyevent`](https://github.com/kevinejohn/react-native-keyevent) allows you to capture external keyboard keys. However, it [only works on Android](https://github.com/kevinejohn/react-native-keyevent).

```jsx
componentDidMount() {
    KeyEvent.onKeyMultipleListener((keyEvent) => {
        console.log(`onKeyMultiple keyCode: ${keyEvent.keyCode}`);
        console.log(`Action: ${keyEvent.action}`);
        console.log(`Characters: ${keyEvent.characters}`);
    });
}

componentWillUnmount() {
    KeyEvent.removeKeyMultipleListener();
}
```
