# Input gestures - Xamarin

With Xamarin, it is common to detect gestures using one of the recognizers defined in [`Xamarin Forms Gestures`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/gestures/).

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```csharp
var pinchGesture = new PinchGestureRecognizer();
pinchGesture.PinchUpdated += (sender, event) => {
  // Provide alternative
};
view.GestureRecognizers.Add(pinchGesture);
```
