# Accessibility state - .NET MAUI

.NET MAUI does not have built-in support to indicate the accessibility state. 

By intercepting the handler changed event you can change the StateDescription (Android) or AccessibilityValue (iOS).

**CustomEntry.xaml**
```xml
    <Entry
        x:Name="txt"
        HandlerChanged="Entry_HandlerChanged"
        HeightRequest="48"
        IsSpellCheckEnabled="false"
        MaxLength="40"
        Text="{Binding Text}" />
```

**CustomEntry.xaml.Android.cs**
```c#
public partial class PinTilesCodeEntryView
{
    private AndroidX.AppCompat.Widget.AppCompatEditText? editor;

    private void Entry_HandlerChanged(object? sender, EventArgs? e)
    {
        if (sender == txt && txt.Handler?.PlatformView is AndroidX.AppCompat.Widget.AppCompatEditText editField)
        {
            if (editor == null)
            {
                editor = editField;
                editor.TextChanged += HandleTextChanged;

                // No fullscreen editing in landscape-mode
                editor.ImeOptions = Microsoft.Maui.Controls.Platform.Android.ImeActionExtensions.ToPlatform(Microsoft.Maui.Controls.PlatformConfiguration.AndroidSpecific.ImeFlags.NoFullscreen);
            }

            if (Android.OS.Build.VERSION.SdkInt >= Android.OS.BuildVersionCodes.R)
                editor.StateDescription = $"{editor.Length()} of {txt.MaxLength}";

            editor.Hint = null;
        }
    }

    private void HandleTextChanged(object? sender, Android.Text.TextChangedEventArgs e)
    {
        if (editor != null)
        {
            editor.ContentDescription = "Email";

            if (Android.OS.Build.VERSION.SdkInt >= Android.OS.BuildVersionCodes.R)
            {
                editor.StateDescription = $"{editor.Length()} of {txt.MaxLength}";
                SemanticScreenReader.Announce($"{editor.ContentDescription} {editor.StateDescription}");
            }
        }
    }
}
```

**CustomEntry.xaml.iOS.cs**
```c#
private void Entry_HandlerChanged(object? sender, EventArgs? e)
{
    if (sender == txt && txt.Handler?.PlatformView is UITextField textField)
    {
        textField.AccessibilityLabel = "E-mail";
        textField.AccessibilityLanguage = ((IApp)Application.Current!).GeneralPreferences.Language;

        textField.EditingChanged += TextField_EditingChanged;
    }
}

private void TextField_EditingChanged(object? sender, EventArgs e)
{
    if (sender is UITextField textField)
    {
        var length = textField.Text?.Length ?? 0;
        var semantics = $"{length} of {txt.MaxLength}";
        
        textField.AccessibilityLabel = CodeType.Translate();
        textField.AccessibilityValue = $"{textField.Text}, {semantics}";

        SemanticScreenReader.Announce($"{textField.AccessibilityLabel} {textField.AccessibilityValue}");
    }
}
```
