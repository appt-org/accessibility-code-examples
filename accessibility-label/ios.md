# Accessibility label - iOS

On iOS, you can use the [`accessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) property to set an accessibility label.

You can also use the [`attributedAccessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/2865944-accessibilityattributedlabel) property for greater control over pronunciation. For example, spell out each character with [`.accessibilitySpeechPunctuation`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620201-accessibilityspeechpunctuation) or set a language using [`.accessibilitySpeechLanguage`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage).

The accessibility label should be as short as possible, while still being intuitive. When long labels cannot be avoided, you should use [`accessibilityUserInputLabels`](https://developer.apple.com/documentation/objectivec/nsobject/3197989-accessibilityuserinputlabels) to provide alternative labels. The primary label is first in the array, optionally followed by alternative labels in descending order of importance.

If another element is used to display the label, you can link the label by setting [`isAccessibilityElement`](https://developer.apple.com/documentation/objectivec/nsobject/1615141-isaccessibilityelement) to `false` and setting [`accessibilityLabel`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619577-accessibilitylabel) to the `value` of the label.

```swift
// Set accessibility label
element.accessibilityLabel = "Appt"

// Set accessibility label with Dutch speech engine
element.attributedAccessibilityLabel = NSAttributedString(
  string: "Appt", 
  attributes: [.accessibilitySpeechLanguage: "nl-NL"]
)

// Set accessibility label for controls
element.accessibilityUserInputLabels = ["Appt", "Alternative"]

// Link visual label
label.isAccessibilityElement = false
element.accessibilityLabel = label.text
```
