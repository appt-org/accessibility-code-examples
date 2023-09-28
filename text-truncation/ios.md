On iOS, you can avoid text truncation by removing all instances of [`maxNumberOfLines`](https://developer.apple.com/documentation/uikit/nstextcontainer/1444531-maximumnumberoflines) from your app. You should also avoid using fixed values for any heights or widths and instead use [`constraints`](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/WorkingwithConstraintsinInterfaceBuidler.html) and [`self-sizing`](https://developer.apple.com/documentation/uikit/uifont/creating_self-sizing_table_view_cells).

```swift
let label = UILabel()
label.text = "Avoid text truncation"
label.maxNumberOfLines = REMOVE
```
