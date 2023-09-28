On iOS, you can use [`UIAccessibilityCustomAction`](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction) to add custom actions for assistive technologies. You can also use [`UIAccessibilityCustomRotor`](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) to add custom actions to the [VoiceOver rotor](https://beta.appt.org/en/docs/ios/features/voiceover).

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
```
