# Motion input - iOS

On iOS, it is common to use the [`motionEnded`](https://developer.apple.com/documentation/uikit/uiresponder/1621090-motionended) method to detect motion.

A motion event should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```swift
import UIKit

class MotionController: UIViewController {

    override var canBecomeFirstResponder: Bool{
        return true
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        becomeFirstResponder()
    }

    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        // Provide alternative
    }
}
```
