# Accessibility announcement - .NET MAUI

.NET MAUI does have built-in support for posting an accessibility message to the VoiceOver or Talkback engine.

```csharp
    SemanticScreenReader.Default.Announce("This is the announcement text.");
```

Another possibility is to make an A11YService with a delayed Speak function. For example: IA11yService

```csharp
    public interface IA11YService
    {
        bool IsInVoiceOverMode { get; }
        Task Speak(string? text, int pauseInMs = 0);
    }
```

```csharp
    // iOS implementation
    public bool IsInVoiceOverMode => UIAccessibility.IsVoiceOverRunning;

    public Task Speak(string? text, int pauseInMs = 0)
    {
        if (IsInVoiceOverMode && !string.IsNullOrEmpty(text))
        {
            if (pauseInMs > 0)
            {
                var dict = new NSMutableDictionary
                {
                    { UIView.SpeechAttributeQueueAnnouncement, new NSString("Yes") }
                };
                UIAccessibility.PostNotification(UIAccessibilityPostNotification.Announcement, new NSAttributedString(str: text, attributes: dict));
            }
            else
                UIAccessibility.PostNotification(UIAccessibilityPostNotification.Announcement, new NSString(text));
        }
        return Task.CompletedTask;
    }
```

```csharp
    // Android implementation
    private static AccessibilityManager? AccessibilityManager => Android.App.Application.Context.GetSystemService(Android.Content.Context.AccessibilityService) as AccessibilityManager;
    
    public bool IsInVoiceOverMode => AccessibilityManager is { IsEnabled: true, IsTouchExplorationEnabled: true };

    public async Task Speak(string? text, int pauseInMs = 0)
    {
        if (IsInVoiceOverMode && !string.IsNullOrEmpty(text))
        {
            if (pauseInMs > 0)
                await Task.Delay(pauseInMs);
            try
            {
                SemanticScreenReader.Announce(text);
            }
            catch (Exception e)
            {
                // Sometimes we get an exception: MauiContext must be set on parent
                System.Diagnostics.Debug.WriteLine($"!!!!!!!!=======> A11YService.Android.Speak exception: {e.Message}");
            }
        }
    }
```                                 