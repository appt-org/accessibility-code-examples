# Reflow - iOS

On iOS, all elements should be placed in a scrollable layout, such as [`UIScrollView`](https://developer.apple.com/documentation/uikit/uiscrollview), [`UITableView`](https://developer.apple.com/documentation/uikit/views_and_controls/table_views) or [`UICollectionView`](https://developer.apple.com/documentation/uikit/views_and_controls/collection_views). Never use fixed values for any heights or widths.

```swift
let label = UILabel()
label.text = "Content should scroll!"

let view = UIView()
view.addSubview(label)

let scrollView = UIScrollView()
scrollView.addSubview(view)
```
