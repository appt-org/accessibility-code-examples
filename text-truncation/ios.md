# Text truncation - iOS

On iOS, you can avoid text truncation by seting the [`numberOfLines`](https://developer.apple.com/documentation/uikit/uilabel/1620539-numberoflines/) property to `0` on your `UILabel`. You should also avoid using fixed values for any heights or widths and instead use [`constraints`](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/WorkingwithConstraintsinInterfaceBuidler.html) and [`self-sizing`](https://developer.apple.com/documentation/uikit/uifont/creating_self-sizing_table_view_cells).

```swift
let label = UILabel()
label.text = "Avoid text truncation"
label.numberOfLines = 0
```
