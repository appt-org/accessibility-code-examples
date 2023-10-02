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
You can use the [`accessibilityActivate`](https://developer.apple.com/documentation/objectivec/nsobject/1615165-accessibilityactivate) method to determine the action on the element when the user doubletaps.
```swift
    override func accessibilityActivate() -> Bool {
        anyFunction()
        return true // true if the element was activated or false if it was not
    }
```
