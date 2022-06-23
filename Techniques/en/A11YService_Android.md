# A11YService - Android implementation
## Xamarin

You can find the iOS implementation of A11YService below:

```csharp
// TODO: Add required imports
[assembly: Dependency(typeof(A11YService))]
namespace Project.Droid.Services
{
    public class A11YService : IA11YService
    {
        private readonly AccessibilityManager _accessibilityManager = (AccessibilityManager)Xamarin.Essentials.Platform.CurrentActivity.GetSystemService(Context.AccessibilityService);

        public bool IsInVoiceOverMode()
        {
            return _accessibilityManager.IsTouchExplorationEnabled;
        }

        public async Task Speak(string text, int pauseInMs = 0)
        {
            if (IsInVoiceOverMode() && !string.IsNullOrEmpty(text))
            {
                if (pauseInMs > 0)
                    await Task.Delay(pauseInMs);
                Xamarin.Essentials.Platform.CurrentActivity.Window?.DecorView?.AnnounceForAccessibility(text.StripHtml());
            }
        }

        public void NotifyForNewPage()
        {
            if (!IsInVoiceOverMode())
                return;

            Device.BeginInvokeOnMainThread(async () =>
            {
                var @event = AccessibilityEvent.Obtain();
                @event.EventType = EventTypes.WindowsChanged;
                await Task.Delay(250);
                _accessibilityManager.SendAccessibilityEvent(@event);
            });
        }

        public void ChangeA11YFocus(VisualElement visualElement)
        {
            if (!IsInVoiceOverMode() || visualElement == null)
                return;

            Task.Run(async () =>
            {
                var view = visualElement.GetViewForAccessibility();
                await Task.Delay(250);
                view?.SendAccessibilityEvent(EventTypes.ViewAccessibilityFocused);
            });
        }

        private void SetFocusOnFirstChild(Layout<Xamarin.Forms.View> container)
        {
            if (container != null && container.Children?.Count > 0)
            {
                var firstChild = container.Children.FirstOrDefault(v => AutomationProperties.GetIsInAccessibleTree(v) ?? true);
                if (firstChild is Layout<Xamarin.Forms.View> fc)
                    SetFocusOnFirstChild(fc );
                else
                {
                    var firstNativeChild = Platform.GetRenderer(firstChild)?.View ?? Platform.CreateRendererWithContext(firstChild, Xamarin.Essentials.Platform.CurrentActivity.ApplicationContext).View;
                    SetFocusOnFoundChild(firstNativeChild);
                }
            }
        }

        private void SetFocusOnFoundChild(Android.Views.View firstNativeChild)
        {
            if (firstNativeChild != null)
            {
                firstNativeChild.ImportantForAccessibility = ImportantForAccessibility.Yes;

                var @event = AccessibilityEvent.Obtain();
                @event.EventType = EventTypes.ViewFocused;
                @event.EventTime = DateTimeOffset.Now.ToUnixTimeSeconds();

                @event.SetSource(firstNativeChild);
                @event.FullScreen = false;

                _accessibilityManager.SendAccessibilityEvent(@event);
            }
        }
    }
}
```

The above code depends on the `GetViewForAccessibility()` Android extension on `Xamarin.Forms.VisualElement`:

```csharp
using Android.Views;
using Xamarin.Forms;
using Xamarin.Forms.Platform.Android;

namespace Project.Droid.Extensions
{
    public static class Extensions
    {
        public static global::Android.Views.View GetViewForAccessibility(this Xamarin.Forms.VisualElement visualElement)
        {
            var renderer = Platform.GetRenderer(visualElement);

            if (visualElement is Layout)
                return renderer?.View;
            else if (renderer is ViewGroup vg && vg.ChildCount > 0)
                return vg.GetChildAt(0);
            else if (renderer != null)
                return renderer.View;


            return renderer?.View;
        }
    }
}
```

See also [AutomationProperties](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties)
