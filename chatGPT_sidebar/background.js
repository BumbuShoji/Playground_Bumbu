chrome.action.onClicked.addListener(function() {
  chrome.windows.getCurrent(function(currentWindow) {
    chrome.windows.create({
      url: "sidebar.html",
      type: "popup",
      width: 300,
      height: 600,
      left: currentWindow.left + currentWindow.width - 300,
      top: 0
    });
  });
});