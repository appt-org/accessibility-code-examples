# Accessibility role - .NET MAUI

.NET MAUI does not have built-in support for setting an accessibility role.

By intercepting the handler changed event you can change the role of a custom component.

 Component.xaml
 ```xml
    <StackLayout AutomationProperties.IsInAccessibleTree="False" BindableLayout.ItemsSource="{Binding Steps}">
        <BindableLayout.ItemTemplate>
            <DataTemplate x:Name="Model" x:DataType="model:Step">
                <controls:BorderedFrame
                    Padding="0"
                    BackgroundColor="Transparent"
                    CornerRadius="10"
                    HandlerChanged="Frame_HandlerChanged"
                    HasShadow="False"
                    IsEnabled="{Binding IsActive}">
                    <Grid...>
                    </Grid>
                    <Frame.GestureRecognizers>
                        <TapGestureRecognizer Command="{Binding Command}" />
                    </Frame.GestureRecognizers>
                </controls:BorderedFrame>
            </DataTemplate>
        </BindableLayout.ItemTemplate>
    </StackLayout>
```
---
Write the Android specific code for Frame_HandlerChanged in a partial class and set the native attributes to set the role.

***Component.Android.cs***
```c#
public partial class Component
{
    void Frame_HandlerChanged(System.Object sender, System.EventArgs e)
    {
        if (sender is Frame frame && frame.Handler?.PlatformView is Android.Widget.FrameLayout view)
        {
            ViewCompat.SetAccessibilityDelegate(view, new CustomFrameDelegate(ViewCompat.GetAccessibilityDelegate(view)));
            ConfigFrame(frame);
        }
    }
    private void ConfigFrame(Frame? frame)
    {
        if (frame != null && frame.Handler != null && frame.Handler.PlatformView is Android.Widget.FrameLayout view)
        {
            if (frame!.IsEnabled)
            {
                view.Focusable = true;
                view.Clickable = true;
                view.Click -= FrameClicked;
                view.Click += FrameClicked;
            }
            else
            {
                view.Clickable = false;
                view.Focusable = false;
            }
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
---
Write the iOS specific code for Frame_HandlerChanged in a partial class and set the native attributes to set the role.

***Component.iOS.cs***
```c#
public partial class Component
{
    void Frame_HandlerChanged(System.Object sender, System.EventArgs e)
    {
        if (sender is Frame frame && frame.Handler != null)
        {
            var uiButton = (UIView)frame.Handler.PlatformView!;
            var subTitle = frame.FindByName<Label>("SubTitle").Text;

            if (frame.IsEnabled && frame.FindByName("Title") is Label label)
            {
                uiButton.UserInteractionEnabled = true;
                uiButton.AccessibilityTraits = UIAccessibilityTrait.Button;
                uiButton.AccessibilityLabel = $"{SemanticProperties.GetDescription(label)}, {subTitle}";
            }
            else
            {
                uiButton.UserInteractionEnabled = false;
                uiButton.AccessibilityTraits = UIAccessibilityTrait.None;
                uiButton.AccessibilityLabel = "";
                var tapGesture = (TapGestureRecognizer)frame.GestureRecognizers.First(g => g is TapGestureRecognizer);
                frame.GestureRecognizers.Remove(tapGesture);
            }
        }
    }
}
```
