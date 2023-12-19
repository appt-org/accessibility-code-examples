# Accessibility role - .NET MAUI

.NET MAUI does not have built-in support for setting an accessibility role.

By intercepting the handler changed event you can change the role of a custom component.

```xml title="Component.xaml"
<StackLayout>
  <BindableLayout.ItemTemplate>
    <DataTemplate>
      <controls:BorderedFrame
        HandlerChanged="Frame_HandlerChanged">
        <Grid...>
        </Grid>
        <Frame.GestureRecognizers>
          <TapGestureRecognizer/>
        </Frame.GestureRecognizers>
      </controls:BorderedFrame>
    </DataTemplate>
  </BindableLayout.ItemTemplate>
</StackLayout>
```

Partial class on Android:

```c# title="Component.Android.cs"
public partial class Component
{
  void Frame_HandlerChanged(System.Object sender, System.EventArgs e)
  {
    if (sender is Frame frame && frame.Handler?.PlatformView is Android.Widget.FrameLayout view)
    {
      ViewCompat.SetAccessibilityDelegate(view, new CustomFrameDelegate(ViewCompat.GetAccessibilityDelegate(view)));
    }
  }
}

public class CustomFrameDelegate : AccessibilityDelegateCompatWrapper
{
    public CustomFrameDelegate(AccessibilityDelegateCompat? originalDelegate) : base(originalDelegate)
    {
    }

    public override void OnInitializeAccessibilityNodeInfo(Android.Views.View host, AccessibilityNodeInfoCompat info)
    {
        base.OnInitializeAccessibilityNodeInfo(host, info);
        if (info != null)
            info.ClassName = "android.widget.Button";
    }
}
```

Partial class on iOS:

```c# title="Component.iOS.cs"
public partial class Component
{
  void Frame_HandlerChanged(System.Object sender, System.EventArgs e)
  {
    if (sender is Frame frame && frame.Handler != null)
    {
      var view = (UIView)frame.Handler.PlatformView!;
      view.AccessibilityTraits = UIAccessibilityTrait.Button;
    }
  }
}
```
