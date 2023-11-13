# Screen orientation - React Native

In React Native, multiple screen orientations are enabled by default. Locking screen orientation is handled in native code:

- For Android, remove instances of the `android:screenOrientation` attribute.
- For iOS, check if 4 orientations have been added to `UISupportedInterfaceOrientations`.

You can use the [`Dimensions`](https://reactnative.dev/docs/dimensions) API to listen to orientation changes.

```jsx
Dimensions.addEventListener('change', () => {
    this.setState({
        orientation: Platform.isPortrait() ? 'portrait' : 'landscape'
    });
});
```
