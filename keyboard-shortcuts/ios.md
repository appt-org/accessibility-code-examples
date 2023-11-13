# Keyboard shortcuts - iOS

On iOS, the [`pressesBegan`](https://developer.apple.com/documentation/uikit/uiresponder/1621134-pressesbegan) and [`pressesEnded`](https://developer.apple.com/documentation/uikit/uiresponder/1621128-pressesended) can be used to activate shortcuts. But, you should use [`UIKeyCommand`](https://developer.apple.com/documentation/uikit/uikeycommand) to add keyboard shortcuts. By adding [`modifierFlags`](https://developer.apple.com/documentation/uikit/uikeymodifierflags) you can be sure that shortcuts are not activated by accident. An additional advantage is that `UIKeyCommand`-shortcuts are shown when long pressing the command key.

```swift
let find = UIKeyCommand(
    input: "f", 
    modifierFlags: .command, 
    action: #selector(findContent), 
    discoverabilityTitle: "Find"
)

override var keyCommands: [UIKeyCommand]? {
    return [find]
}

@objc private func find() {
    // Logic
}
```
