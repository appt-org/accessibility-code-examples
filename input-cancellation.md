# Input cancellation

Users should be able to cancel accidental interaction. For example, when users accidentally touches the wrong button, they should be able to undo this and avoid performing an action. Accidental interaction is more common for people with various disabilities.

## WCAG

Relates to 2.5.2

## Android

On Android, you should avoid using the [`ACTION_DOWN`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN) event of [`OnTouchListener`](https://developer.android.com/reference/android/view/View.OnTouchListener), because users will not be able to cancel their interaction. Actions should only be activated through an [`ACTION_UP`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP) event. Use an [`OnClickListener`](https://developer.android.com/reference/android/view/View.OnClickListener) instead, because it has built-in support for cancellation.

```kotlin
webView.setOnTouchListener { _, event ->
    if (event == MotionEvent.ACTION_DOWN) {
        // Use OnClickListener instead
    }
}
```

## iOS

On iOS, you should avoid using [`touchesBegan`](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan) or [`UIControlEventTouchDown`](https://developer.apple.com/documentation/uikit/uicontrolevents/uicontroleventtouchdown) because users will not be able to cancel their interaction. Actions should only be activated through `up` events. Use a [`UITapGestureRecognizer`](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer) instead, because it has built-in support for cancellation.

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    // Use UITapGestureRecognizer instead
}
```

## Flutter

On Flutter, be careful when using a [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html) Avoid using events such as `onDown`, like `onTapDown` and `onLongPressDown`, because users will not be able to cancel their interaction. Use `onAction` events such `onTap` or `onLongPress` instead, because these have built-in support for cancellation.

```dart
@override
Widget build(BuildContext context) {
    return new GestureDetector(
        onDown: ... // Use onTap instead
    );
}
```

## React Native

In React Native, be careful when using [`PressEvent`](https://reactnative.dev/docs/pressevent). Avoid using events like [`onPressIn`](https://reactnative.dev/docs/pressable#onpressin), because users will not be able to cancel their interaction. Use events like [`onPress`](https://reactnative.dev/docs/pressable#onpressin) instead, because these have built-in support for cancellation.

```jsx
<Pressable
  onPressIn={() => {
    // Use onPress instead
  }}
/>
```

## Xamarin

In Xamarin.Forms, be careful when building a [`CustomRenderer`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/) to detect touch events. Make sure not to use the down event for actions. For tap events, you should use [`TapGestureRecognizer`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer?view=xamarin-forms).

```csharp
// Android CustomRenderer
public override bool OnTouchEvent(MotionEvent event)
{
    if (e.Action == MotionEventActions.Down)
    {
        // Don't use down event
    }
    return base.OnTouchEvent(event);
}
    
// iOS CustomRenderer
public override void TouchesBegan(NSSet touches, UIEvent event)
{
    // Don't use down event
    base.TouchesBegan(touches, event);
}
```
