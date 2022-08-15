# A11YEffect - iOS implementation

## Xamarin

You can find the iOS implementation of A11YEffect below:

```csharp
using System;
using System.Linq;
using System.Threading.Tasks;
using Project.Common.Constants;
using Project.Common.Controls;
using Project.Common.Effects;
using Foundation;
using LabelHtml.Forms.Plugin.Abstractions;
using UIKit;
using Xamarin.Forms;
using Xamarin.Forms.Platform.iOS;
using A11YEffect = Project.iOS.Effects.A11YEffect;
using CoreEffect = Project.Common.Effects.A11YEffect;

[assembly: ResolutionGroupName(AppConfigConstants.A11YEffectGroupName)]
[assembly: ExportEffect(typeof(A11YEffect), nameof(A11YEffect))]
namespace Project.iOS.Effects
{
    public class A11YEffect : PlatformEffect
    {
        protected override void OnAttached()
        {
            try
            {
                if (!(Element.Effects?.FirstOrDefault(e => e is Common.Effects.A11YEffect) is Common.Effects.A11YEffect))
                    return;

                if (Control != null)
                {
                    SetEffectOnControl(Control);
                }
                else if (Container != null && Container is UIView container)
                {
                    SetEffectOnControl(container);
                }
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine($"====> Error in A11Effect.OnAttached: {typeof(Element)} - {e.Message}");
            }
        }

        private void SetEffectOnControl(UIView control)
        {
            var text = AutomationProperties.GetName(Element);
            var hint = AutomationProperties.GetHelpText(Element);
            var inA11YTree = AutomationProperties.GetIsInAccessibleTree(Element).GetValueOrDefault(true);

            if (inA11YTree)
            {
                control.IsAccessibilityElement = inA11YTree;
                control.AccessibilityLabel = text;
                control.AccessibilityHint = hint;
                var newControlType = CoreEffect.GetControlType(Element);

                if (Container != null)
                {
                    // het Element is een Container
                    control.ShouldGroupAccessibilityChildren = true;
                }
                if (newControlType == A11YControlTypes.None)
                {
                    control.AccessibilityTraits = UIAccessibilityTrait.None;
                    return;
                }
                if (newControlType == A11YControlTypes.Button || newControlType == A11YControlTypes.Toggle)
                {
                    if (Element is Switch @switch)
                    {
                        var labelText = "";
                        if (AutomationProperties.GetLabeledBy(@switch) is Label label)
                            labelText = label.Text;
                        control.AccessibilityLabel = labelText;
                    }
                    else
                    {
                        control.AccessibilityTraits = UIAccessibilityTrait.None;
                        control.AccessibilityTraits = UIAccessibilityTrait.Button;
                    }
                }
                else if (newControlType == A11YControlTypes.Link)
                {
                    control.AccessibilityTraits = UIAccessibilityTrait.Link;
                    if (Element is Button)
                    {
                        if (control is UIButton btn)
                        {
                            var txt = new NSMutableAttributedString(btn.CurrentTitle);
                            txt.AddAttribute(UIStringAttributeKey.UnderlineStyle, NSObject.FromObject(NSUnderlineStyle.Single), new Foundation.NSRange(0, btn.CurrentTitle.Length));
                            btn.SetAttributedTitle(txt, UIControlState.Normal);
                            btn.LineBreakMode = UILineBreakMode.WordWrap;
                            btn.HorizontalAlignment = UIControlContentHorizontalAlignment.Left;
                        }
                    }
                    else if (Element is Label labelWithHyperlinkSpan && !(Element is HtmlLabel))
                    {
                        if (labelWithHyperlinkSpan.FormattedText != null)
                        {
                            CheckForGestureRecognizers(control, labelWithHyperlinkSpan);
                        }
                        else
                        {
                            // if the text does not contain hyperlinks then  do not speak the text that it is a link
                        
                            if (!string.IsNullOrEmpty(text) && (text.Contains("<a href") || text.Contains("&lt;a href")))
                                control.AccessibilityTraits ^= UIAccessibilityTrait.Link;
                        }
                    }
                    else
                    {
                        // If Element has link-effect, check the text, if emtpy then delete link-effect
                        if (Element is HtmlLabel htmlLabel)
                        {
                            if (string.IsNullOrEmpty(htmlLabel.Text))
                            {
                                control.AccessibilityTraits ^= UIAccessibilityTrait.Link;
                                AutomationProperties.SetIsInAccessibleTree(Element, false);
                            }
                            if (htmlLabel.Text != null && !(htmlLabel.Text.Contains("<a href") || htmlLabel.Text.Contains("&lt;a href")))
                                control.AccessibilityTraits ^= UIAccessibilityTrait.Link;
                        }
                    }
                }

                if (newControlType == A11YControlTypes.Header)
                    control.AccessibilityTraits = UIAccessibilityTrait.Header;

                if (newControlType == A11YControlTypes.LiveUpdate && (Element is Label || Element is CustomErrorLabel))
                {
                    Element.PropertyChanged += Element_PropertyChanged;
                }
            }
        }

        private void CheckForGestureRecognizers(UIView control, Label labelWithHyperlinkSpan)
        {
            var spans = labelWithHyperlinkSpan.FormattedText?.Spans;
            if (spans == null)
                return;
            foreach (var span in spans)
                foreach (var gr in span.GestureRecognizers)
                    labelWithHyperlinkSpan.GestureRecognizers.Add(gr);
        }

        private void Element_PropertyChanged(object sender, System.ComponentModel.PropertyChangedEventArgs e)
        {
            var text = "";

            if (sender is Label label)
            {
                if (e.PropertyName.Equals(Label.TextProperty.PropertyName) ||
                    e.PropertyName.Equals(AutomationProperties.NameProperty.PropertyName) ||
                    (e.PropertyName.Equals(Label.IsVisibleProperty.PropertyName) && label.IsVisible))
                {
                    var a11yTxt = AutomationProperties.GetName(label);
                    text = string.IsNullOrEmpty(a11yTxt) ? label.Text : a11yTxt;
                }
            }
            else if (sender is CustomErrorLabel errorLabel)
            {
                if (e.PropertyName.Equals(nameof(errorLabel.ErrorText)) || e.PropertyName.Equals(nameof(errorLabel.IsVisible)))
                {
                    text = errorLabel.ErrorText;
                }
            }
            if (!string.IsNullOrEmpty(text))
            {
                Task.Run(async () =>
                {
                    System.Diagnostics.Debug.WriteLine($"\nA11YEffect.Element_PropertyChanged: '{text}'");
                    await Task.Delay(2000);
                    UIAccessibility.PostNotification(UIAccessibilityPostNotification.Announcement, NSObject.FromObject(text));
                });
            }
        }

        protected override void OnDetached()
        {
            if (Element is Label label && CoreEffect.GetControlType(Element) == A11YControlTypes.LiveUpdate)
            {
                Element.PropertyChanged -= Element_PropertyChanged;
            }
        }
    }
}
```

See also [AutomationProperties](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties)
