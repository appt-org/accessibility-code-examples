# Transcript - iOS

On iOS, you can use [`UITextView`](https://developer.apple.com/documentation/uikit/uitextview) to present a transcript. A `UITextView` is scrollable by default. You can also choose to place one or more [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel)'s in a [`UIScrollView`](https://developer.apple.com/documentation/uikit/uiscrollview).

```swift
// Option 1
let transcript = UITextView()
transcript.text = "Appt transcript"

// Option 2
let transcript = UILabel()
transcript.text = "Appt transcript"

let view = UIView()
view.addSubview(transcript)

let scrollView = UIScrollView()
scrollView.addSubview(view)
```
