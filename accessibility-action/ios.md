# Accessibility action - iOS

On iOS, you can use [`UIAccessibilityCustomAction`](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction) to add custom actions for assistive technologies. You can also use [`UIAccessibilityCustomRotor`](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) to add custom actions to the [VoiceOver rotor](https://appt.org/en/docs/ios/features/voiceover). Furthermore, you can use the [`accessibilityActivate`](https://developer.apple.com/documentation/objectivec/nsobject/1615165-accessibilityactivate) method to override the action that happens when a user activates an element, e.g. by double tapping with the screen reader.

```swift
// Custom action
let customAction = UIAccessibilityCustomAction(
    name: "Appt action",
    actionHandler: { (action: UIAccessibilityCustomAction) -> Bool in
        // Logic
        return true
    }
)
accessibilityCustomActions = [customAction]

// Custom rotor
let customRotor = UIAccessibilityCustomRotor(name: "Appt rotor") { predicate in
    // Logic
}
accessibilityCustomRotors = [customRotor]

// Custom activation
override func accessibilityActivate() -> Bool {
    // Logic
    return true // True if the element was activated, false if not
}
```
