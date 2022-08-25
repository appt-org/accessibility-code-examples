# Motion action

Provide an alternative way for actions activated by motion, to allow everyone to use the functionality. For example, for users with limited hand function, shaking is not always possible. Also make it possible to disable actions activated by motion. For example, for users with spasms, these actions could be triggered accidently.

## Android

On Android, the [`SensorManager`](https://developer.android.com/reference/android/hardware/SensorManager) can be used in combination with [`SensorEventListener`](https://developer.android.com/reference/android/hardware/SensorEventListener) to detect movement.

An event through sensors should not be the only way to trigger actions. Make sure to add a second way, such as a button, to trigger the same action.

```kotlin
Not available, contribute!
```

## iOS

On iOS, it is common to use the [`motionEnded`](https://developer.apple.com/documentation/uikit/uiresponder/1621090-motionended) method to detect motion.

A motion event should not be the only way to trigger actions. Make sure to add a second way, such as a button, to trigger the same action.

```swift
Not available, contribute!
```

## Flutter

With Flutter, packages like [sensors_plus](https://pub.dev/packages/sensors_plus) can be used to detect movement.

An event through sensors should not be the only way to trigger actions. Make sure to add a second way, such as a button, to trigger the same action.

```dart
Not available, contribute!
```

## React Native

In React Native, packages like [`expo-sensors`](https://docs.expo.dev/versions/latest/sdk/sensors/) can be used to detect motion.

An event through sensors should not be the only way to trigger actions. Make sure to add a second way, such as a button, to trigger the same action.

```jsx
Not available, contribute!
```

## Xamarin

In Xamarin, the [`Accelerometer`](https://docs.microsoft.com/en-us/xamarin/essentials/accelerometer) class can be used to listen to changes in acceleration of the device in three-dimensional space.

An event through acceleration should not be the only way to trigger actions. Make sure to add a second way, such as a button, to trigger the same action.

```xml
Not available, contribute!
```
