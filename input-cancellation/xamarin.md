# Input cancellation - Xamarin

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
