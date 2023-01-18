# Frequent flashes

Rapidly flashing images or views (more than three flashes per second) can cause seizures for some users. You need to make sure this is not the case when designing and developing an app.

## WCAG

Relates to 2.3.1

## Android

On Android, flashing content often uses [`Executors`](https://developer.android.com/reference/java/util/concurrent/Executors), [`Handler`](https://developer.android.com/reference/android/os/Handler), or [`Timer`](https://developer.android.com/reference/java/util/Timer). Check if these objects are used to show more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```kotlin
Not available, contribute!
```

## iOS

On iOS, flashing content often uses [`DispatchQueue`](https://developer.apple.com/documentation/dispatch/dispatchqueue). Check if this object is used to show more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```swift
Not available, contribute!
```

## Flutter

In Flutter, flashing content often uses widgets that change on changes from a [`Stream`](https://api.flutter.dev/flutter/dart-async/Stream-class.html). For example, this could happen by using a [`StreamBuilder`](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html), and thus requesting a re-draw of certain parts of the screen. Check if these objects are used to show more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```dart
Not available, contribute!
```

## React Native

In React Native, flashing content might be a result of using [`Animated`](https://reactnative.dev/docs/animated) or [`Timers`](https://reactnative.dev/docs/timers). By default, each animation will take 500 milliseconds. Make sure your animations does not result in more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```jsx
setTimeout(() => {
    // Avoid three flashes per second
}, 500);
```

## Xamarin

In Xamarin.Forms, flashing content might be a result of using [`Timer`](https://learn.microsoft.com/en-us/dotnet/api/System.Threading.Timer?view=net-7.0) or [`ViewExtensions`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.viewextensions?view=xamarin-forms) for animations. By default, each animation will take 250 milliseconds. Make sure your animations does not result in more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```csharp
Not available, contribute!
```
